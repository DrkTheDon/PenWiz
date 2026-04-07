import os
import subprocess

def install_tool(tool_name):
    print(f"Installerar {tool_name}...")
    subprocess.run(["sudo", "apt", "install", "-y", tool_name])

def wizard():
    print("Startar installations wizard...\n")

    val = input("Vill du installera nmap? (y/n): ")
    if val.lower() == "y":
        install_tool("nmap")

    val = input("Vill du installera wireshark? (y/n): ")
    if val.lower() == "y":
        install_tool("wireshark")

    val = input("Vill du installera git? (y/n): ")
    if val.lower() == "y":
        install_tool("git")

    print("\nKlart!")

def main():
    print("1. Wizard (rekommenderas)")
    print("2. Installera alla verktyg")

    val = input("Välj: ")

    if val == "1":
        wizard()
    elif val == "2":
        install_tool("nmap")
        install_tool("wireshark")
        install_tool("git")
    else:
        print("Fel val")

if __name__ == "__main__":
    main()
