import asyncio
import os
import shutil


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

async def func1():
    await asyncio.sleep(2)
    return "Func1() Completed"

async def func2():
    await asyncio.sleep(1)
    return "Func2() Completed"

def save_file_to_server(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    print("===>>", temp_file)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file
