import os

import csv_reader

def read_exercises():
    exercises = []

    for root, dirs, files in os.walk("../content"):
        for file_name in files:
            file_exercises = csv_reader.parse_file(os.path.join(root, file_name))
            exercises = exercises + file_exercises
    return exercises