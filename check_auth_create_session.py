import requests

class BasicAuthentication():
    def check_basic_auth(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 401:
                # Sửa lỗi chính tả 'reponse' thành 'response' từ ảnh gốc
                basic_auth = response.headers.get("WWW-Authenticate", "")
                if "Basic" in basic_auth:
                    return True
                else:
                    return False
            else:
                return False
        except:
            print(f"Can't connect to {url} please try again")
            return False

    def create_auth_session(self, self_user, password):
        s = requests.Session()
        s.auth = (self_user, password)
        return s

def main():
    basic_auth = BasicAuthentication()
    url = input("input your url: ")
    
    if basic_auth.check_basic_auth(url):
        print("Uses basic Auth")
        user = input("input user name: ")
        password = input("input password: ")
        s = basic_auth.create_auth_session(user, password)
        response = s.get(url)
        
        if response.ok:
            print("authenticated")
        else:
            print("failed to auth")
    else:
        print("Does not use basicAuth")

if __name__ == "__main__":
    main()