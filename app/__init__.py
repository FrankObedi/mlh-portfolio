import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

work_experiences = [
    {
        "position": "Web Dev Intern",
        "company": "North York Arts",
        "date": "Jul 2023 - Sep 2023",
        "detail": ["Contributed to the successful launch of a website rebrand by implementing design concepts, resulting in improved aesthetics and user experience.",
                "Optimized website performance by minimizing page load times, resulting in an improved user experience and increase in user engagement."]
    },
    {
        "position": "Frontend Developer Intern",
        "company": "Danforth Collegiate and Technical Institute.",
        "date": "Jun 2020 - Aug 2020",
        "detail": ["Collaborated in a team of three to develop, test, and deploy an online art gallery website, enabling high school students to showcase their artworks online during the pandemic.",
                "Utilized HTML, CSS3, and JavaScript web technologies to build the user interface.",
                "Enhanced user experience by implementing search, filter, and pagination features, facilitating easier artwork discovery on the website."]
    }
         
]

hobbies = [
    {
        "description": "Exercise offers many benefits that can improve nearly every aspect of your health.",
        "img_path": "./static/img/gym.jpg",
        "img_alt_text":"Going to the Gym"
    },
    {
        "description": "I love playing soccer. It's the greatest sport in the world!",
        "img_path": "./static/img/greatest-sport.jpg",
        "img_alt_text":"Soccer ball on field"
    },
    {
        "description": "Canoeing on the lake is one of my favorite ways to relax.",
        "img_path": "./static/img/canoeing.jpg",
        "img_alt_text":"Shogi board game"
    },
    {
        "description": "Being outdoors, going on hikes and exploring nature is just a part of my identity.",
        "img_path": "./static/img/hiking.jpg",
        "img_alt_text":"Shogi board game"
    }
]

education = [
    {
        "institution": "Wilfrid Laurier University",
        "program": "Computer Science",
        "date": "Sep 2020 - Apr 2025"
    },
]

@app.route('/')
def index():    
    return render_template('index.html', title="MLH Fellow", work_experiences=work_experiences, hobbies=hobbies, education = education, url=os.getenv("URL"))

@app.route("/hobbies")
def hobby_page():
    return render_template("hobbies.html", title = "My Hobbies", hobbies=hobbies, url=os.getenv("URL"))

