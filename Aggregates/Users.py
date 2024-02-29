from ConnectDb import formCollection

tablename = 'Workers'
collection = formCollection(tablename)

record = [
    {
    'id' : 1,
    'first_name' : 'Pratiyush',
    'last_name' : 'Pathak',
    'email' : 'pratiyush@gmail.com',
    'city' : 'Gaya',
    'job_id':1,
    'sal_id':1
    },

{
    'id' : 2,
    'first_name' : 'Shivam',
    'last_name' : 'Kumar',
    'email' : 'shivam@gmail.com',
    'city' : 'Ujjain',
    'job_id':2,
    'sal_id':2
    },
{
    'id' : 3,
    'first_name' : 'Sam',
    'last_name' : 'Kumbhar',
    'email' : 'samruddha@gmail.com',
    'city' : 'Pune',
    'job_id':3,
    'sal_id':3
    },
{
    'id' : 4,
    'first_name' : 'Ayush',
    'last_name' : 'Shrivastava',
    'email' : 'ayush@gmail.com',
    'city' : 'Delhi',
    'job_id':1,
    'sal_id':1
    },
{
    'id' : 5,
    'first_name' : 'Prashant',
    'last_name' : 'Patel',
    'email' : 'prashant@gmail.com',
    'city' : 'Gaya',
    'job_id':2,
    'sal_id':2
    },
{
    'id' : 6,
    'first_name' : 'Rushabh',
    'last_name' : 'Shete',
    'email' : 'rushabh@gmail.com',
    'city' : 'Latur',
    'job_id':3,
    'sal_id':3
    },
{
    'id' : 7,
    'first_name' : 'Shreys',
    'last_name' : 'Jha',
    'email' : 'shreyash@gmail.com',
    'city' : 'Navi Mumbai',
    'job_id':3,
    'sal_id':3
    },
{
    'id' : 8,
    'first_name' : 'Akshay',
    'last_name' : 'Kapse',
    'email' : 'akshay@gmail.com',
    'city' : 'Latur',
    'job_id':3,
    'sal_id':3
    },
{
    'id' : 9,
    'first_name' : 'Akshay',
    'last_name' : 'Tiwari',
    'email' : 'akshayt@gmail.com',
    'city' : 'Indore',
    'job_id':2,
    'sal_id':2
    },
{
    'id' : 10,
    'first_name' : 'Shivam',
    'last_name' : 'Mishra',
    'email' : 'shivammishra@gmail.com',
    'city' : 'Muzaffarpur',
    'job_id':2,
    'sal_id':2
}
]

collection.insert_many(record)


