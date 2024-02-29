
print('<----------------------Filter----------------------->')

scores = [45, 76, 98, 32, 90, 23, 100, 53]

def passed(score):
    return score>75
over_75 = list(filter(passed, scores))
print('The student who passed are:',over_75)

words = ['rat', 'sheep', 'madam', 'demigod', 'naman','anutforajaroftuna']

palindromes = list(filter(lambda word : word == word[::-1], words))
print('The palindromes in',words,'are:',palindromes)

