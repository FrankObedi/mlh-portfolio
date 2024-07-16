import os, datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict


load_dotenv()
app = Flask(__name__)
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(os.getenv('MYSQL_DATABASE'),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


# Website content
work_experiences = [
    {
        "position": "Web Dev Intern",
        "company": "NYA",
        "date": "Jul 2023 - Sep 2023",
        'image_url': "./static/img/nya.svg",
        "detail": ["Contributed to the successful launch of a website rebrand by implementing design concepts, resulting in improved aesthetics and user experience.",
                "Optimized website performance by minimizing page load times, resulting in an improved user experience and increase in user engagement."]
    },
    {
        "position": "Frontend Developer Intern",
        "company": "DCTI",
        "date": "Jun 2020 - Aug 2020",
        'image_url': "./static/img/dcti.png",
        "detail": ["Collaborated in a team of three to develop, test, and deploy an online art gallery website, enabling high school students to showcase their artworks online during the pandemic.",
                "Utilized HTML, CSS3, and JavaScript web technologies to build the user interface.",
                "Enhanced user experience by implementing search, filter, and pagination features, facilitating easier artwork discovery on the website."]
        
    }
         
]

hobbies = [
    {
        "title": "Canoeing",
        "description": "Canoeing on the lake is one of my favorite ways to relax.",
        "img_url": "./static/img/canoeing.jpg",
        "img_alt_text":"Canoeing"
    },
    {
        "title": "Hiking",
        "description": "Being outdoors, going on hikes and exploring nature is just a part of my identity.",
        "img_url": "./static/img/hiking.jpg",
        "img_alt_text":"Hiking"
    },
    {
        "title": "Soccer",
        "description": "I love playing soccer. It's the greatest sport in the world!",
        "img_url": "./static/img/greatest-sport.jpg",
        "img_alt_text":"Soccer ball on field"
    },
    {
        "title": "Gym",
        "description": "Exercise offers many benefits that can improve nearly every aspect of your health.",
        "img_url": "./static/img/gym.jpg",
        "img_alt_text":"Gym center"
    }    
]

education = [
    {
        "institution": "Wilfrid Laurier University",
        "program": "Computer Science",
        "date": "Sep 2020 - Apr 2025"
    },
]


@app.route("/")
def index():
    return render_template("index.html", title = "About Me", url=os.getenv("URL"))

@app.route("/hobbies")
def hobby_page():
    return render_template("hobbies.html", title = "My Hobbies", hobbies=hobbies, url=os.getenv("URL"))

@app.route("/experience")
def experience_page():
    return render_template("experience.html", title = "Experience", work_experiences=work_experiences, url=os.getenv("URL"))

@app.route("/travel-map")
def map():
    return render_template("map.html", title = "My Travel Map", url=os.getenv("URL"))

@app.route("/timeline")
def timeline():
    return render_template('timeline.html', title='Timeline')


# POST route to add a timeline post
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

# GET rout to retrieve all timeline posts ordered by created_at descending
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

# DELETE rout to delete a timeline posts by id
@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    id = request.form['id']
    try:
        timeline_post = TimelinePost.get(TimelinePost.id==id)        
        deleted_post = model_to_dict(timeline_post)       
        timeline_post.delete_instance()
        return deleted_post
    
    except DoesNotExist:
        print("No matching record found.")
        return {
            "Error": "Failed to delete post. Post not found"
        }

@app.route('/api/timeline_post/delete_all', methods=['DELETE'])
def delete_all_time_line_post():
    query = TimelinePost.delete()
    query.execute()
    return{
        "message":"deleted all records"
    }


