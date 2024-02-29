print('\nLists in Python ******* :) *******\n')

# li = ['Python', 'Java', 'DotNet']
# print(li)
#
# li.append('ReactJs')
# print(li)

# li = [1, 23, 34, [23, 45, ['Java', 'Python']]]
#
# print(li)
# [1, 23, 34, [23, 45, ['Java', 'Python']]]
#
# print(li[2])
# 34
#
# print(li[3])
# [23, 45, ['Java', 'Python']]
#
# print(li[3][1])
# 45
#
# print(li[3][2])
# ['Java', 'Python']
#
# print(li[3][2][1])
# Python

# list = [1,2,3,4,5,6,7,8]
# print(list)
# list.insert(4,100)
# print(list)

# list = [1,2,3,4,5,6,7,8]
# print(list)
# list.remove(3)
# print(list)
# n=list.pop(3)
# print(n)
# print(list)

# list = [1,2,3,4,5,6,7,8]
# print(list)
# list.clear()
# print(list)

# list = [100,122,3,49,512,61,-7,28]
# print(list)
# n=list.copy()
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.copy()
# print(list)
# print(n)

# fruits =['apple', 'orange', 'kiwi', 'coconut','coconut', 'papaya']
# print(fruits.count('coconut')) # Finds the occurance of the elements in a list

# print(fruits.index('kiwi')) # finds the index of a given element in a list
# fruits.reverse() #reverses the whole list
# fruits.append('grape') #Adds the given element to the end of the list
# fruits.sort() #Sorts the given list in ascending order
# print(fruits)

# stack = [4, 6, 8]
# stack.append(10)
# print(stack)
#
# stack.pop()
#
# print(stack)

# from collections import deque
# # queue = [1, 2, 3, 4, 5, 6]
# queue = deque(["Aman", "Anam","Mana"])
# print(queue)
# queue.append("Shivam")
# queue.appendleft('Sam')
# queue.pop()
# queue.popleft()
# print(queue.__contains__('Mana'))
# print(queue)

# squares = []
# for i in range(21):
#     squares.append(i**2)
# print('Squares: ',squares)
#
# cubes = [x**3 for x in range(21)]
# print('Cubes: ',cubes)
#
# print([(x,y) for x in [1, 2, 3] for y in [4,5,3] if x!=y])
# print([(x,y,x) for x in [1, 2, 3] for y in [4,5,3] if x!=y])
# print([((x,y),x**y) for x in [1, 2, 3] for y in [4,5,3] if x!=y])


list = []
print('Initial Empty List')
print(list)

list.append(1)
list.append(2)
list.append(3)
print('New List after appending single digits')
print(list)

for i in range(1, 5):
    list.append(i)
print('New List after for loop ')
print(list)

list.append((5,6))
print('list after adding a tuple')
print(list)

list2=['Pratiyush', 'Pathak']
list.append(list2)

print('list after concatenating other list')
print(list)

print(list[7][1])
print(list[8])
