"""
This file is used for to write all utility methods.
Author: 'Rohit Pandey' <rohitpandey5491@gmail.com>
Date created: 27/09/2022
Python version: 3.6
"""

import os
import shutil
import zipfile


def remove_directory(target_path):
    """This method is used for to delete folder if it is exists"""
    try:
        if os.path.exists(target_path):
            shutil.rmtree(target_path, ignore_errors=True)
    except FileNotFoundError:
        print(f"Path does not exists: {target_path}")


def create_directory(target_path):
    """This method is used for to create folder if it is not exists"""
    if not os.path.exists(target_path):
        os.makedirs(target_path)


def extract_zip_file(base_path, target_path, zip_filename):
    """This method is used for to extract zip file to a target folder"""
    source_dir = os.path.join(base_path, zip_filename)
    create_directory(target_path)
    with zipfile.ZipFile(source_dir, "r") as zip_ref:
        zip_ref.extractall(target_path)
