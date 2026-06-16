from google import genai
from google.genai import types
from google.genai import errors
from shpeak.utils import verbose_schema, load_cmds, load_ps_cmds, get_api_key
from shpeak.data.operators import CMD_OPERATORS, POWERSHELL_OPERATORS
from shpeak.prompts import CMD_PROMPT, PS_PROMPT
import json
import re
import sys

def cmd_suggest(query: str, verbose: bool=False, test: bool=False):
    time_limit = types.HttpOptions(timeout=60_000)
    client = genai.Client(api_key=get_api_key(), http_options=time_limit)
    cmd_cmds = load_cmds()
    schema = verbose_schema(verbose)

    config = types.GenerateContentConfig(
            system_instruction=CMD_PROMPT.format(cmd_cmds=cmd_cmds, cmd_operators=CMD_OPERATORS, schema=schema),
            temperature=0.0,
            )
    try:
        response = client.models.generate_content(
            model='gemma-4-26b-a4b-it', 
            contents=query,
            config=config,
            )
        
        if not response.text:
            raise Exception("no llm response")
        raw = response.text

        clean = re.sub(r"```json|```", "", raw).strip()
        result = json.loads(clean)

        if test and response.usage_metadata:
            usage = response.usage_metadata
            print(f"Input Tokens (Prompt):   {usage.prompt_token_count}")
            print(f"Output Tokens (Response): {usage.candidates_token_count}")
            print(f"Total Tokens Used:       {usage.total_token_count}")

        return result
    
    except TimeoutError as e:
    # If the request takes longer than 30 seconds, it will raise a timeout error here
        print(f"Request failed or timed out: {e}")
        sys.exit(1)
    except errors.ServerError as e:
        print(f"Google API Server Error: {e.message}")
        sys.exit(1)
        # Fallback logic goes here (e.g., return a default message to your user)
    except errors.APIError as e:
        # Catches other API errors (like 400 Bad Request, 429 Quota Exceeded)
        print(f"A general API error occurred: {e}")
        sys.exit(1)
    
def ps_suggest(query: str, verbose: bool=False, test: bool=False):
    time_limit = types.HttpOptions(timeout=60_000)
    client = genai.Client(api_key=get_api_key(), http_options=time_limit)
    client = genai.Client(api_key=get_api_key())
    powershell_cmds = load_ps_cmds()
    schema = verbose_schema(verbose)

    config = types.GenerateContentConfig(
            system_instruction=PS_PROMPT.format(powershell_commands=powershell_cmds, powershell_operators=POWERSHELL_OPERATORS, schema=schema),
            temperature=0.0,
            )
    try:
        response = client.models.generate_content(
            model='gemma-4-26b-a4b-it', 
            contents=query,
            config=config,
            )
        
        if not response.text:
            raise Exception("no llm response")
        raw = response.text

        clean = re.sub(r"```json|```", "", raw).strip()
        result = json.loads(clean)

        if test and response.usage_metadata:
            usage = response.usage_metadata
            print(f"Input Tokens (Prompt):   {usage.prompt_token_count}")
            print(f"Output Tokens (Response): {usage.candidates_token_count}")
            print(f"Total Tokens Used:       {usage.total_token_count}")

        return result
    
    except TimeoutError as e:
    # If the request takes longer than 30 seconds, it will raise a timeout error here
        print(f"Request failed or timed out: {e}")
        sys.exit(1)
    except errors.ServerError as e:
        print(f"Google API Server Error: {e.message}")
        sys.exit(1)
    # Fallback logic goes here (e.g., return a default message to your user)
    except errors.APIError as e:
    # Catches other API errors (like 400 Bad Request, 429 Quota Exceeded)
        print(f"A general API error occurred: {e}")
        sys.exit(1)
