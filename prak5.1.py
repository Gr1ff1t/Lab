class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

# Example usage
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

# Addition
print("Addition:")
print(matrix1 + matrix2)

# Subtraction
print("Subtraction:")
print(matrix1 - matrix2)

# Multiplication
print("Multiplication:")
print(matrix1 * matrix2)
