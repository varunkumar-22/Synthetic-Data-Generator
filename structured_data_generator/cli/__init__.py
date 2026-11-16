"""
Command line interface: sdg generate, sdg profile <file>
"""

import argparse

from structured_data_generator.cli import generate, profile


def main():
    parser = argparse.ArgumentParser(prog="sdg", description="Synthetic data generator")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("generate", help="Generate a dataset interactively")
    profile_parser = commands.add_parser("profile", help="Profile a CSV or JSON dataset")
    profile_parser.add_argument("file", help="path to a .csv or .json file")

    args = parser.parse_args()
    if args.command == "generate":
        generate.main()
    else:
        profile.main(args.file)
