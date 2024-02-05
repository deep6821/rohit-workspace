import asyncio
import time
from fastapi import BackgroundTasks, FastAPI
from typing import Optional
from models import Course
from utils import write_notification, func1, func2

app = FastAPI()

course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]


# # http://localhost:8000/
# @app.get("/")
# def root():
#   return {"message": "Hello World"}

@app.get("/")
async def home():
    tasks = []
    start = time.time()
    for i in range(2):
        tasks.append(asyncio.create_task(func1()))
        tasks.append(asyncio.create_task(func2()))
    response = await asyncio.gather(*tasks)
    end = time.time()
    return {"response": response, "time_taken": (end - start)}

# http://localhost:8000/courses/apitesting
@app.get("/courses/{course_name}")
def read_course(course_name):
    return {"course_name": course_name}

# http://localhost:8000/courses/3 
@app.get("/courses/{course_id}")
def read_course(course_id: int):
    return {"course_id": course_id}

# http://localhost:8000/courses/?start=0&end=10 
@app.get("/courses/")
def read_courses(start: int, end: int):
    return course_items[start : start + end]

# http://localhost:8000/courses/
@app.get("/courses/")
def read_courses(start: int = 0, end: int = 10):
    return course_items[start : start + end]

# http://localhost:8000/courses/1?q=Hello
@app.get("/courses/{course_id}")
def read_courses(course_id: int, q: Optional[str] = None):
    if q is not None:
        return {"course_name": course_items[course_id], "q": q} 
    return {"course_name": course_items[course_id]}

@app.post("/courses/")
def create_course(course: Course):
    return course

@app.post("/send-notification/{email}")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


# To start the server, you need to run the following command ==> uvicorn main:app --reload