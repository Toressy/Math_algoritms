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


#Метод Ньютона
def newton(x0,e):
    print('\n\n*** Метод Ньютона ***')
    step = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print(f'Step = {step}, x1 = {x1:.7f} and f(x1) = {f(x1):.7f}')
        
        step = step + 1
        
        condition = abs(x1-x0) > e
        x0 = x1
    
    print(f'\nВідповідь: {x1:.7f}')
    

x0 = float(input('x0: '))
e = float(input('e: '))

newton(x0,e)