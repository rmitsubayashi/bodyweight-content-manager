import csv

import exercise

def parse_file(file_name):
    exercises = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip header
        next(csv_reader)
        for row in csv_reader:
            e = exercise.Exercise(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            exercises.append(e)

    return exercises