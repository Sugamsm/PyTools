import math

def calculate_entropy(x, opt):
    result=[]
    if opt == 'single':
        return -(x)*math.log(x, 2)
    elif opt == 'array':
        for i in x:
            h = -(i)*(math.log(i, 2))
            result.append(h)
        return sum(entropies)
    else:
        print('opt should be either \'single\' or \'array\'')
        return 0

def conditional_entropy(x, y, opt):
    result = []
    if opt == 'single_joint':
        return x*math.log(y/x, 2)
    elif opt == 'single_conditional':
        return y*x*math.log(x, 2)
    elif opt == 'array_joint':
        for i in range(len(x)):
            h = x[i]*(math.log(y[i]/x[i], 2))
            result.append(h)
    elif opt == 'array_conditional':
        for i in range(len(x)):
            h = -y[i]*x[i]*math.log(x[i], 2)
            result.append(h)
    else:
        print('opt should be either \'single_conditional\',\'single_joint\'\
              or \'array_conditional\', \'array_conditional\'')
    return sum(result)        

def mutual_info(x, y, joint, opt):
    if opt == 'single':
        return joint*math.log(joint/(x*y), 2)
    elif opt == 'array':
        result = []
        for i in range(len(x)):
            result.append(joint[i]*math.log(joint[i]/(x[i]*y[i]), 2))
        return sum(result)

def relative_entropy(p, q, opt):
    result = []
    if opt == 'single':
        return p*math.log(p/q, 2)
    elif opt == 'array':
        for i in range(len(p)):
            h = p[i]*math.log(p[i]/q[i], 2)
            result.append(h)
        return sum(result)
    else:
        print('opt should have value either \'single\' or \'array\'')


    
        
