import colorama
import requests
import subprocess
import ctypes
import platform
import requests
import pyfiglet

from colorama import Fore, Back, Style
colorama.init()

def main():
    subprocess.run('cls', shell=True)
    if platform.system() == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW("Webby - Discord Webhook Controller {Cleaned Edition by Venom}")

    print(pyfiglet.figlet_format("WEBBY"))
    print("Discord Webhook Controller || Webby clean edition, modified & packaged by venom")
    print("="*120)

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
        input()
        main()

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
        webhookconfig()
def webhookconfig():
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
                input()
                main()
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error verifying webhook: {e}" + Style.RESET_ALL)
            input()
            main()
    elif choice != "2":
        print(Fore.RED + "Invalid option.")
        print(Fore.WHITE)
        webhookconfig()
            

if __name__ == "__main__":
    main()