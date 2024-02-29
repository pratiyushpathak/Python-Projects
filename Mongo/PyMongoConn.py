from pymongo import MongoClient

# client = MongoClient()
try:
    client = MongoClient('mongodb://localhost:27017/')
    print('Connected To the Database')
except:
    print('Could Not connect')

db = client.My_Database

collection = db.Customers

record = [
    {
    'id' : 1,
    'first_name' : 'Pratiyush',
    'last_name' : 'Pathak',
    'email' : 'pratiyush@gmail.com',
    'city' : 'Gaya'
    },

{
    'id' : 2,
    'first_name' : 'Shivam',
    'last_name' : 'Kumar',
    'email' : 'shivam@gmail.com',
    'city' : 'Ujjain'
    },
{
    'id' : 3,
    'first_name' : 'Sam',
    'last_name' : 'Kumbhar',
    'email' : 'samruddha@gmail.com',
    'city' : 'Pune'
    },
{
    'id' : 4,
    'first_name' : 'Ayush',
    'last_name' : 'Shrivastava',
    'email' : 'ayush@gmail.com',
    'city' : 'Delhi'
    },
{
    'id' : 5,
    'first_name' : 'Prashant',
    'last_name' : 'Patel',
    'email' : 'prashant@gmail.com',
    'city' : 'Gaya'
    },
{
    'id' : 6,
    'first_name' : 'Rushabh',
    'last_name' : 'Shete',
    'email' : 'rushabh@gmail.com',
    'city' : 'Latur'
    },
{
    'id' : 7,
    'first_name' : 'Shreys',
    'last_name' : 'Jha',
    'email' : 'shreyash@gmail.com',
    'city' : 'Navi Mumbai'
    },
{
    'id' : 8,
    'first_name' : 'Akshay',
    'last_name' : 'Kapse',
    'email' : 'akshay@gmail.com',
    'city' : 'Latur'
    },
{
    'id' : 9,
    'first_name' : 'Akshay',
    'last_name' : 'Tiwari',
    'email' : 'akshayt@gmail.com',
    'city' : 'Indore'
    },
{
    'id' : 10,
    'first_name' : 'Shivam',
    'last_name' : 'Mishra',
    'email' : 'shivammishra@gmail.com',
    'city' : 'Muzaffarpur'
}
]

# collection.insert_many(record)

cursor = collection.find()
# print(type(cursor))
for i in cursor:
    first_name= i['first_name']
    last_name = i['last_name']
    print('Name :',first_name, last_name, '| id :',i['id'] )
    # print(i)