#!/usr/bin/env python3
########################################
# Project: PenWiz                      #
# Author: DrkTheDon                    #
# Bakgrouund:                          #
# A Penetration Testing Wizard for all #
# kinds of tools.                      #
########################################

################################################################################

### Imports
import argparse
import subprocess
import sys
import os
import pyfiglet


def banner():
    ascii_banner = pyfiglet.figlet_format("PenWiz")
    print(ascii_banner)


def run_installation():
    """Run installation.py if requested."""
    install_script = os.path.join(os.path.dirname(__file__), "installation.py")
    if os.path.exists(install_script):
        subprocess.run([sys.executable, install_script], check=True)
    else:
        print("No installation.py found.")


def main():
    banner()  # show banner at start

    parser = argparse.ArgumentParser(
        prog="penwiz",
        description="PenWiz CLI Tool"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="PenWiz 1.0"
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Run installation script"
    )

    args = parser.parse_args()

    if args.install:
        run_installation()
    else:
        print("PenWiz running! Add more CLI options here.")
