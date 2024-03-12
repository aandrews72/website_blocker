import os
import time

local = "127.0.0.1"

# Function to check/write a backup or etc/hosts
def backup():
    backup = "/etc/hosts.backup"
    if os.path.exists(backup):
        print("A backup file already exists, please check and remove it")
        return False
    # backup the host file
    os.system(f"cp /etc/hosts {backup}") 
    return True

# Function to unblock websites
def unblock():
    backup = "/etc/hosts.backup"
    os.system(f"cp {backup} /etc/hosts")
    os.remove(backup)
    print("Websites unblocked")

def block(duration):
    backup()
    # Read the websites from the file
    with open("blocked_websites.txt", "r") as f:
        blocked_websites = [line.strip() for line in f.readlines()]


    # Block websites by writing contents of blocked_websites.txt to etc/hosts
    with open("/etc/hosts", "a") as f:
        for website in blocked_websites:
            f.write(f"{local} {website}\n")


    # Calculate the unblock time and print it 
    unblock_time = time.time() + duration * 60
    # print unblock time with time 
    
    # While loop to check if we've passed the unblock time, if not sleep for 5 seconds
    while time.time() < unblock_time:
        time.sleep(5)


    # Once out of while loop, call the unblock function
    unblock()
    
block(1)




