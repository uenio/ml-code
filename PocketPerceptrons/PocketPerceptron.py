import numpy as np

class PocketPerceptron(object):
    vectors = []
    weights = []
    pocketWeights = []

    learningRate = 0.5
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
        self.pocketWeights = np.zeros(len(curFloatVec)-1)

    def train(self):
        run = 0
        while True:
            run += 1
            for instance in self.vectors:
                if ((np.dot(self.weights, instance[:-1]) >= 0 and instance[-1] == -1)
                    or (np.dot(self.weights, instance[:-1]) < 0 and instance[-1] == 1)):
                    self.weights = np.add(self.weights, np.multiply(instance[:-1], self.learningRate))
            print(run)
            if self.checkWrongs(self.weights) < self.checkWrongs(self.pocketWeights):
                self.pocketWeights = np.copy(self.weights)
            else:
                return self.pocketWeights
            
        return self.pocketWeights

    def checkWrongs(self, weights):
        counter = 0 
        for instance in self.vectors:
            output = np.dot(instance[:-1], weights)
            
            # if there exists i such that outputs aren't equal
            if np.dot(instance[:-1], weights)*instance[-1] <= 0:
                counter += 1
        return counter
                
perceptron = PocketPerceptron()
print(perceptron.train())
