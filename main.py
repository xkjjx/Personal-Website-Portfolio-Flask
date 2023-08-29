from flask import Flask, render_template, request
from helper import *
app = Flask(__name__)

@app.route('/')
def index():
    projectList = readProjects()
    about = getAboutMe()
    return render_template('index.html', about = about,projects = projectList)

@app.route("/Projects/<path:url>")
def serveProjects(url):
    return render_template("project.html",project = readProject(url))

@app.route("/contact")
def serveContact():
    return render_template("contact.html")

@app.route("/contactSubmit",methods=["POST"])
def getContact():
    data = request.json
    with open("info.csv", 'a') as file:
        file.write(",".join([data["name"], data["email"], data["message"]]) + "\n")
    return {'message': 'Data received and processed'}



if __name__ == '__main__':
    app.run()
