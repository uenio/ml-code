import numpy as np

class GenericLinearRegression(object):
    xMatrix0 = []
    yMatrix0 = []
    weights0 = []
    
    xMatrix1 = []
    yMatrix1 = []
    weights1 = []
    
    def stringListToFloatList(self, strList):
        # insert bias of 1
        floatList = [1]
        for i in strList[:-2]:
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

            if (curFloatVec[-1] == 0):
                # add to x matrix
                self.xMatrix0.append(curFloatVec)

                # add last data point to y matrix
                self.yMatrix0.append(float(curStrVec[-2]))
            else:
                # add to x matrix
                self.xMatrix1.append(curFloatVec)

                # add last data point to y matrix
                self.yMatrix1.append(float(curStrVec[-2]))

            print(self.xMatrix0)

    def train(self):
        run = 0
        while run < self.max_iterations:
            run += 1
            for instance in self.vectors:
                if ((np.dot(self.weights, instance[:-1]) >= 0 and instance[-1] == -1)
                    or (np.dot(self.weights, instance[:-1]) < 0 and instance[-1] == 1)):
                    self.weights = np.add(self.weights, np.multiply(np.multiply(instance[:-1], self.learningRate),instance[-1]))
            if self.checkWrongs(self.weights) < self.checkWrongs(self.pocketWeights):
                self.pocketWeights = np.copy(self.weights)
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
