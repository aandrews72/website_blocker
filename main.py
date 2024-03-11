import os
import time

# Function to check/write a backup or etc/hosts
def backup():
    backup = "/etc/hosts.backup"
    if os.path.exists(backup):
        print("A backup file already exists, please check and remove it")
        return
    os.system(f"cp /etc/hosts {backup}") 


# Function to block websites, taking time as an arg, and continously checking that time 



# Function to unblock websites



