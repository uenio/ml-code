import numpy as np


class Perceptron(object):
    vectors = []
    weights = []
    activation = 0
    max_iterations = 900
    
    def stringListToFloatList(self, strList):
        # insert bias of 1
        floatList = [1]
        for i in strList:
            floatList.append(float(i))
        return floatList
    
    def __init__ (self):
        # open file and skip first line
        f = open("Breast_cancer_data.csv", "r")
        next(f)

        # read line by line
        for line in f:
            # split string by commas and transform into float lists
            curStrVec = line.split(',')
            curFloatVec = self.stringListToFloatList(curStrVec)
            # change 0 to -1
            if curFloatVec[-1] == 0:
                curFloatVec[-1] = -1
            # add to list of vectors
            self.vectors.append(curFloatVec)

        # instantiate weights to 0 and set weight[0] to bias
        self.weights = np.zeros(len(curFloatVec)-1)

    def output(self, instance):
        # dot product of weights(minus bias) and instance(minus output) plus bias
        output = np.dot(self.weights, instance[:-1])
        # activation function
        if output > self.activation:
            result  = 1
        else:
            result = -1
        return result

    def train(self):
        for _ in range(self.max_iterations):
            allCorrect = True
            for instance in self.vectors:
                output = self.output(instance)

                # if there exists i such that outputs aren't equal
                if self.output(instance)*instance[-1] <= 0:
                    allCorrect = False
                    # updated weight = weight + y(i)*x(i)
                    self.weights = np.add(self.weights, np.multiply(instance[:-1], instance[-1]))
            # if everything correct, just return weights
            if allCorrect:
                break
        return self.weights

    def checkWrongs(self):
        counter = 0 
        for instance in self.vectors:
            output = self.output(instance)
            
            # if there exists i such that outputs aren't equal
            if self.output(instance)*instance[-1] <= 0:
                counter += 1
        return counter
                

    
perceptron = Perceptron()
print(perceptron.train())

