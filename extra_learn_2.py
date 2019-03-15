


def some_data_2():
    
    import numpy as np
    import matplotlib.pyplot as plt
    import h5py
    import sklearn
    import sklearn.datasets
    import sklearn.linear_model
    import scipy.io

    data = scipy.io.loadmat('datasets/data.mat')
    train_X = data['X'].T
    train_Y = data['y'].T
    test_X = data['Xval'].T
    test_Y = data['yval'].T

     #plt.scatter(train_X[0, :], train_X[1, :], c=train_Y.ravel(), s=40, cmap=plt.cm.Spectral);
    
    return train_X, train_Y, test_X, test_Y
