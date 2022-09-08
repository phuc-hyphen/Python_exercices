from jira import JIRA
jira_connection = JIRA(
    basic_auth=('phuc', 'admin'),
    server="http://localhost:8080"
)

# issue = jira_connection.issue('PRJ1-20')
# issue.update(fields={'customfield_10112': '4444444444444444'})
issue_dict = {
    'project': {'key': 'ESC'},
    'summary':'London',
    'description':'Description',
    'issuetype': {'name':'Bogue'},
    'customfield_10113': 'MAS-45',
    'fixVersions':[{'name':'1.0'}, {'name': '1.1'}
    ],
    'versions': [{'name':'1.0'}],
    'labels':['new'],
    'components': [{'name':'base de donnée'}],
    'comments':['commnet1']
}
new_issue = jira_connection.create_issue(fields=issue_dict)

print(new_issue)
