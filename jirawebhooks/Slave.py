from jira import JIRA


class JIRASlave:
    def __init__(self, jira_connection):
        self.External_ID_Field = 'customfield_10113'
        self.Jira_instant = jira_connection
        self.Master_Key = ''
        self.Key = 'ESC'
        self.issue_dict = {}
    
    def GetIssue(self, data):
        fix_versions = []
        if data['issue']['fields']['fixVersions'] is not None:
            for version in data['issue']['fields']['fixVersions']:
                fix_versions.append({"name": version['name']})
        versions = []
        if data['issue']['fields']['versions'] is not None:
            for version in data['issue']['fields']['versions']:
                versions.append({"name": version['name']})
        components=[]
        if data['issue']['fields']['components'] is not None:
            for component in data['issue']['fields']['components']:
                components.append({"name": component['name']})
        self.issue_dict = {
            'project': {'key': self.Slave.Key},
            'summary': data['issue']['fields']['summary'],
            'issuetype': {'name': data['issue']['fields']['issuetype']['name']},
            'description': data['issue']['fields']['description'] if data['issue']['fields']['description'] is not None else "",
            'priority': {'id': data['issue']['fields']['priority']["id"]},
            'status': {'name':data['issue']['fields']['status']['name']}, #on ne peut mettre le le 1er status
            'versions': list(versions),
            'fixVersions': list(fix_versions),
            'labels': list(data['issue']['fields']['labels']) if data['issue']['fields']['labels'] is not None else [],
            'components': list(components),
            # 'comments' : 
            self.Slave.External_ID_Field: data['issue']['key']
        }
        self.assign= data['issue']['fields']['assignee'] if data['issue']['fields']['assignee'] is not None else ""
        self.creator = data['issue']['fields']['creator']
        self.reporter = data['issue']['fields']['reporter']
        print(self.reporter.name)
        print(self.creator.name)
        
        self.issue_key = data['issue']['key']


    def AckMaster(self, master):
        self.Master_Key = master.Key


