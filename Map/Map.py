
# my_pets = ['Jeremy', 'Shaktiman', 'rapido']
#
# uppered_pets = list(map(str.upper, my_pets))
# print(uppered_pets)

# ['JEREMY', 'SHAKTIMAN', 'RAPIDO']

# numbers = [1.09443, 2.998845, 1.99845, 0.398228, 3.99894, 4.332, 56.99832]
#
# rounded= list(map(round, numbers, range(1,len(numbers)+1)))
# print(rounded)
#
# [1.1, 3.0, 1.998, 0.3982, 3.99894, 4.332]

#zip()-------------------------------------------------

# myStrings = ['a', 'b', 'c', 'd']
# myNum = [1, 2, 3, 4, 5]
#
# tuples = list(zip(myNum,myStrings))
# print(tuples)

# myStrings = ['a', 'b', 'c', 'd']
# myNum = [[1, 2, 3, 4, 5],[6,7,8,9,10]]
#
# tuples = list(zip(*myNum))
# print(tuples)