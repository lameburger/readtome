import json
from flask import Flask, render_template, request
from main import *

global mode


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('language.html')

@app.route('/mode')
def mode():
    return render_template('mode.html')

@app.route('/speak', methods=['POST'])
def speak():
    global lang
    output = request.get_json()
    if output == "English":
        text_to_speech("English", "English", 100, 1)
        lang = "English"
    elif output == "German":
        text_to_speech("Deutsch", "German", 100, 1)
        lang = "German"
    elif output == "Spanish":
        text_to_speech("Español", "Spanish", 100, 1)
        lang = "Spanish"
    elif output == "French":
        text_to_speech("Français", "French", 100, 1)
        lang = "French"

@app.route('/selection', methods=['POST'])
def selection(): 
    global mode
    output = request.get_json()
    if output == "Food Menu":
        mode = "Food Menu"
    elif output == "Currency":
        mode = "Currency"
    elif output == "Read":
        mode = "Read"
    else:
        mode = "settings"
    
@app.route('/cam')
def camera():
    return render_template('cam.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/read', methods=['POST'])
def read():
    output = request.get_json()
    print(type(output))
    result = json.loads(output)
    print(result)
    print(type(result))
    # js2py.run_file('static/scripts/python.js')
    return scan(result)


if __name__ == '__main__':
    app.run(debug=True)  