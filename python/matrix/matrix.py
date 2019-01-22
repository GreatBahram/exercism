class Matrix:
    def __init__(self, matrix_string):
        self.from_string(matrix_string)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]

    def from_string(self, string):
        """Parse matrix from string input."""
        self.matrix = [
            [int(item) for item in row.split()]
            for row in string.splitlines()
        ]
