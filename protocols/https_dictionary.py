import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def https(url, user, pswd):
    if 'https://' not in url:
        url = 'https://' + url
    
    payload = {
        "username" : user,
        "password" : pswd
    }
    r = requests.post(url=url, verify=False, headers=payload)
    if r.status_code == 200:
        print("Password is " + pswd)
    else:
        pass