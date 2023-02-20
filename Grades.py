class Grades:
    def __init__(self, code, units, grades):
        self.code = code
        self.units = units
        self.grades = grades
    def __str__(self):
        return f"{self.code}({self.units}) = {self.grades}"
