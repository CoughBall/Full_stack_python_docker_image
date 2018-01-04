from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/api/posts/<post_id>', methods = ['GET'])
def api_get_posts_comments(post_id):
    
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    jsonPosts = posts.json()
    postsDictionary = dict()
    commentsDictionary = dict()

    isUserFound = False
    isPostFound = False

    for post in jsonPosts:
        for key, value in post.items():
            if(key == 'userId' and value == 1):
                isUserFound = True
            if(key == 'id' and value == int(post_id)):
                isPostFound = True
        if (isUserFound == True and isPostFound == True):
            postsDictionary = post
            break
        isUserFound = False
        isPostFound = False

    if not isUserFound and not isPostFound: return jsonify({})

    commentsApi = 'https://jsonplaceholder.typicode.com/posts/'+post_id+'/comments'
    comments = requests.get(commentsApi)
    jsonComments = comments.json()
    commentsDictionary = jsonComments

    for comment in commentsDictionary:
        del comment['postId']

    return jsonify({'post':postsDictionary,'comments':commentsDictionary})

if __name__ == '__main__':
    app.run()
	
