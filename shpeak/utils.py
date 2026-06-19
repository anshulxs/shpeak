import json
import os
from pathlib import Path
from dotenv import load_dotenv
import getpass
from rich.console import Console
from importlib.resources import files
console = Console()

CONFIG_DIR = Path.home() / ".config" / "shpeak"
CONFIG_FILE = CONFIG_DIR / "config.env"


def verbose_schema(verbose: bool=False) -> str:
    schema = '''{
    "intent": "<restate the user's goal in one sentence>",
    "available": true | false,
    "error": "<if available is false, explain why — otherwise null>",
    "irreversible": true | false,
    "warning": {
        "description": "<exactly what will permanently change — null if irreversible is false>",
        "precaution": "<pointer on specific backup or verification step — null if irreversible is false>"
    },
    "command": "<the command — null if unavailable>"
        '''
    if verbose:
        schema += ''',"breakdown": {
    "command": "<command name>",
    "description": "<description from dictionary>",
    "parameters": "<explain each flag/parameter used>",
    "expected_output": "<what the user should see>"
    },
    "safer": {
        "command": "<the safer command — null if none exists>",
        "explanation": "<why this is safer and what it does differently — null if none exists>"
        }'''
    schema += "\n}"

    return schema

def get_api_key():
    # 1. Check environment variable (lets power users override)
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    # 2. Check saved config file
    if CONFIG_FILE.exists():
        load_dotenv(CONFIG_FILE)
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            return api_key

    # 3. First run — prompt and save
    console.print("Looks like this is your first time running shpeak.")
    api_key = api_key = getpass.getpass("Please enter your Gemini API key: ")

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(f"GEMINI_API_KEY={api_key}\n")
    CONFIG_FILE.chmod(0o600)  # restrict to owner read/write only

    console.print(f"Saved! (stored at {CONFIG_FILE})")
    return api_key