#Implementation of logistic regression using Gradient descent algorithm.
__author__ = 'Vardhaman'
import sys, getopt
import math
import csv
import math
import copy
import time
import numpy as np
from collections import Counter
from numpy import *
import matplotlib.pyplot as plt

def normalize(matrix,sd,me):
    with np.errstate(divide='ignore'):
        a = matrix
        sd_list = []
        mean_list = []
        if me == 0 and sd == 0:
            b = np.apply_along_axis(lambda x: (x-np.mean(x))/float(np.std(x)),0,a)
            tmp = a.shape[1]
            for i in range(tmp):
                sd_list.append(np.std(a[:,i]))
                mean_list.append(np.mean(a[:,i]))
            return b,sd_list,mean_list
        else:
            res = np.empty(shape=[a.shape[0],0])

            for i in range(a.shape[1]):
                col = matrix[:, i]
                mean_val = me[i]
                std_val = sd[i]
                b = np.apply_along_axis(lambda x: (x-mean_val)/float(std_val),0,col)
                res = np.concatenate((res, b), axis=1)
        res = np.nan_to_num(res)
    return res,sd,me

def load_csv(file):
    X = genfromtxt(file, delimiter=",",dtype=str)
    np.random.shuffle(X)
    return (X)

def random_numpy_array(ar):
    np.random.shuffle(ar)
    arr = ar
    return arr

def generate_set(X):
    X = X.astype(np.float)
    num_test = round(0.1*(X.shape[0]))
    start = 0
    end = num_test
    test_attri_list =[]
    test_class_names_list =[]
    training_attri_list = []
    training_class_names_list = []
    for i in range(10):
        X_test = X[start:end , :]
        tmp1 = X[:start, :]
        tmp2 = X[end:, :]
        X_training = np.concatenate((tmp1, tmp2), axis=0)
        y_training = X_training[:, -1]
        y_test = X_test[:, -1]
        X_training = X_training[:,:-1]
        X_test = X_test[:,:-1]
        X_training = np.matrix( X_training )
        X_test = np.matrix(X_test)
        X_training_normalized,sd,mean = normalize(X_training,0,0)
        X_training_normalized = np.nan_to_num(X_training_normalized)
        X_test_normalized,sd,mean = normalize(X_test,sd,mean)
        len1 = X_training_normalized.shape[0]
        len2 = X_test_normalized.shape[0]
        x_training_ones = np.ones(len1)
        x_training_ones = x_training_ones.reshape([x_training_ones.shape[0],1])
        x_test_ones = np.ones(len2)
        x_test_ones = x_test_ones.reshape([x_test_ones.shape[0],1])
        X_training_normalized = np.concatenate((x_training_ones,X_training_normalized),axis=1)
        X_test_normalized = np.concatenate((x_test_ones,X_test_normalized),axis=1)
        y_test = y_test.flatten()
        y_training = y_training.flatten()
        test_attri_list.append(X_test_normalized)
        test_class_names_list.append(y_test)
        training_attri_list.append(X_training_normalized)
        training_class_names_list.append(y_training)
        start = end
        end = end+num_test
    return test_attri_list,test_class_names_list,training_attri_list,training_class_names_list

def gradient_descent(X,Y,lRate,tolerance,plotGraph):
    #MaxIterCount is 1000, don't iterate more than 1000 times
    max_iter = 1000
    #Count the number of features
    X_count = X.shape[1]
    #Create a feature vector with each element assigned to zero
    thetha = np.zeros(X_count)
    initialthetha = thetha
    x_vals = []
    y_vals = []
    iterCount = 0
    #calculate value of element in each weight vector
    while( max_iter > iterCount):
        iterCount += 1
        for i in range(X_count):
            prediction = cal_gradient(X,Y,thetha,i)
            prevWeightValue = thetha[i]
            thetha[i] = prevWeightValue - lRate*prediction
        if plotGraph:
            #rmse,sse = compute_rmse(X,Y,thetha)
            mean = compute_log_loss(X,Y,thetha)
            x_vals.append(iterCount)
            y_vals.append(mean)
    if plotGraph:
        plt.suptitle("Gradient Descent plot")
        plt.plot(x_vals,y_vals)
        plt.xlabel("Iteration ")
        plt.ylabel("RMSE")
        fileName = "GradientDescentPlot";
        plt.savefig(fileName)
    return thetha

def compute_log_loss(X,Y,thetha):
    p_1 = sigmoid(np.dot(X, thetha)) # predicted probability of label 1
    log_l = (-Y)*np.log(p_1) - (1-Y)*np.log(1-p_1) # log-likelihood vector

    return log_l.mean()
def sigmoid(X):
    return 1 / (1 + np.exp(- X))

def cal_gradient(X,Y,thetha,pos):
    sum = 0.0
    #temp_fea = np.dot(X,thetha)
    temp_fea = sigmoid(np.dot(X, thetha))
    for i in range(temp_fea.shape[0]):
            sum = sum + ((temp_fea[i] - Y[i])*X[i][pos])
    return sum

def compute_rmse(test_X,test_Y,thetha):
    m = test_Y.size
    predict = test_X.dot(thetha)
    error = predict - test_Y
    sse = error.T.dot(error)/float(m)
    rmse = math.sqrt(sse)
    return rmse,sse

def compute_efficiency(test_X,test_Y,thetha):
    m = test_Y.size
    right = 0
    #prediction = test_X.dot(thetha)
    for i in range(m):
        prediction = 0
        value  = np.dot(thetha,test_X[i])
        if value >= 0.5:
            prediction = 1
        else:
            prediction = 0

        if prediction == test_Y[i]:
            right+=1

    print "Total : ",test_X.shape[0]," Correct : ",right," Percentage : ",right*100/test_X.shape[0]
    return right*100/test_X.shape[0]


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"f:t:e:")
    except getopt.GetoptError as error:
        print "Unknown input argument provided : "," Error : ",str(error)
        sys.exit(2)
    newfile = ""
    tolerance = 0.0
    eta = 0.0
    for opt,value in opts:
        if opt == "-f":
            newfile = value
        if opt == "-t":
            tolerance = float(value)
        if opt == "-e":
            eta = float(value)
    num_arr = load_csv(newfile)
    test_x,test_y,training_x,training_y = generate_set(num_arr)
    res = []
    for i in range(len(training_x)):
        plotGraph = False
        plotGraph = (i == len(training_x) - 3)
        theta = gradient_descent(training_x[i],training_y[i],eta,tolerance,plotGraph)
        res.append(compute_efficiency(test_x[i],test_y[i],theta))
    npResult = np.array(res)
    print "Mean : ",np.mean(npResult,axis = 0)," SD : ",np.std(npResult,axis = 0)

if __name__ == "__main__":
    main(sys.argv[1:])
