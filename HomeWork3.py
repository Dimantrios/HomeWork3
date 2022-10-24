import math

input_str = input()

values = input_str.split()
count =len(values)

if count == 1:
    a = int(''.join(values))
    if a == 0:
        print('There can\'t be a circle with 0 radius')
    else:
        print(f'circle: radius = {a}; perimeter = {2*a*3.14}; area = {3.14*a**2}')