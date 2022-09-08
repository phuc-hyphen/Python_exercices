import requests
import re

r = requests.get("https://opensource-demo.orangehrmlive.com/")
html = r.content
try:
    token = re.search('name="_csrf_token" value="(.+?)" id="csrf_token"',str(html)).group(1)
except AttributeError: 
    pass
