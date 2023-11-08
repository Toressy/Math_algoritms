import numpy as np
#import random
import math

def jacobi(a, x ,b, n, N):
     temp_x = x
     for i in range(0, N):                    
       for j in range(0, n):        
         d = b[j] 
         
         for i in range(0, n):     
             if(j != i):
                 d-=a[j][i] * x[i]
         temp_x[j] = d / a[j][j]
       new_x = [0 for c in range(n)]
       for i in range(0, n): new_x.append(temp_x[i] - x[i])
       if np.linalg.norm(new_x) / np.linalg.norm(x) < (1*math.e-8): break
       x = temp_x  
     return temp_x 


   
#a = np.random.randint(-500,500,(3, 3))
#b = random.sample(range(10, 30), 3)
#a = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]                    
x = [1, 1, 1]                        
a = [[8, 6, 5],[3, 3, 2],[4, 2, 3]]   
b = [21, 10, 8]
n = len(b)
N = 1000
            
x = jacobi(a, x,  b, n, N)
print(x) 
