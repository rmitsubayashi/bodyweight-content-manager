import unittest
import exercise

class ExerciseTest(unittest.TestCase):
    def setUp(self):
        self.correct_title = "title"
        self.correct_description = "description"
        self.correct_category_id = "1"
        self.correct_is_default = "0"
        self.correct_target_sets = "5,5"
        self.correct_measurement_type = "REP"
        self.correct_level = "5"

    def test_correct(self):
        exercise.Exercise(self.correct_title, self.correct_description, self.correct_category_id,
        self.correct_is_default, self.correct_target_sets, self.correct_measurement_type, self.correct_level)
    
    def test_invalid_title(self):
        with self.assertRaises(ValueError):
            exercise.Exercise("", self.correct_description, self.correct_category_id,
            self.correct_is_default, self.correct_target_sets, self.correct_measurement_type, self.correct_level)

    def test_invalid_category_id(self):
        with self.assertRaises(ValueError):
            exercise.Exercise(self.correct_title, self.correct_description, "10",
            self.correct_is_default, self.correct_target_sets, self.correct_measurement_type, self.correct_level)
    
    def test_invalid_target_sets(self):
        with self.assertRaises(ValueError):
            exercise.Exercise(self.correct_title, self.correct_description, self.correct_category_id,
            self.correct_is_default, "1,", self.correct_measurement_type, self.correct_level)

    def test_invalid_measurement_type(self):
        with self.assertRaises(ValueError):
            exercise.Exercise(self.correct_title, self.correct_description, self.correct_category_id,
            self.correct_is_default, self.correct_target_sets, "reps", self.correct_level)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            exercise.Exercise(self.correct_title, self.correct_description, self.correct_category_id,
            self.correct_is_default, self.correct_target_sets, self.correct_measurement_type, "11")

if __name__ == '__main__':
    unittest.main()