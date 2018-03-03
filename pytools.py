import math


def calculate_entropy_single(x):
    return -(x)*math.log(x, 2)

def calculate_entropy_from_array(x):
    result=[]
    for i in x:
        h = -(i)*(math.log(i, 2))
        result.append(h)
    return sum(entropies)

def conditional_entropy(x, y, opt='conditional'):
    result = []
    if opt == 'joint':
        for i in len(x):
            h = x[i]*(math.log(y[i]/x[i], 2))
            result.append(h)
    return sum(entropies)        

def mutual_info_probability(x, y, opt=''):
    p, q = 0, 0
    p = calculate_entropy(x)
    q = calculate_entropy(y)
    if opt == 'conditional':
        i = p - q



    
        
