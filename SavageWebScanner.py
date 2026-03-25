import requests
from BasicAuthentication import BasicAuthentication
from termcolor import colored
from bs4 import BeautifulSoup as BS
from bs4 import Comment

class SavageWebScanner:
    def __init__(self, target=None):
        if target:
            self.target = target
        else:
            self.target = input("Enter the URL to scan: ")
    def scanForComments(self):
        print(colored("[i] ","blue")+ "Checking for comments...")
        basic_auth = BasicAuthentication()
        if basic_auth.check_basic_auth(self.target):
            print("User Basic Auth")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            s = basic_auth.createAuthSession(username, password)
        else:
            s = requests.Session()
        response = s.get(self.target)
        soup = BS(response.text, "html.parser")
        comments = [text for text in soup.findAll(string=True) if isinstance(text, Comment)]
        for comment in comments:
            print(comment)
    def checkForRobots(self):
        print(colored("[i] ","blue")+ "Checking for robots...")
        basic_auth = BasicAuthentication()
        if basic_auth.check_basic_auth(self.target):
            print("User Basic Auth")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            s = basic_auth.createAuthSession(username, password)
        else :
            s = requests.Session()
        if self.target.endswith("/"):
            response = s.get(self.target + "robots.txt")
        else :
            response = s.get(self.target + "/robots.txt")
        if response.ok :
            print("User Robots")
            print(response.text)
        else :
            print("User Not Found")

def main():
    web_scanner = SavageWebScanner()
    web_scanner.scanForComments()
    web_scanner.checkForRobots()
if __name__ == "__main__":
    main()
