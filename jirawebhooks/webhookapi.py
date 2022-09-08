# encoding: utf8
import json
import flask
from flask import request, jsonify, Response, make_response
from jira import JIRA
from Slave import JIRASlave
from Master import JIRAMaster
import logging.config


app = flask.Flask(__name__)
jira_connection = JIRA(
    basic_auth=('phuc', 'admin'),
    server="http://localhost:8080"
)

slave = JIRASlave(jira_connection)
master = JIRAMaster(jira_connection,slave)
slave.AckMaster(master)


logging.config.fileConfig('logging.conf')
print("Jira Webhook Rest Api")
print("Listening on http://localhost:5000")


@app.route('/', methods=['GET'])
def home():
    return '''<h1>FlightsApp Rest Api</h1>
<p>Listening on http://localhost:5000</p>
</p>
'''

@app.route('/webhook_api/v1/Master', methods=['POST'])
def MasterEvents():
    print("Master")
    if (request.is_json):
        data = request.get_json()
        master.GetIssue(data)
        if data['issue_event_type_name'] == 'issue_created':
            print("Issue created event")
            master.IssueCreatedEvent()
        if data['issue_event_type_name'] == 'issue_updated':
            print("Issue updates event")
            # master.IssueCreatedEvent()

    response = make_response("Defect created", 201,)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/webhook_api/v1/Slave', methods=['POST'])
def SlaveEvents():
    print("slave:")
    if (request.is_json):
        data = request.get_json()
        # print(json.dumps(data))
        master.GetIssue(data)
        if data['issue_event_type_name'] == 'issue_created':
            print("Issue created event")
            master.IssueCreatedEvent()

    response = make_response("Defect created", 201,)
    response.headers["Content-Type"] = "application/json"
    return response
app.run()
