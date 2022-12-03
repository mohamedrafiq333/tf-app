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
       headers = {'Content-Type': 'application/json','Authorization': 'Bearer eyJraWQiOiIyMDIyMTExMjA4MjgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTk5ZWI2Yjk1LWRlYmMtNGQwYy05Yjc0LTA5OTc0MmM0MjljZSIsImlkIjoiaWFtLVNlcnZpY2VJZC05OWViNmI5NS1kZWJjLTRkMGMtOWI3NC0wOTk3NDJjNDI5Y2UiLCJyZWFsbWlkIjoiaWFtIiwianRpIjoiMzAzZWZmNzctYjk3NC00M2I3LTkxM2YtZmY0ZjJkNmVhNDFmIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC05OWViNmI5NS1kZWJjLTRkMGMtOWI3NC0wOTk3NDJjNDI5Y2UiLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIiwic3ViIjoiU2VydmljZUlkLTk5ZWI2Yjk1LWRlYmMtNGQwYy05Yjc0LTA5OTc0MmM0MjljZSIsInN1Yl90eXBlIjoiU2VydmljZUlkIiwiYXV0aG4iOnsic3ViIjoiU2VydmljZUlkLTk5ZWI2Yjk1LWRlYmMtNGQwYy05Yjc0LTA5OTc0MmM0MjljZSIsImlhbV9pZCI6ImlhbS1TZXJ2aWNlSWQtOTllYjZiOTUtZGViYy00ZDBjLTliNzQtMDk5NzQyYzQyOWNlIiwic3ViX3R5cGUiOiJTZXJ2aWNlSWQiLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIn0sImFjY291bnQiOnsiYm91bmRhcnkiOiJnbG9iYWwiLCJ2YWxpZCI6dHJ1ZSwiYnNzIjoiOTdlOWE0NzRjZTMwNGMwNmE3Y2EwMTE3Y2U2MThjZDQiLCJmcm96ZW4iOnRydWV9LCJpYXQiOjE2NzAwNjY5MzUsImV4cCI6MTY3MDA3MDUzNSwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.uwn2tVQCVYQeY4lo8B2Rqw9-lj3pmgZxKfSM76bORUUBRd7djvI6us8YEqaEbAyO_KZgmk1wEa8_cjQQpxw1B9KliLZ56uD4td54km3uwuPitXXxjgYKCy8o-K8dFDCr2FyTwEErDXAtSOVFfdVZrciUtUVBGzgjNss3mdRB6uIxNUkCHr-cBVCcK7etargiZaDfQLIYT7lFjhVcQAZHo_gePG12wPGf_iPh0abKtdK-KVZ5oWWV3-1fuPyaj8Dd-ULkGxydtYT5JlT5xAJrgcWHs6oFqEcoKLXwN3spxSmJF51S599yk5dayCY1_ius7eqEG31rIgQxZAE9RB00zA'}
       data = json.dumps({
            'specversion': '1.0',
            'time': '2018-04-05T17:31:00Z',
            'id': '9ca5e995-3cbb-4985-ba27-9f8d7f7b10e2',
            'ibmenseverity': 'HIGH',
            'source': 'api-server',
            'ibmensourceid': '7f421efa-ff79-4890-9152-deb007fbadc4:api',
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
       print("The POST response and status code is :")
       print(resp.text)
       print(resp.status_code)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))



if __name__ == '__main__':
   app.run()