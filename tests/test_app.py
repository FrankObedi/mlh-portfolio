import unittest
import os


os.environ["TESTING"] = "true"

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>About Me</title>" in html
        # typo in this heading
        # assert "<h2>MLH Fellow</h2>" in html
        assert '<h2 class="card-title">Full-Stack Dev</h2>' in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code ==200 
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # test POST endpoint 
        message = "This is a test post from test_app.py"
        response = self.client.post("/api/timeline_post",data={"name":"test","email":"test@example.com","content":message})
        assert response.status_code == 200
        first_post = response.get_json()
        response = self.client.post("/api/timeline_post",data={"name":"test2","email":"test2@example.com","content":"This is a test2 post from test_app.py"})
        assert response.status_code == 200
        second_post = response.get_json()
        response = self.client.get("/api/timeline_post")
        assert response.status_code ==200 
        assert response.is_json
        json = response.get_json()
        posts = json["timeline_posts"]
        assert len(posts) == 2
        # check posts descending order 
        assert posts[0]["id"] == second_post["id"]
        assert posts[1]["id"] == first_post["id"]
        
        # test timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h2>Create a Post</h2>" in html
        assert '<button type="submit">Submit</button>' in html
        assert f"<p class='post-content'>{message}</p>"
        # delete all (Otherwise it affects the test_db testing..)
        self.client.delete("/api/timeline_post/delete_all")

    def test_malformed_timeline_post(self):
        # POST request missing name 
        response = self.client.post("/api/timeline_post", data=
                                    {"email": "john@example.com","content":"Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content 
        response = self.client.post("/api/timeline_post", data=
                                    {"name": "John Doe","email": "john@example.com","content":""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        print(html)
        assert "Invalid content" in html

        # POST request with malformed email 
        response = self.client.post("/api/timeline_post", data=
                                    {"name":"John Doe","email": "not-an-email","content":"Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
        
