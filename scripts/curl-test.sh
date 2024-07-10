#!/bin/bash
curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=Frank&email=frankobedi6@gmail.com&content=Test the API endpoints using curl and bash script'
curl http://127.0.0.1:5000/api/timeline_post
curl --request DELETE http://127.0.0.1:5000/api/timeline_post/delete_all