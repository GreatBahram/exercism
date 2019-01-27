class Matrix:
    def __init__(self, matrix_string):
        matrix = self.matrix_from_string(matrix_string)
        transpose = self.transpose(matrix)
        self.rows, self.columns = matrix, transpose

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]

    @staticmethod
    def matrix_from_string(string):
        """Parse matrix from string."""
        return [
            [int(item) for item in row.split()]
            for row in string.splitlines()
        ]

    @staticmethod
    def transpose(matrix):
        """Return a transposed version of a matrix."""
        return [
            list(column)
            for column in zip(*matrix)
        ]
