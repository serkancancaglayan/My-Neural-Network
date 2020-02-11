import random


# converts an array to a Matrix
def fromArray(array):
    matrix = Matrix(len(array), 1)
    matrix.initMatrixZEROS()
    for i in range(matrix.rows):
        matrix.matrix[i][0] = array[i]
    return matrix


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

    # initializes a matrix with zeroes
    def initMatrixZEROS(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            self.matrix.append(row)

    # initializes a matrix with random values
    def initMatrixRandom(self, low, high):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(random.uniform(low, high))
            self.matrix.append(row)

    # adds a constant value to matrix's every element
    def add(self, x):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] += x

    def addMatrix(self, toAdd):
        if self.rows == toAdd.rows and self.cols == toAdd.cols:
            result = Matrix(self.rows, self.cols)
            result.initMatrixZEROS()
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + toAdd.matrix[i][j]
            return result
        else:
            return None

    def subtractMatrix(self, toAdd):
        if self.rows == toAdd.rows and self.cols == toAdd.cols:
            result = Matrix(self.rows, self.cols)
            result.initMatrixZEROS()
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] - toAdd.matrix[i][j]
            return result
        else:
            return None

    def randomize(self, low, high):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.uniform(low, high)

    def multiplication(self, other):
        if self.cols != other.rows:
            return None
        result = Matrix(self.rows, other.cols)
        result.initMatrixZEROS()
        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                result.matrix[i][j] = sum
        return result

    def Activasion(self, activasionFunction):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = activasionFunction(self.matrix[i][j])

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        result.initMatrixZEROS()
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]
        return result

    def printMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end = " ")
            print()