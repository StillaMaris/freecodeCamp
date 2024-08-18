import numpy as np

def mean(mat, axis = None):
    return np.mean(mat, axis)

def variance(mat, axis = None):
    return np.var(mat, axis)

def std(mat, axis = None):
    return np.std(mat, axis)

def min_value(arr, axis=None):
    return np.min(arr, axis=axis)

def max_value(arr, axis=None):
    return np.max(arr, axis=axis)

def sum_value(arr, axis=None):
    return np.sum(arr, axis=axis)

def constraints(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

def calculate(list):

    # Check that the list has the required lenght: 9
    constraints(list)
    

    # Transform the list in a np.array
    array = np.array(list)

    # Trasform the array in a matrix 3,3
    matrix = array.reshape(3,3)

    # Define the dictionary
    calculations = { 'mean':[],
                     'variance':[],
                     'standard deviation':[],
                     'max':[],
                     'min':[],
                     'sum':[]
                     }


    # Insert values:
    for i in range(3):
        calculations['mean'].append(mean(matrix, i if i < 2 else None).tolist())
        calculations['variance'].append(variance(matrix, axis=i if i < 2 else None).tolist())
        calculations['standard deviation'].append(std(matrix, axis=i if i < 2 else None).tolist())
        calculations['max'].append(max_value(matrix, axis=i if i < 2 else None).tolist())
        calculations['min'].append(min_value(matrix, axis=i if i < 2 else None).tolist())
        calculations['sum'].append(sum_value(matrix, axis=i if i < 2 else None).tolist())


    return calculations