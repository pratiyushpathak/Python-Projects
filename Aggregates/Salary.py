from ConnectDb import formCollection

tablename = 'salary'
collection = formCollection(tablename)

record = [
    {
    'sal_id':1,
    'salary':130000
    },

{
    'sal_id':2,
    'salary':100000
    },
{
    'sal_id':3,
    'salary':200000
    }
]

collection.insert_many(record)


