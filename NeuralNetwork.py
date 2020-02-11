from Activasion import sigmoid
from Matrix import Matrix
from Matrix import fromArray

# hidden error matrixi None object type oluyor



class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes  # number of input nodes
        self.hidden_nodes = hidden_nodes  # number of nodes in hidden layer
        self.output_nodes = output_nodes  # number of output nodes

        # weight matrix between input and hidden layers
        self.weights_INPUT_HIDDEN = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_INPUT_HIDDEN.initMatrixRandom(-1, 1)

        # weight matrix between hidden and output layers
        self.weights_HIDDEN_OUTPUT = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_HIDDEN_OUTPUT.initMatrixRandom(-1, 1)

        # bias matrix for hidden layer
        self.bias_HIDDEN = Matrix(self.hidden_nodes, 1)
        self.bias_HIDDEN.initMatrixRandom(-1, 1)

        # bias matrix for output layer
        self.bias_OUTPUT = Matrix(self.output_nodes, 1)
        self.bias_OUTPUT.initMatrixRandom(-1, 1)

    def feedForward(self, inputMatrix):

        # hidden is weighted sum matrix
        hidden = self.weights_INPUT_HIDDEN.multiplication(inputMatrix)
        hidden = hidden.addMatrix(self.bias_HIDDEN)
        hidden.Activasion(sigmoid)

        # generating output
        output = self.weights_HIDDEN_OUTPUT.multiplication(hidden)
        output = output.addMatrix(self.bias_OUTPUT)
        output.Activasion(sigmoid)

        return output

    def trainNetwork(self, inputs, answer):
        inputMatrix = fromArray(inputs)
        answerMatrix = fromArray(answer)
        guess = self.feedForward(inputMatrix)
        output_errors = answerMatrix.subtractMatrix(guess)

        hiddenTranspose = self.weights_INPUT_HIDDEN.transpose()
        self.weights_INPUT_HIDDEN.printMatrix()
        print()
        hiddenTranspose.printMatrix()
        # hidden_errors = hiddenTranspose.multiplication(output_errors)


def main():
    nn = NeuralNetwork(2, 2, 1)
    input = [2.045, -3.14]
    print(nn.feedForward(fromArray(input)).matrix)

if __name__ == '__main__':
    main()
