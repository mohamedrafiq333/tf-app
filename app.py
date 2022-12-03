from datetime import datetime
import requests
import json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       url = 'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/dea67c39-5b87-4c5e-aae1-131976c218cf/notifications'
       headers = {'Content-Type': 'application/json','Authorization': 'Bearer eyJraWQiOiIyMDIyMTExMjA4MjgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTk5ZWI2Yjk1LWRlYmMtNGQwYy05Yjc0LTA5OTc0MmM0MjljZSIsImlkIjoiaWFtLVNlcnZpY2VJZC05OWViNmI5NS1kZWJjLTRkMGMtOWI3NC0wOTk3NDJjNDI5Y2UiLCJyZWFsbWlkIjoiaWFtIiwianRpIjoiZDQ0N2M3ZjUtZWJmZC00Y2E2LThmNTQtMGFkZmFkNjE5MWViIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC05OWViNmI5NS1kZWJjLTRkMGMtOWI3NC0wOTk3NDJjNDI5Y2UiLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIiwic3ViIjoiU2VydmljZUlkLTk5ZWI2Yjk1LWRlYmMtNGQwYy05Yjc0LTA5OTc0MmM0MjljZSIsInN1Yl90eXBlIjoiU2VydmljZUlkIiwiYXV0aG4iOnsic3ViIjoiU2VydmljZUlkLTk5ZWI2Yjk1LWRlYmMtNGQwYy05Yjc0LTA5OTc0MmM0MjljZSIsImlhbV9pZCI6ImlhbS1TZXJ2aWNlSWQtOTllYjZiOTUtZGViYy00ZDBjLTliNzQtMDk5NzQyYzQyOWNlIiwic3ViX3R5cGUiOiJTZXJ2aWNlSWQiLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIn0sImFjY291bnQiOnsiYm91bmRhcnkiOiJnbG9iYWwiLCJ2YWxpZCI6dHJ1ZSwiYnNzIjoiOTdlOWE0NzRjZTMwNGMwNmE3Y2EwMTE3Y2U2MThjZDQiLCJmcm96ZW4iOnRydWV9LCJpYXQiOjE2NzAwNjYzMDIsImV4cCI6MTY3MDA2OTkwMiwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.Eocgpsfdk1S6ODvXDNNP9duizxU0-kuwDoj-9etek3Z1_sz4zeQcyQdxjFqUFx0kTxPU9Qd3rEhM-ISuhfrRKhegzPeFzniBU0L6aWptz-z9z6irshRTIxTPwH32QQ5uGu666RkmpUI9Xd5m1ilOHSu4U69-cMTjRWA3KVmwjjvBaqKxDigY5hVf5LMFAJIK6-JBz9YbuzBSgdF6FHqaX1tI_BaiZcQ_bJlyz-tC97puN97rlQFmed6ZfWbcSolSLxxEtpRWApQT_dUQQXj3-UWFwOgn7H4yR3OgOmw4BH0EOiSW3i-UxxPBrcnxJDhr9RL2R0yCaHmZPN7pA8B-wg'}
       data = json.dumps({
            'specversion': '1.0',
            'time': '2018-04-05T17:31:00Z',
            'id': '9ca5e995-3cbb-4985-ba27-9f8d7f7b10e2',
            'ibmenseverity': 'HIGH',
            'source': 'api-server',
            'ibmensourceid': '023d4528-1e9f-40c8-a463-b9a5acd69c2d:api',
            'type': '*',
            'data': {
                'createTimestamp': 1557282940339,
                'shortDescription': 'Test notification bro'
            },
            'ibmendefaultshort': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
            'ibmendefaultlong': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
            'datacontenttype': 'application/json'
       })
       resp = requests.request("POST",url,headers=headers,data=data)
       print("The POST status code is :")
       print(resp.status_code)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))



if __name__ == '__main__':
   app.run()