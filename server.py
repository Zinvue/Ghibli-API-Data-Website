import bottle
import films
import chat
import json

@bottle.route('/ghibli.js')
def server_static():
    return bottle.static_file('ghibli.js', root='')

@bottle.route('/')
def server_static1():
    return bottle.static_file('index.html', root='')

@bottle.route('/films')
def get_films():
    url = 'https://ghibliapi.herokuapp.com/films'
    return films.rotten(url)

#chat function

@bottle.route('/')
def index():
 return bottle.static_file("index.html", root="")
 
@bottle.route('/chat.js')
def static():
 return bottle.static_file("chat.js", root="")
 
@bottle.route('/chat')
def get_chat():
 return json.dumps(chat.get_chat())
 
@bottle.post('/send')
def do_chat():
 content = bottle.request.body.read().decode()
 content = json.loads(content)
 chat.add_message(content['message'])
 return json.dumps(chat.get_chat())

bottle.run(host='0.0.0.0', port=8080, debug=True)

#all the wrong code down below but I'll keep it for nostalgia sake

#========
# do this in bottle first
#
#import films
#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route("/ghibli.js")
#def server_static():
#    return render_template('./ghibli.js')
#
##app.send_static_file
##render_template
#
#@app.route("/")
#def server_static1():
#    return render_template('./index.html')
#    
#@app.route("/films")
#def get_films():
#    url = 'https://ghibliapi.herokuapp.com/films'
#    return films.rotten(url)
#    
#if __name__ == '__main__':
#    app.run(debug = True, host='0.0.0.0', port='8080')
#    app.run(debug=True, port=8080)
#    
#=========================
#====================




# $ pip install Flask
# $ FLASK_APP=hello.py flask run
#  * Running on http://localhost:5000/

# from flask import Flask
# app = Flask(__name__)
#


#@app.route("/")
#def index():
#   return render_template("index.html")

# ========
# THE BIG TEST
#from flask import Flask, request
## set the project root directory as the static folder, you can set others.
#app = Flask(__name__, static_url_path='')
#
#@app.route('/')
#def root():
#    return app.send_static_file('index.html')
#
#@app.route('/')
#def root():
#    return app.send_static_file('index.html')

# ============================
# no no no no
# from flask import Flask, request, send_from_directory

# # set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')

# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)

# if __name__ == "__main__":
#     app.run()

# ====================================

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

#USE FLASK
