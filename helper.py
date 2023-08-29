import os

def readProjects():
    projects = [x for x in os.listdir("static/ProjectInfo") if "." not in x]
    ProjectsList = []
    for project in projects:
        name = project
        skills = []
        with open("static/ProjectInfo/{}/description.txt".format(name)) as d:
            description = d.read()

        with open("static/ProjectInfo/{}/shortDescription.txt".format(name)) as d:
            shortDescription = d.readlines()[0]

        with open("static/ProjectInfo/{}/skills.txt".format(name)) as s:
            for line in s.readlines():
                skills.append(line.strip())

        with open("static/ProjectInfo/{}/github.txt".format(name)) as g:
            git = g.readlines()[0].strip()
        ProjectsList.append({"name":name,"description":description,"github":git,"shortDescription":shortDescription})
    return ProjectsList

def getAboutMe():
    with open("static/ProjectInfo/aboutMe.txt") as f:
        outP = f.read().strip()
    return outP