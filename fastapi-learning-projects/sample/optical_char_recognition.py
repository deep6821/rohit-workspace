import pytesseract
import asyncio


pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\rohitpandey02\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        await asyncio.sleep(2)
        return text
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)
