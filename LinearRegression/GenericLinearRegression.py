import numpy as np
from numpy import linalg as LA

class GenericLinearRegression(object):
    xMatrix0 = []
    yMatrix0 = []
    weights0 = []
    aaa = []
    
    xMatrix1 = []
    yMatrix1 = []
    weights1 = []
    
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

            if (curFloatVec[-1] == 0):
                # add to x matrix
                self.xMatrix0.append(curFloatVec[:-2])

                # add last data point to y matrix
                self.yMatrix0.append(float(curStrVec[-2]))
                self.aaa = curFloatVec[:-1]
            else:
                # add to x matrix
                self.xMatrix1.append(curFloatVec[:-2])

                # add last data point to y matrix
                self.yMatrix1.append(float(curStrVec[-2]))

    def findBestFitLine0(self):
        # find A
        a = np.dot(np.transpose(self.xMatrix0), self.xMatrix0)
        b = np.dot(np.transpose(self.xMatrix0), self.yMatrix0)
        
        # do a eigenvalue decomposition to find A=VDV^T
        ev, v = LA.eig(a)

        # find d
        d = np.diag(ev)

        # find d+
        anotherD = np.copy(d)
        for i in range(len(d)):
            for j in range(len(d[0])):
                if (i == j):
                    anotherD[i][j] = 1 / anotherD[i][j]
                else:
                    anotherD[i][j] = 0

        # to find w, first find VDD+V^T
        # Aw = VDD+V^Tb
        self.weights0 = v @ d @ anotherD @ np.transpose(v) @ b @ LA.inv(a)
        
    def findBestFitLine1(self):
        # find A
        a = np.dot(np.transpose(self.xMatrix1), self.xMatrix1)
        b = np.dot(np.transpose(self.xMatrix1), self.yMatrix1)
        
        # do a eigenvalue decomposition to find A=VDV^T
        ev, v = LA.eig(a)

        # find d
        d = np.diag(ev)

        # find d+
        anotherD = np.copy(d)
        for i in range(len(d)):
            for j in range(len(d[0])):
                if (i == j):
                    anotherD[i][j] = 1 / anotherD[i][j]
                else:
                    anotherD[i][j] = 0

        # to find w, first find VDD+V^T
        # Aw = VDD+V^Tb
        self.weights1 = v @ d @ anotherD @ np.transpose(v) @ b @ LA.inv(a)

    def learn(self):
        self.findBestFitLine0()
        self.findBestFitLine1()
        self.eucDisPointToPlane(self.aaa, self.weights0)

    def eucDisPointToPlane(self, point, plane):
        # put in bias and take out the last feature
        pointAndBias = [1]
        pointAndBias += point[1:-1]

        # x*w + b / ||w||
        print(np.dot(pointAndBias, self.weights0) / LA.norm(self.weights0[1:]))
        
        
    def checkWrongs(self, weights):
        counter = 0 
        for instance in self.vectors:
            output = np.dot(instance[:-1], weights)
            
            # if there exists i such that outputs aren't equal
            if np.dot(instance[:-1], weights)*instance[-1] <= 0:
                counter += 1
        return counter

    
glr = GenericLinearRegression()
glr.learn()
