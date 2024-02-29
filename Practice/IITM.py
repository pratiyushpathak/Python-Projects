# str1 = input()
# str2 = input()
# str3 = ''
# for char in str2:
#     if not str1.__contains__(char):
#         str3 += char
# print(str3)

# Palindrome

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

# n1 = int(input())
# n2 = int(input())
#
# coPrime = False
#
# l1 = [n1]
# l2 = [n2]

# for i in range(2, (n1)//2+1):
#     if n1%i == 0:
#         l1.append(i)
# for i in range(2, (n2)//2+1):
#     if n2%i ==0:
#         l2.append(i)
# for i in l1:
#     if l2.__contains__(i):
#         coPrime= False
#         break;
#     else:
#         coPrime= True
# if coPrime:
#     print('CoPRIME')
# else:
#     print('Not Coprime')

# num = input()
#
# if num.isnumeric():
#     print('Integer')
# elif num.__contains__('.'):
#     print('Float')
# else:
#     print('None')

# str1 = list(map(str, input().split()))
# str2 = input()
# count = str1.count(str2)
#
# if count != 0:
#     print('YES')
#     print(count)
# else:
#     print('NO')

# n = int(input())
# l1 = [i for i in range(1, n+1, +1)]
# print(l1)

n = int(input())
# li=[]
# for i in range(n):
#     li.append(input())
# print(li)

li=[input() for i in range(n)]
print(li)