# Base image
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER Dopefish

# Nginx #
# Download and Install Nginx
RUN apt-get update
RUN apt-get install -y nginx  

# Delete nginx default configuration
RUN rm -v /etc/nginx/sites-available/default

# Create new nginx configuration
COPY default /etc/nginx/sites-available/

# Expose ports
EXPOSE 80

# Install Python and Basic Python Tools
RUN apt-get install -y python3 python-dev python-distribute python3-pip

# Copy the application folder inside the container
COPY /project/ /full-stack-python-docker-image/project/

# Get pip to download and install requirements:
RUN pip3 install -r /full-stack-python-docker-image/project/requirements.txt virtualenv

# Set the default command to execute
COPY runContainer.sh /bin/
ENTRYPOINT runContainer.sh
