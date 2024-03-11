import os
import time

local = "127.0.0.1"

# Function to check/write a backup or etc/hosts
def backup():
    backup = "/etc/hosts.backup"
    if os.path.exists(backup):
        print("A backup file already exists, please check and remove it")
        return
    # backup the host file
    os.system(f"cp /etc/hosts {backup}") 
    return

# Function to unblock websites
def unblock():
    os.system(f"cp {backup} /etc/hosts")
    print("Websites unblocked")

def block(time):
    backup()
    # Read the websites from the file
    with open("blocked_websites.txt", "r") as f:
        blocked_websites = [line.strip() for line in f.readlines()]


    # Block websites by writing contents of blocked_websites.txt to etc/hosts


    # Calculate the unblock time and print it 

    
    # While loop to check if we've passed the unblock time 


    # Once out of while loop, call the unblock function

    




