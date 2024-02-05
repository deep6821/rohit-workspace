#!/bin/bash

export PROJECT_PATH=$(pwd)
export kafka=$(cat /Users/rohitpandey/workspace/django_project/projects/local-settings/local_kafka.yml)
export rdbms=$(cat /Users/rohitpandey/workspace/django_project/projects/local-settings/local_mysql.yml)

# Create network for docker containers as needed
network=$(docker network list | grep test-bridge)
if [ -z "$network" ]
then
    docker network create --driver bridge --subnet=172.18.0.0/16 test-bridge
fi

# Start kafka container
kafka_running=$(docker ps -a | grep kafka-test)
if [ -n "$kafka_running" ]
then
  docker rm --force kafka-test
fi
 docker run --network=test-bridge --ip 172.18.0.2 --name kafka-test -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=127.0.0.1 --env ADVERTISED_PORT=9092 -d spotify/kafka

# Start MySQL container
mysql_running=$(docker ps -a | grep mysql-test)
if [ -z "$mysql_running" ]
then
  docker run --network=test-bridge --ip 172.18.0.3 --name mysql-test -p 3306:3306 --env MYSQL_ROOT_PASSWORD=password --env MYSQL_USER=username --env MYSQL_PASSWORD=password -d mysql:5.7.19
  sleep 10
  docker exec -it mysql-test mysql -ppassword -e "create database rohit;"
fi


# Run Django App
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
