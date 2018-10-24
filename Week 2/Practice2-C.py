import numpy as np 
def your_array () : 
    
    l = np.array( [23,76,97,28,10,8,2,4,6] )
    r = np.mean(l, axis=None, dtype=int, out=None )
    b = np.std(l, axis=None, dtype=int, out=None, ddof=0 )
    c = np.median(l, axis=None, out=None, overwrite_input=False, keepdims=False)
    return ("your mean is : ",r,"your standerd deviation is : ",b,"your median is : ",c)
print (your_array ())
