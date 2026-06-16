import argparse
from shpeak.translator import cmd, ps


def main():
    parser = argparse.ArgumentParser(description="Natural Language to Terminal(scary) Commands CLI")
    subparser = parser.add_subparsers(dest="command", help="Available Commands")

    cmd_parser = subparser.add_parser("cmd", help="For CMD commands")
    cmd_parser.add_argument("query", type=str, help="Describe your command")
    cmd_parser.add_argument("-v", "--verbose", action="store_true", help="Understand the CMD command")

    ps_parser = subparser.add_parser("ps", help="For POWERSHELL commands")
    ps_parser.add_argument("query", type=str, help="Describe your command")
    ps_parser.add_argument("-v", "--verbose", action="store_true", help="Understand the POWERSHELL command")

    args = parser.parse_args()

    match args.command:
        case "cmd":
            cmd(args.query, args.verbose)

        case "ps":
            ps(args.query, args.verbose)

        case _:
            parser.print_help()