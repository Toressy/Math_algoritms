# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 18:50:26 2022

@author: Victoria
"""
#функція
def f(x):
    return x**2 - 4
#похідна
def g(x):
    return 2*x


#Метод релаксації
def relaxation(x0,e,a):
    print('\n\n*** Метод релаксації ***')
    if a*g(x0) < 0 and a*g(x0) > -2:
        step = 1
        condition = True
        while condition:
                   
            x1 = x0 + a*f(x0)
            print(f'Step = {step}, x1 = {x1:.7f} and f(x1) = {f(x1):.7f}')
            
            step = step + 1
            
            
            condition = abs(x1-x0) > e
            x0 = x1
        
        print(f'\n Відповідь: {x1:.7f}')
    else:
        print('Error,\nWrong x0 and a')
    

relaxation(-0.5,0.00001,0.001)