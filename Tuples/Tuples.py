print('<---------------------TUPLES IN PYTHON--------------------->')

# print('\nCreate Tuples using Round Brackets ()---------------->')
#
# var = ('Hello', 'World', 'Beautiful')
# print(var)
#
# print('\nCreate a Tuple With One Item-------------->')
#
# values : tuple[int | str, ...] = (1, 2, 3, "Hello")
# print(values)

# In the above example we see that tuples can be created using different type of  values
# Here the type of values are int or str and the '...' implies that the tuple can contain multiple
# integers or string

# If you want to build a tuple with single element then there should be a comma after the object

# ex:
# tuple1 = ('World',)
# print("\ntype of tuple1 = ('World',)")
# print(type(tuple1))
# ===================>      <class 'tuple'>

# tuple2 = ('World')
# print("\ntype of tuple2 = ('World')")
# print(type(tuple2))
# ===================>      <class 'str'>

# print('\nTuple Constructor in Python-------------->')

# To create a tuple constructor, we will pass the elements as its parameters

# tuple_constructor = tuple(('Hello', 'Beautiful', 'World'))
# print(tuple_constructor)

#
# myTuple = (1, 2, 3, 4, 5, 2, 6)
#
# print(myTuple[1])
# print(myTuple[5])
#Tuples can contain duplicate values

# myTuple[1]=100 #TypeError: 'tuple' object does not support item assignment
# print(myTuple)

# Accessing Values in Python Tuples
#
# print('value in myTuple[0]:', myTuple[0])
# print('value in myTuple[1]:', myTuple[1])
# print('value in myTuple[2]:', myTuple[2])
# print('value in myTuple[4]:', myTuple[4])
# print(myTuple)
# print('value in myTuple[-1]:', myTuple[-1])
# print('value in myTuple[-3]:', myTuple[-3])
# print('value in myTuple[-5]:', myTuple[-5])
#
# print('\nConcatenation')
# t1=[1,2,3]
# t2=['Hello', 'Guys']
# print('Originals:\n',t1,'\n', t2)
# print('Concatenated:\n',t1+t2)
#
# print('\nNesting')
# t3=(t1,t2)
# print(t3)
#
# print('\nRepetition')
# t4=('Python',)*3
# print(t4)
#
# print('\nSlicing')
# t5=(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print('t5[1:]:',t5[1:])
# print('t5[::-1]:',t5[::-1])
# print('t5[1:4]:',t5[1:4])
#
# print('\nDeleting')
# t6=('Hello', 'World')
# print(t6)
# del t6
# print(t6)  #NameError: name 't6' is not defined. Did you mean: 't1'?
#
# print('\nFinding the Length')
# t7 = ('python', 'coding')
# print('Length of t7=',t7,'is:',len(t7))
#
# print('\nMultiple data types with tuples')
# t8 = ('Immutable', True, 100)
# print(t8)
#
# print('\nConverting a list to tuples')
# list1 = [1, 2, 3, 4]
# print('List is:',list1)
# print('Converted to tuple:',tuple(list1))
# print('\nString is: Python')
# print('Connverted to Tuple:',tuple('Python'))
#
# print('\nTuples in a loop')
# tup=('Hello',)
# n=5
# for i in range(n):
#     tup = (tup,)
#     print(tup)



# print('UNPACKING in Tuples')
# print()
# fruits = ('apple', 'banana', 'cherry')
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)

# n = int(input())
# s = ''
# for i in range(1,n+1):
#     s = s + i
# print(s)

# import functools
# A = int(input())
# s1 = set(map(int, input().split()))
# n = int(input())
# for i in range(n):
#     x1 = list(map(str, input().split()))
#     x2 = set(map(int, input().split()))
#     x3 = eval(x1[0] + '()')
#     s1 = s1.x3(x2)
# print(functools.reduce(lambda x, y : x+y, s1))

# def add(a, b):
#     pass
# print(type(add))

# set1 = {1, 2, 3, 4, 5, 5}
# set2 = {3, 5, 6, 8, 9}
# l = ["update"]
# method_name = l[0]
# getattr(set1, method_name)(set2)
# print(set1)

import functools

A = int(input())
s1 = set(map(int, input().split()))
n = int(input())
for i in range(n):
    x1 = list(map(str, input().split()))
    x2 = set(map(int, input().split()))
    x3 = x1[0]
    getattr(s1, x3)(x2)

print(s1)
print(functools.reduce(lambda x, y: x + y, s1))