
# Q: Accept four integers as input and write a program to print these integers in non decreasing
#    print(order)
#    The input will be four integers in four lines. The output should be in single line with all the integers separated by a single space in a non decreasing manner

# a = []
#
# for i in range(4):
#     a.append(int(input()))
#
# a.sort()
# print(*a)


#vowels:

# word = input()
# length = len(word)
# v1=[]
# v2=[]
# v3=[]
# v4=[]
# v5=[]
# isValid = False
# for i in range(length):
#     if word[i]=='a':
#         v1.append(i)
#     elif word[i]=='e':
#         v2.append(i)
#     elif word[i]=='i':
#         v3.append(i)
#     elif word[i]=='o':
#         v4.append(i)
#     elif word[i]=='u':
#         v5.append(i)
# if len(v1)>0 and len(v2)>0 and len(v3)>0 and len(v4)>0 and len(v5)>0:
#     if v1[0] < v2[0] and v2[0] < v3[0] and v3[0] < v4[0] and v4[0] < v5[0]:
#         if len(v1)>=len(v2) and len(v2)>=len(v3) and len(v3)>=len(v4) and len(v4)>=len(v5):
#             isValid=True
#
# if isValid:
#     print('It is a perfect word')
# else:
#     print('It is not a perfect word')

# print(len(v1))

# for x in range(100):
#     for y in range(100):
#         if x != y:
#             print(f'{x},{y}')

# series of fibbonacci series


# x = int(input())
# sum=0
#
# def fibo(num):
#     fiboSum=0
#     for i in range(num+1):
#         fiboSum += i
#     return fiboSum
#
# for i in range(x+1):
#     sum += fibo(i)
#
# print(sum)

# n = int(input())
# def isPrime(num):
#     isprime = True
#     if num == 1:
#         isprime=False
#     elif num == 2 or num == 3 :
#         isprime = True
#     elif num>3:
#         for i in range (2, ((num//2)+1)):
#             if num % i == 0 :
#                 isprime= False
#     return isprime
# for i in range(1, n+1):
#     if n % i == 0:
#         if isPrime(i):
#             print(i)
#


#BOT

# import math
#
# x, y =0, 0
# while True:
#     step = input()
#
#     if step == 'STOP':
#         break
#     else:
#         if step == 'START':
#             x = 0
#             y =0
#         elif step == 'RIGHT':
#             x += 1
#         elif step == 'LEFT':
#             x -= 1
#         elif step == 'UP':
#             y += 1
#         elif step == 'DOWN':
#             y -= 1
#
# sum = abs(x) + abs(y)
#
# print(sum)


# s = input()
# s_lower = s.lower()
# res=[]
# for i in range(len(s_lower)):
#     res.append(s_lower[i])
# for x in sorted(res):
#     print(x, end='')

# n = input()
# num = str(n)
# first_digits = ['6', '7', '8', '9']
# seven_list = []
# isValid = False
# for char in num:
#     if(num.count(char) > 7):
#         seven_list.append(char)
#
# def condFour(x):
#     for i in range(10):
#         if str(i)*6 in str(x):
#             return False
#     return True
#
# if first_digits.__contains__(num[0]):
#     if len(num) == 10:
#         if len(seven_list) == 0 :
#             if condFour(n) == True:
#                 isValid=True
#
# if isValid:
#     print('Valid')
# else:
#     print('Not Valid')

# for i in range(1,6):
#     for j in range(1, i+1):
#         if j==i:
#             print(j,end='')
#         else:
#             print(j, end=' , ')
#     print()
# for i in range(4, 0, -1):
#     for j in range(1, i+1):
#         if j==i:
#             print(j,end='')
#         else:
#             print(j, end=' , ')
#     print()


# a = input()
# b = input()
# c =""
# for i in range(len(a+b)):
#     c += sorted(a+b)[i]
# print(c)

# str = input()
# if (str.__contains__('.') and str.count('.')==1) or str.isnumeric():
#     if str.__contains__('.'):
#         print('Float')
#     else:
#         print('Integer')
# else:
#     print('None')


# num = int(input())
# prime = False
# def isPrime(x):
#     if x == 2 or x == 3:
#         prime = True
#     else:
#         for i in range(2, x//2 +1):
#             if x % i == 0:
#                 prime = False
#                 break
#             else:
#                 prime = True
#
#     if prime:
#         print('PRIME')
#     else:
#         print('NOTPRIME')
# isPrime(num)
#
# length = {'abcdefghijklmnopqrstuvwxyz':26,}
# while True:
#     word = input()
#     if word == 'abcdefghijklmnopqrstuvwxyz':
#         # length.update({word: len(word)} )
#         break
#     else:
#         length.update({word: len(word)})
#
#
#
# sorted_length = sorted(length.items(), key=lambda x:x[1])
# print(sorted_length[0][0])

# n = int(input())
# numbers = range(1, n+1)
# list(map(print, numbers))

# s = input().lower()
# s1 = s[0:len(s)//2]
# s2 = s[len(s)//2 if len(s) % 2 == 0 else ((len(s)//2)+1):]
# palindrome = False
# for i in range(len(s)//2):
#     if s1[i] == s2[-(i+1)]:
#        palindrome=True
#     else:
#         palindrome= False
#
# if palindrome:
#     print('PALINDROME')
# else:
#     print('NOT PALINDROME')


