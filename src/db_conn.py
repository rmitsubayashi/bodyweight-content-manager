import mysql.connector

import exercise

class DB:
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="28Ju3OG7L6uIajvM",
            database="schema"
        )

    def save_exercises(self, exercises):
        for exercise in exercises:
            exercise_sql = "INSERT INTO exercise (title, description, level, measurement_type, category_id, is_default) VALUES (%s, %s, %s, %s, %s, %s)"
            exercise_vals = (exercise.title, exercise.description, exercise.level, exercise.measurement_type, exercise.category_id, exercise.is_default)
            cursor = self.conn.cursor()
            cursor.execute(exercise_sql, exercise_vals)
            self.conn.commit()
            id = cursor.lastrowid
            for index, set_value in enumerate(exercise.target_sets):
                target_sets_sql = "INSERT INTO target_set (exercise_id, set_number, value) VALUES (%s, %s, %s)"
                target_sets_vals = (id, index+1, set_value)
                cursor.execute(target_sets_sql, target_sets_vals)
            self.conn.commit()


            