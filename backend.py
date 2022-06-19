from flask import Flask ,request
app = Flask(__name__)

@app.route('/')

def index():

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    iphone_safari = open('index-mobile.html').read()
    google_chrome_android = open('index-mobile.html').read()
    PC = open('index.html').read()
    
    
    if "iphone" in user_agent:
     return (iphone_safari)
    elif "android" in user_agent:
        return (google_chrome_android)
    else:
        return (PC)

if __name__ == '__main__':
  app.run(host='0.0.0.0')

