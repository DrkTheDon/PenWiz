#!/usr/bin/env python3
########################################
# Project: PenWiz                      #
# Author: DrkTheDon                    #
# Description:                         #
# A simple Penetration Testing Wizard  #
########################################

import argparse
import subprocess
import sys
import os

# Banner (enkel version utan extra bibliotek)
def banner():
    print("====================================")
    print("           PenWiz CLI")
    print("====================================")


def run_installation():
    """Kör installation.py"""
    install_script = os.path.join(os.path.dirname(__file__), "installation.py")

    if os.path.exists(install_script):
        try:
            subprocess.run([sys.executable, install_script], check=True)
        except subprocess.CalledProcessError:
            print("Fel uppstod vid installation.")
    else:
        print("installation.py hittades inte.")


def main():
    banner()

    parser = argparse.ArgumentParser(
        prog="penwiz",
        description="PenWiz - enkelt installationsverktyg"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="PenWiz v0.01"
    )

    parser.add_argument(
        "--install",
        action="store_true",
        help="Starta installations wizard"
    )

    args = parser.parse_args()

    if args.install:
        run_installation()
    else:
        print("\nProgrammet körs!")
        print("Använd --install för att starta installationen\n")


if __name__ == "__main__":
    main()
