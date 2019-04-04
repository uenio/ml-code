import numpy as np


class Perceptron(object):
    vectors = []
    weights = []
    
    def stringListToFloatList(self, strList):
        floatList = []
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
            # add to list of vectors
            self.vectors.append(curFloatVec)

        # instantiate weights to 0 and set weight[0] to bias
        self.weights = np.zeros(len(curFloatVec))

    
perceptron = Perceptron()
