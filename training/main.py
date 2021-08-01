import numpy as np
import csv

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})



def sigmoid(x):
    return 1/(1+np.exp(-x))

def dsigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

# Feed forward
def train():
    #Initializing weights
    global hiddenWeights
    hiddenWeights = np.random.rand(3, 3) * 0.01
    global finalWeights
    finalWeights = np.random.rand(2, 3) * 0.01

    #Initializing biases
    global hiddenBiases
    hiddenBiases = np.random.rand(3, 1) * 0.01
    global finalBiases
    finalBiases = np.random.rand(2, 1) * 0.01
    with open('data.csv', mode ='r') as file:
        dataFile = csv.reader(file)

        for example in dataFile:
            #Format inputs
            inputs = np.asarray([int(i)/255 for i in example[:3]])
            inputs = np.reshape(inputs, (3,1))

            #Format outputs
            outputs = np.asarray([int(i) for i in example[3:5]])
            outputs = np.reshape(outputs, (2,1))

            #Calculate hidden layer
            hiddenZ = np.dot(hiddenWeights, inputs) + hiddenBiases
            hiddenLayer = sigmoid(hiddenZ)

            #Calculate final layer
            finalZ = np.dot(finalWeights, hiddenLayer) + finalBiases
            finalLayer = sigmoid(finalZ)

            #Calculate errors
            finalError = np.multiply((finalLayer - outputs), dsigmoid(finalZ))
            hiddenError = np.multiply(np.matmul(finalWeights.transpose(), finalError), dsigmoid(hiddenZ))

            #Calculate changes
            changeFinalWeights = np.dot(finalError, hiddenLayer.transpose())
            changeFinalBias = finalError
            changeHiddenWeights = np.dot(hiddenError, inputs.transpose())
            changeHiddenBias = hiddenError

            #Apply changes
            finalWeights += changeFinalWeights
            finalBiases += changeFinalBias
            hiddenWeights += changeHiddenWeights
            hiddenBiases += changeHiddenBias

    # print("Hidden weights: " + str(hiddenWeights))
    # print("Hidden biases: "+ str(hiddenBiases))
    # print("Final weights: " + str(hiddenWeights))
    # print("Final biases: "+ str(hiddenBiases))
    # print("Final error: " + str(finalError))

def guess(r, g, b):
    inputs = np.asarray([r/255, g/255, b/255])
    inputs = np.reshape(inputs, (3,1))

    #Calculate hidden layer
    hiddenZ = np.dot(hiddenWeights, inputs) + hiddenBiases
    hiddenLayer = sigmoid(hiddenZ)

    #Calculate final layer
    finalZ = np.dot(finalWeights, hiddenLayer) + finalBiases
    finalLayer = sigmoid(finalZ)

    finalList = np.reshape(finalLayer, (1,2)).tolist()
    #return finalList
    if(finalList[0][0] > finalList[0][1]):
        return "White text"
    else:
        return "Black text"

train()
print(guess(255, 255, 255))