import colorama
import pystyle
import threading
import socket
import sys
import requests
import subprocess
import scapy
from scapy.all import IP, ICMP, sr1
import ctypes
import datetime
import platform
import random
import socket
import time
import getpass
from time import sleep
from threading import Thread
import requests
import pyfiglet


from pystyle import *
from colorama import Fore, Back, Style
colorama.init()

def main():
    subprocess.run('cls', shell=True)
    if platform.system() == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"Webby - Discord Webhook Controller")

    print(datetime.datetime.now())
    print(pyfiglet.figlet_format("WEBBY"))
    print("Discord Webhook Controller")
    print("===================================")

    webhook_url = input(">> Webhook URL: ").strip()

    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            print(Fore.GREEN + "Webhook verified." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Failed to verify webhook. Status code: {response.status_code}" + Style.RESET_ALL)
            return
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error verifying webhook: {e}" + Style.RESET_ALL)
        return

    while True:
        message = input(">> Message to send: ").strip()

        payload = {
            "content": message
        }

        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204 or response.status_code == 200:
                print(Fore.GREEN + f"Sent \"{message}\" successfully." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Failed to send message. Status code: {response.status_code}" + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error sending message: {e}" + Style.RESET_ALL)

        print("\n>> 1. Different Webhook")
        print(">> 2. Send Another Message")
        choice = input(">> Select an option: ").strip()

        if choice == "1":
            webhook_url = input(">> Webhook URL: ").strip()
            try:
                response = requests.get(webhook_url)
                if response.status_code == 200:
                    print(Fore.GREEN + "Webhook verified." + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Failed to verify webhook. Status code: {response.status_code}" + Style.RESET_ALL)
                    return
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Error verifying webhook: {e}" + Style.RESET_ALL)
                return
        elif choice != "2":
            print("Invalid option. Exiting.")
            break

if __name__ == "__main__":
    main()