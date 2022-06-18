import json
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

def jira_extract():
    extract_list = []
    r = requests.get('https://sandbox.getxray.app/issues/?filter=12500', auth=('user9', 'Phuc12345'))
    soup = BeautifulSoup(r.content, features="html.parser")
    issues_links = soup.findAll('a', class_="issue-link")
    for issues_link in issues_links:
        text = issues_link.getText()
        if text != '' and text != '\n\n':
            extract_list.append(text)
    extract_dict = {}
    for i in range(0, len(extract_list)):
        if i % 2 == 0 and i + 1 <= len(extract_list):
            extract_dict[str(extract_list[i])] = extract_list[i + 1]
    # print(list)
    return extract_dict


# response = requests.get("https://sandbox.getxray.app/issues/?filter=12500")
# print(response.content)
book_dictionary = jira_extract()
print(json.dumps(book_dictionary, indent=4))

# print(soup)
