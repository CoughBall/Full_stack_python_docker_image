

Container running in my website: http://www.eyalherzlich.com:666/project/

This is a simple full stack python application that is ready to be wrapped with [Docker](https://www.docker.com/) as an image and deployed as a container. It exposes one API end point in /api/posts/<post_number> and a web application in /project which consumes that API. This is my first time trying all of these technologies, nice experience overall.

## DOCKER
### The stack
* OS - Ubuntu 16.04
* Web server - nginx 1.10.3
* WSGI - gunicorn 19.7.1
* Web framework - flask 0.12.2
* Frontend frameworks - bootstrap, jquery

The Dockerfile installs the necessary programs and listens on port 80 for the web application, the container will launch using the runContainer.sh script

## The application
1. API - project/app.py

Exposing an API that consumes 2 other API's and consolidates their output from https://jsonplaceholder.typicode.com, the website is just used to test the API, it exposes posts for users and comments for those posts. This new API is consumed via /api/posts/<post_number> and returns a post for a user only if it exists for this specific user (the user id is always 1) and the comments for that specific post by consuming [posts](https://jsonplaceholder.typicode.com/posts) and [comments](https://jsonplaceholder.typicode.com/posts/1/comments) with the given post id

![](https://i.imgur.com/KLCFy0L.gif)

2. Web application: - project/static/index.html

Web application that calls the previously mentioned API with an input of the post Id

![](https://i.imgur.com/PIwgRVA.gif)

This is a simple full stack python application that is ready to be wrapped with [Docker](https://www.docker.com/) as an image and deployed as a container. It exposes one API end point in /api/posts/<post_number> and a web application in /project which consumes that API. This is my first time trying all of these technologies, nice experience overall.

## DOCKER
### The stack
* OS - Ubuntu 16.04
* Web server - nginx 1.10.3
* WSGI - gunicorn 19.7.1
* Web framework - flask 0.12.2
* Frontend frameworks - bootstrap, jquery

The Dockerfile installs the necessary programs and listens on port 80 for the web application, the container will launch using the runContainer.sh script

## The application
1. API - project/app.py

Exposing an API that consumes 2 other API's and consolidates their output from https://jsonplaceholder.typicode.com, the website is just used to test the API, it exposes posts for users and comments for those posts. This new API is consumed via /api/posts/<post_number> and returns a post for a user only if it exists for this specific user (the user id is always 1) and the comments for that specific post by consuming [posts](https://jsonplaceholder.typicode.com/posts) and [comments](https://jsonplaceholder.typicode.com/posts/1/comments) with the given post id

![](https://i.imgur.com/KLCFy0L.gif)

2. Web application: - project/static/index.html

Web application that calls the previously mentioned API with an input of the post Id

![](https://i.imgur.com/PIwgRVA.gif)
