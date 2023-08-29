from flask import Flask, render_template
from helper import *
app = Flask(__name__)

@app.route('/')
def index():
    projectList = readProjects()
    about = getAboutMe()
    return render_template('index2.html', about = about,projects = projectList)

if __name__ == '__main__':
    app.run()
