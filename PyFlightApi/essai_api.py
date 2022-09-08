from jira import JIRA
jira_connection = JIRA(
    basic_auth=('phuc', 'admin'),
    server="http://localhost:8080"
)

issue = jira_connection.issue('ESC-14')
issue.update(fields={'customfield_10113': '4444444444444444'})


print(issue)
