from datetime import datetime
import requests
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

url = "https://eu-gb.event-notifications.cloud.ibm.com/event-notifications/v1/instances/0eb42def-21aa-4f0a-a975-0812ead6ceee/notifications"
headers["Authorization"] = "Bearer eyJraWQiOiIyMDIyMTExMjA4MjgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLWEwOTlhMTVlLTY2MTMtNGU3YS05ZmNhLWUxZGU0NzkxYzcyNyIsImlkIjoiaWFtLVNlcnZpY2VJZC1hMDk5YTE1ZS02NjEzLTRlN2EtOWZjYS1lMWRlNDc5MWM3MjciLCJyZWFsbWlkIjoiaWFtIiwianRpIjoiZmIxY2E0ODEtYjM2My00NjdjLWE3MjItYzY1NmI4NzgxY2ZmIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC1hMDk5YTE1ZS02NjEzLTRlN2EtOWZjYS1lMWRlNDc5MWM3MjciLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIiwic3ViIjoiU2VydmljZUlkLWEwOTlhMTVlLTY2MTMtNGU3YS05ZmNhLWUxZGU0NzkxYzcyNyIsInN1Yl90eXBlIjoiU2VydmljZUlkIiwiYXV0aG4iOnsic3ViIjoiU2VydmljZUlkLWEwOTlhMTVlLTY2MTMtNGU3YS05ZmNhLWUxZGU0NzkxYzcyNyIsImlhbV9pZCI6ImlhbS1TZXJ2aWNlSWQtYTA5OWExNWUtNjYxMy00ZTdhLTlmY2EtZTFkZTQ3OTFjNzI3Iiwic3ViX3R5cGUiOiJTZXJ2aWNlSWQiLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIn0sImFjY291bnQiOnsiYm91bmRhcnkiOiJnbG9iYWwiLCJ2YWxpZCI6dHJ1ZSwiYnNzIjoiNGY2MzFlYTNiMzIwNGIyYjg3OGEyOTU2MDQ5OTRhY2YiLCJmcm96ZW4iOnRydWV9LCJpYXQiOjE2Njk5ODU0OTEsImV4cCI6MTY2OTk4OTA5MSwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.HywGmbdSSPVQ6vGfN2zL3boDkkxXDp6UD4hgXcw69TLDt-RmJZsGGF0dtBureLSi5DDu1DguZ20aFtrkxkP87zyIZZaFVOW-f9euxEn5spiG6QW2ZWZv3f-xPtop4i9QWeX_vrqLpwZjkMQcB7Y7cvsXB94TXM8r2w_f9aZ-t8S34xGF7wqz2Obb1TjUWQIEJecJ4j1Ln_rnBxfGSJMzY-ojOokJ6Oy47zwwrEtmULWSKP4sF4Lm0vJcEG0IaqLMSKNKHBG1Hl8tAQbwiJFwQ5TPlPd3cTF4u3qoFpCNzI7_P0oLFWp0WMT49be5axR9-zMZmS6mOjXt8AmqRz5nbQ"
resp = requests.get(url, headers=headers)

print(resp.status_code)

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
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))



if __name__ == '__main__':
   app.run()