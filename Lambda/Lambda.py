
import functools

str1 ='HelloBeautifulWorld'

upper = lambda string: string.upper()
print(upper(str1))

animals = ['dog', 'cat', 'cow', 'lion', 'chneetah']

upper_animals = list(map(lambda animal: animal.upper(), animals))
print(upper_animals)

li = [5, 6, 7, 8, 9]
sum = functools.reduce((lambda x,y: x+y), li)
diff = functools.reduce((lambda x,y : x-y if x>y else y-x), li)
mul = functools.reduce((lambda x, y:x*y), li)
max = functools.reduce((lambda x, y: x if x>y else y), li)
print('Sum: ',sum)
print('Difference: ',diff)
print('Product: ',mul)
print('The Largest number in the list is: ',max)