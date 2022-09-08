
import requests
import re
from http.cookies import SimpleCookie
from bs4 import BeautifulSoup


def getCSRF(html):
  #  soup = BeautifulSoup(html, 'html.parser')
    # csrf = soup.find(id="csrf").get('value')
    r = requests.get(
        "http://192.168.13.1/orangehrm/symfony/web/index.php/auth/login")
    html = r.content
    try:
        token = re.search(
            'name="_csrf_token" value="(.+?)" id="csrf_token"', str(html)).group(1)
    except AttributeError:
        pass
    return token


def cookiesToDict(cookies):
    simple_cookie = SimpleCookie(cookies)
    cookiesDict = {}
    for key, morsel in simple_cookie.items():
        cookiesDict[key] = morsel.value
    return cookiesDict


def preprocess(req):
    # Initiate response
    r = None

    # Request url
    url = req.get_full_url()

    # Get set cookie
    req_cookies = req.get_header("Cookie")
    if req_cookies:
        decoded_cookies = req_cookies.decode('ascii')
        cookiesDict = cookiesToDict(decoded_cookies)
        if "PHPSESSID" in cookiesDict:
            r = requests.get(
                url, cookies={"PHPSESSID": cookiesDict["PHPSESSID"]})
    else:
      #   Gets phpsessid from first request
        r = requests.get(url)
        phpsessid = r.cookies.get("PHPSESSID")
    # Sets req phpsessid
        req.add_header("Cookie", f"PHPSESSID={phpsessid}")

    csrf = getCSRF(r.text)

    req.full_url = f"{req.get_full_url()}&csrf={csrf}"
