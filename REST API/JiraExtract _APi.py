import json
import requests
import xlwt


def jira_extract(user, password):
    extract_dist = {}
    r = requests.get(
        'https://sandbox.getxray.app/rest/raven/2.0/api/test/?filter=12500', auth=(user, password))
    # print(json.dumps(r.json(), indent=4))
    for test_case in r.json():
        key = test_case.get('key')
        uri = "https://sandbox.getxray.app/rest/api/2/issue/" + \
            str(test_case.get('id'))
        r2 = requests.get(uri, auth=(user, password))
        summary = r2.json()["fields"].get('summary')
        extract_dist[key] = summary
    return extract_dist


def write_in_excel(dict, filepath):
    data = xlwt.Workbook()
    page1 = data.add_sheet("JIRA_XRAY")
    i = 1
    page1.write(0, 0, "KEY")
    page1.write(0, 1, "SUMMARY")
    for key, value in dict.items():
        page1.write(i, 0, key)
        page1.write(i, 1, value)
        i += 1
    data.save(filepath)
    
    
# response = requests.get("https://sandbox.getxray.app/issues/?filter=12500")
# print(response.content)
book_dictionary = jira_extract('user9', 'Phuc12345')
print(json.dumps(book_dictionary, indent=4))
write_in_excel(book_dictionary,"jira_extract.xls")
