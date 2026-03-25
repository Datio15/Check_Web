import requests

class BasicAuthentication():
    def check_basic_auth(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 401:
                basic_auth = reponse.headers['WWW-Authorization']
                if "Basic" in basic_auth:
                    return True
                else:
                    return False

        except :
            print(f"Error connecting to {url}")
    def createAuthSession(self, username, password):
        s = requests.Session()
        s.auth = (username, password)
        return s
def main():
    url = input("Enter the URL: ")
    basic_auth = BasicAuthentication()
    if basic_auth.check_basic_auth(url):
        print("User Basic Auth")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        s = basic_auth.createAuthSession(username, password)
        response = s.get(url)
        if response.ok:
            print("Authentication Successful")
        else:
            print("Authentication Failed")

    else:
        print("Does use Basic Auth")

if __name__ == "__main__":
    main()
