import sys

class Exercise:
    def __init__(self, title, description, category_id, is_default, target_sets, measurement_type, level):
        self.parse_title(title)
        self.parse_description(description)
        self.parse_category_id(category_id)
        self.parse_is_default(is_default)
        self.parse_target_sets(target_sets)
        self.parse_measurement_type(measurement_type)
        self.parse_level(level)

    def parse_title(self, title):
        if title == "":
            raise ValueError("title empty")
        self.title = title
    
    def parse_description(self, description):
        if description is None:
            self.description = ""
        else:
            self.description = description
    
    def parse_category_id(self, category_id):
        cat_id_int = int(category_id)
        if cat_id_int < 1 or cat_id_int > 6:
            raise ValueError("cat ID invalid:" + category_id)
        self.category_id = cat_id_int

    def parse_is_default(self, is_default):
        if is_default == "1":
            self.is_default = True
        elif is_default == "0":
            self.is_default = False
        else:
            raise ValueError("isDefault invalid:" + is_default)
    
    def parse_target_sets(self, target_sets):
        arr = target_sets.split(',')
        sets = []
        for w in arr:
            sets.append(int(w))
        if len(sets) == 0:
            raise ValueError("target sets empty")
        self.target_sets = sets
    
    def parse_measurement_type(self, measurement_type):
        upper_measurement_type = measurement_type.upper()
        if upper_measurement_type == "REP" or upper_measurement_type == "SECONDS":
            self.measurement_type = upper_measurement_type
        else:
            raise ValueError("measurement type invalid: " + measurement_type)
    
    def parse_level(self, level):
        level_int = int(level)
        if level_int > 10 or level_int < 1:
            raise ValueError("level out of range 1~10:" + level)
        self.level = level_int
