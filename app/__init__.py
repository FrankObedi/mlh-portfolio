import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

work_experiences = [
    {
        "position": "Frontend Developer",
        "company": "Ori.Gatou Creative Solution Inc. - Apprenticeship",
        "date": "2023 Jul - 2023 Sep",
        "detail": ["Created reactive data analytics dashboard with Svelte and D3.js.",
                "Integrated a backend API to fetch data with the front end."]
    },
    {
        "position": "React Teaching Assistant",
        "company": "ComIT",
        "date": "2023 Sep - 2023 Dec",
        "detail": ["Provide additional assistance to students in troubleshooting, understanding course materials, and completing assignments through chat and video calls.",
                "Maintain attendance records and communicate with the instructor and program coordinators to address student absences and issues related to class participation."]
    },
    {
        "position": "Web Dev Intern",
        "company": "North York Arts",
        "date": "2023 Jul - 2023 Sep",
        "detail": ["Contributed to the successful launch of a website rebrand by implementing design concepts, resulting in improved aesthetics and user experience.",
                "Optimized website performance by minimizing page load times, resulting in an improved user experience and increase in user engagement."]
    }     
]

hobbies = [
    {
        "description": "Making Music with Guitar and Piano",
        "img_path": "./static/img/piano-man.jpg",
        "img_alt_text":"Playing the public piano"
    },
    {
        "description": "Soccer is the greatest sport in the world!",
        "img_path": "./static/img/greatest-sport.jpg",
        "img_alt_text":"Soccer ball on field"
    },
    {
        "description": "Shogi - Japanese Chess",
        "img_path": "./static/img/shogi-game.jpg",
        "img_alt_text":"Shogi board game"
    }
]

education = [
    {
        "institution": "ComIT",
        "program": "Node Js Course",
        "date": "2023 Jun - 2023 Sep"
    },
    {
        "institution": "Osaka University",
        "program": "Economics, Economics and Management",
        "date": "2010 Apr - 2014 Mar"
    },
    {
        "institution": "Wilfrid Laurier University",
        "program": "Computer Science",
        "date": "2020 Sep - 2025 Apr"
    },
]

@app.route('/')
def index():
    
    return render_template('index.html', title="MLH Fellow", work_experiences=work_experiences, hobbies=hobbies, education = education, url=os.getenv("URL"))

