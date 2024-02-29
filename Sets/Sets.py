# a = {'Name', 'Roll', 'Marks'}
# type(a)

# myset = set(['a', 'b', 'c'])
# myset = {'a', 'b', 'c'}
# print(myset)
#
#
# myset.add('d')
# print(myset)

# myset[1]='Admin'
# print(myset)
# TypeError: 'set' object does not support item assignment

# myset = {'a', 1,4,'b','Pratiyush',True}
# print(myset)

# Sets in pythion can store hetrogenous elements

# odd_square = [x**2 for x in range(1,20) if x%2 !=0]
# print(odd_square)

#Slicing in lists

# List = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
# print('initial list')
# print(List)
#
# sliced_list = List[:-6]
# print('\nElements sliced till 6th element from last: ')
# print(sliced_list)
#
# sliced_list1 =List[-6:-1]
# print('\nElements sliced from index -6(included) to -1(Not Included)')
# print(sliced_list1)
#
# sliced_list2 = List[::-1]
# print('\nPrinting the list in reverse order:')
# print(sliced_list2)

# List = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
# print('initial list')
# print(List)
#
# sliced_list = List[6:]
# print('\nElements sliced from 6th element till last: ')
# print(sliced_list)
#
# sliced_list1 =List[1:6]
# print('\nElements sliced from index 1(included) to -6(Not Included)')
# print(sliced_list1)
#
# sliced_list2 = List[:]
# print('\nPrinting the list:')
# print(sliced_list2)

# normal_set = set(['a', 'b', 'c'])
# print('\nNormal Set')
# print(normal_set)
#
# frozen_set = frozenset(['e', 'f', 'g'])
# print('\nFrozen Set')
# print(frozen_set)
#
# frozen_set.add('n') #AttributeError: 'frozenset' object has no attribute 'add'

