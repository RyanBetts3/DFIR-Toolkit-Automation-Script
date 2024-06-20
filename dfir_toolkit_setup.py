import os
import subprocess
import platform
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {' '.join(command)}")
        logging.error(f"Error message: {str(e)}")

def install_volatility():
    logging.info("Installing Volatility...")
    execute_command(["pip", "install", "volatility"])

def install_rekall():
    logging.info("Installing Rekall...")
    execute_command(["pip", "install", "rekall"])

def install_autopsy():
    logging.info("Installing Autopsy...")
    if platform.system() == "Windows":
        execute_command(["choco", "install", "autopsy", "-y"])
    elif platform.system() == "Linux":
        execute_command(["sudo", "apt-get", "install", "autopsy", "-y"])
    elif platform.system() == "Darwin":
        execute_command(["brew", "cask", "install", "autopsy"])

def install_wireshark():
    logging.info("Installing Wireshark...")
    if platform.system() == "Windows":
        execute_command(["choco", "install", "wireshark", "-y"])
    elif platform.system() == "Linux":
        execute_command(["sudo", "apt-get", "install", "wireshark", "-y"])
    elif platform.system() == "Darwin":
        execute_command(["brew", "cask", "install", "wireshark"])

def install_sleuthkit():
    logging.info("Installing The Sleuth Kit...")
    if platform.system() == "Windows":
        execute_command(["choco", "install", "sleuthkit", "-y"])
    elif platform.system() == "Linux":
        execute_command(["sudo", "apt-get", "install", "sleuthkit", "-y"])
    elif platform.system() == "Darwin":
        execute_command(["brew", "install", "sleuthkit"])

def main():
    print("Welcome to the DFIR Toolkit Automation Script!")
    print("This script will install and configure commonly used DFIR tools.")

    # Prompt user for tool selection
    tools = ["Volatility", "Rekall", "Autopsy", "Wireshark", "The Sleuth Kit"]
    selected_tools = []
    for tool in tools:
        choice = input(f"Do you want to install {tool}? (y/n): ")
        if choice.lower() == "y":
            selected_tools.append(tool)

    # Install selected tools
    for tool in selected_tools:
        if tool == "Volatility":
            install_volatility()
        elif tool == "Rekall":
            install_rekall()
        elif tool == "Autopsy":
            install_autopsy()
        elif tool == "Wireshark":
            install_wireshark()
        elif tool == "The Sleuth Kit":
            install_sleuthkit()

    logging.info("DFIR Toolkit setup complete!")

if __name__ == "__main__":
    main()