# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install pipenv
COPY . /code/
RUN pip install -r requirements.txt

EXPOSE 8000
