# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and change to working dir
RUN mkdir /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy code
COPY . /code/

# EXPOSE port 7000 to allow communication to/from server
EXPOSE 8000

# Database migrations
CMD python manage.py makemigrations
CMD python manage.py migrate

# CMD specifies the command to execute to start the server running.
CMD python manage.py runserver 0.0.0.0:8000