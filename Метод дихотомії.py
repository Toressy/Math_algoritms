def f(x):
    return x**2-4

# Метод ділення навпіл
def bisection(a,b,e):
    step = 1
    print('\n\n*** Метод ділення навпіл ***')
    condition = True
    while condition:
        c = (a + b)/2
        print(f'step = {step}, c = {c:.7f} and f(c) = {f(c):.7f}')

        if f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c    
        else:
            return c

        step = step + 1
        condition = abs(f(c)) > e

    print(f'с = {c:.8f}')


a = float(input('a: '))
b = float(input('b: '))
e = float(input('e: '))


if f(a) * f(b) > 0.0:
    print('Wrong a and b')
else:
    bisection(a,b,e)
