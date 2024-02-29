print('<---------------------DICTIONARIES IN PYTHON--------------------->')

tel = {'Hello':12223, 'World':232232}
print(tel)
tel['Beautiful']=990099
print(tel)
del tel['World']
print(tel)
tel['Mountains']=990099
print(tel)
print('Mountains' in tel)
print('Hello' not in tel)

print('\nUsing the "dict()" constructor')
newDict=dict([('Name',10),('Email',12),('Eid',13)])
print(newDict)

dict2 = {x: x**2 for x in(2, 4, 6)}
print(dict2)

dict3 = dict(shape=123, size=234, rectangle=4)
print(dict3)

print('\nLOOPING TECHNIQUES')
Shapes = {'Circles':'No Sides','Rectangles':'4sides','Triangles':'3 Sides'}
for k, v in Shapes.items():
    print(k,v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

questions=['name','address','mobile']
answers=['Pratiyush','Pune',7903078432]

for q, a in zip(questions, answers):
    print('What is Your {0}? It is {1}'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'guava', 'orange', 'coconut', 'iceapple', 'kiwi']
for i in sorted(basket):
    print(i)
