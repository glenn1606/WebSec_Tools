import requests
from check_auth_create_session import BasicAuthentication
from termcolor import colored
from bs4 import BeautifulSoup as BS
from bs4 import Comment

class SavageWebScanner():
    def __init__(self, target=None):
        if target:
            self.target = target
        else:
            self.target = input("enter target: ")
            
    def scanForComments(self):
        print(colored("[i] ", "blue") + "checking for basic auth")
        basic_auth = BasicAuthentication()
        if basic_auth.check_basic_auth(self.target):
            print("Uses basic Auth")
            user = input("input user name: ")
            password = input("input password: ")
            s = basic_auth.create_auth_session(user, password)
        else:
            s = requests.Session()
            
        response = s.get(self.target)
        soup = BS(response.text, "html.parser")
        # html.parser la bo doc dich html, reponse.text la toan bo ma nguon html, soup la 1 cay DOMdocument object model
        comments = [text for text in soup.find_all(string=True) if isinstance(text, Comment)]
        # soup.find_all(string=True) la boc tach toan bo text trong cay DOM cua soup, bo qua tat ca cac tag html chi tim text va comments va cho vao 1 list de duyet
        # cac binh luan trong html duoc phan loai la kieu Comment cua thu vien bs4
        for comment in comments:
            print(colored("[$] ", "green") + "found comment: ")
            print(f"\t{comment}")
            
    def checkForRobots(self):
        print(colored("[i] ", "blue") + "checking for basic auth")
        basic_auth = BasicAuthentication()
        if basic_auth.check_basic_auth(self.target):
            print("Uses basic Auth")
            user = input("input user name: ")
            password = input("input password: ")
            s = basic_auth.create_auth_session(user, password)
        else:
            s = requests.Session()
            
        if self.target.endswith("/"):
            response = s.get(self.target + "robots.txt")
        else:
            response = s.get(self.target + "/robots.txt")
            
        if response.ok:
            print(colored("[$] ", "green") + "found robots.txt with entries: ")
            print(response.text)
        else:
            print(colored("[-] ", "red") + "did not find robots.txt")
   
def main():
    web_scanner = SavageWebScanner()
    web_scanner.checkForComments()
    web_scanner.checkForRobots()

if __name__ == "__main__":
    main()