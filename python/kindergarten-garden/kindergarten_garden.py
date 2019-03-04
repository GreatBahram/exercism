DEFAULT_STUDENTS = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve',
    'Fred', 'Ginny', 'Harriet', 'Ileana', 
    'Joseph', 'Kincaid', 'Larry',
]

FLOWERS_MAP = {
    'R': 'Radishes',
    'G': 'Grass',
    'C': 'Clover',
    'V': 'Violets',
}


class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.students = sorted(students)
        self.rows = diagram.splitlines()
    
    def plants(self, name):
        start = self.students.index(name) * 2
        end = start + 2
        return [
            FLOWERS_MAP[seed]
            for row in self.rows
            for seed in row[start:end]
        ]
