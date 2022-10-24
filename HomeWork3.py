import math

input_str = input()

values=input_str.split()
count =len(values)

if count == 1:
    r = int(''.join(values))
    if r == 0:
        print('There can\'t be a circle with 0 radius')
    else:
        print(f'circle: radius = {r}; P = {2*r*3.14}; S = {3.14*r**2}')

if count == 2:
    a, b = values
    a1 = int(a)
    b1 = int(b)
    if a1 <= 0 or b1 <= 0:
        print('this rectangle or square cannot exist')
    else:
        if a1 == b1:
            print(f'square: side = {a1}, P = {4*a1}, S = {2**a1}')
        else:
            print(f'rectangle: a = {a1}, b = {b1}, P = {2*(a1+b1)}, S = {a1*b1}')

if count == 3:
    a, b, c = values
    a1 = int(a)
    b1 = int(b)
    c1 = int(c)
    if a1 <= 0 or b1 <= 0 or c1 <= 0:
        print('no such triangle exists')
    elif a1 + b1 <= c1 or a1 + c1 <= b1 or b1 + c1 <= a1:
        print('wrong side ratio')
    else:

    # Расчёт площади (S) треугольника по формуле Герона
        p1 = 1/2 * (a1 + b1 + c1)
        print(f'triangle: a = {a1}, b = {b1}, c = {c1}, P = {a1 + b1 + c1}, S = {math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1))}')