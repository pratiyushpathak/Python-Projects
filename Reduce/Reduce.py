import functools
import operator
print('<----------------------Reduce----------------------->')


lis = [1,3, 5, 6, 2, 1099, -17, -1]
print('The sum of the list element is: ',end='')
print(functools.reduce(lambda a, b :a+b, lis))

print('The maximum element of the list is: ', end='')
print(functools.reduce(lambda a, b : a if a>b else b, lis))

print('The smallest element is: ', end='')
print(functools.reduce(lambda a, b : a if a<b else b, lis))

print('reduce with operator functions')

print('The difference of the list elements is: ', end='')
print(functools.reduce(operator.sub, lis))

print('The product of the list elements is: ', end='')
print(functools.reduce(operator.mul, lis))

print('The sum of the list elements is: ', end='')
print(functools.reduce(operator.add, lis))

print('The concatenated output is: ', end='')
print(functools.reduce(operator.add, ['Hello ', 'Beautiful ', 'World']))