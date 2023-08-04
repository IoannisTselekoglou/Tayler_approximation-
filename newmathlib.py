#Key is a 2x1 array and cointains 2 variables: prefix and the actuall key: 
# sin = [1,0], cos = [1,4], -sin = [-1,0], -cos = [-1,4]
import numpy as np

def derivate(grad: int,key: list,x):
    n_list = []
    for i in range(grad):
        if key[0] == 1 and key[1] == 0:
           #np.sin(x)
           y = np.sin(x)
           key = [1,4]
           n_list.append(y)
        elif key[0] == 1 and key[1]== 4:
            #np.cos(x)
            y = np.cos(x)
            key = [-1,0]
            n_list.append(y)
        elif key[0] == -1 and key[1] == 0:
            #np.sin(x)
            y = np.sin(x)
            key = [-1,4]
            n_list.append(-y)
        elif key[0] == -1 and key[1] == 4:
            y = np.cos(x)
            key =[1,0]
            n_list.append(-y)
    return n_list
   
   
