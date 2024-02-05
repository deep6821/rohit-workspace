import time
from fastapi import FastAPI, File, UploadFile
from typing import List

from ocr import read_image
from utils import save_file_to_server


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    for img in Images:
        print("Images Uploaded: ", img.filename)
        temp_file = save_file_to_server(img, path="./", save_as=img.filename)
        text = await read_image(temp_file)
        response[img.filename] = text
    response["Time Taken"] = round((time.time() - s),2)

    return response