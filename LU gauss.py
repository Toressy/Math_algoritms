
import numpy as np
import random
from scipy.linalg import hilbert
def luDecomp(mat, n):
    global lower, upper
  
    lower = np.zeros_like(mat, dtype=np.double)
    upper = np.zeros_like(mat, dtype=np.double);

    
    for i in range(n):
	    for k in range(i, n):
		    sum = 0
		    for j in range(i):
			    sum += (lower[i][j] * upper[j][k])
		    upper[i][k] = mat[i][k] - sum

	    for k in range(i, n):
		    if (i == k):
			    lower[i][i] = 1 
		    else:
			    sum = 0
			    for j in range(i):
				    sum += (lower[k][j] * upper[j][i])

			    lower[k][i] = (mat[k][i] - sum) / upper[i][i]
								


def forwsub(lower, b, n):    
    n = lower.shape[0]
    global y
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / lower[0, 0]
       
    for i in range(1, n):
            sum1 = 0
            for j in range(i):
                sum1 += (lower[i][j] * y[j])
            y[i] = (b[i] - sum1) / lower[i,i]    
    return y

def backsub(upper, y):   
    n = upper.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / upper[-1, -1] 
    for i in range(n-2, -1, -1):
        sum1 = 0
        for j in range(i+1, n):
            sum1 += (upper[i][j] * x[j])
        x[i] = (y[i] - sum1) / upper[i,i]        
    return x
a = np.random.randint(-500,500,(30, 30))
#b = random.sample(range(10, 30), 3)
a = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
a = hilbert(5)
#a = [[8, 6, 5],[3, 3, 2],[4, 2, 3]]   
b = np.ones(5)
b = np.dot(a, b)
n = 5

luDecomp(a, n)
forwsub(lower, b, n)
print(backsub(upper, y))
