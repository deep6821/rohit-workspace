"""
This file is used for to write all constants.
Author: 'Rohit Pandey' <rohitpandey5491@gmail.com>
Date created: 27/09/2022
Python version: 3.6
"""

import os
from utils import extract_zip_file

FILE_FORMAT = "csv"
SEPARATOR = "::"

BASE_PATH = os.path.dirname(os.path.abspath("data"))
SOURCE_PATH = os.path.join(BASE_PATH, "data")
TARGET_PATH = os.path.join(BASE_PATH, "temp")
ZIP_FILE_NAME = "ml-1m.zip"
ZIP_FOLDER_NAME = "ml-1m"
extract_zip_file(SOURCE_PATH, TARGET_PATH, ZIP_FILE_NAME)
ZIP_FILE_PATH = os.path.join(TARGET_PATH, ZIP_FOLDER_NAME)

MOVIES_DAT_FILE = os.path.join(ZIP_FILE_PATH, "movies.dat")
RATINGS_DAT_FILE = os.path.join(ZIP_FILE_PATH, "ratings.dat")
USERS_DAT_FILE = os.path.join(ZIP_FILE_PATH, "users.dat")
