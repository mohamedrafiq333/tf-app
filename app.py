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
       headers = {'Content-Type': 'application/json','Authorization': 'Bearer $TOKEN'}
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