class Matrix:
    def __init__(self, matrix):
        transpose = self.transpose(matrix)
        self.rows, self.columns = matrix, transpose
        self.validate()

    @staticmethod
    def transpose(matrix):
        """Return a transposed version of a matrix."""
        return [
            list(column)
            for column in zip(*matrix)
        ]

    def validate(self):
        """Validate irregular matrix."""
        if len(self.rows) > 0:
            first_row = self.rows[0]
            if any(len(row) != len(first_row) for row in self.rows):
                raise ValueError('Irregular matrix.')

def saddle_points(matrix_list):
    matrix = Matrix(matrix_list)
    return {
        (row_index + 1, col_index + 1)
        for row_index, row in enumerate(matrix.rows)
        for col_index, cell in enumerate(row)
        if cell == max(row) and cell == min(matrix.columns[col_index])
    }
