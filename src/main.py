import reader
import db_conn

exercises = reader.read_exercises()
database = db_conn.DB()
database.save_exercises(exercises)