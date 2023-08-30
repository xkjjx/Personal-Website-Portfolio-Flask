from flask import Flask, render_template, request
from helper import *
application = Flask(__name__)

@application.route('/')
def index():
    projectList = readProjects()
    about = getAboutMe()
    return render_template('index.html', about = about,projects = projectList)

@application.route("/Projects/<path:url>")
def serveProjects(url):
    return render_template("project.html",project = readProject(url))

@application.route("/contact")
def serveContact():
    return render_template("contact.html")

@application.route("/contactSubmit",methods=["POST"])
def getContact():
    data = request.json
    with open("info.csv", 'a') as file:
        file.write(",".join([data["name"], data["email"], data["message"]]) + "\n")
    return {'message': 'Data received and processed'}



if __name__ == '__main__':
    application.run()
