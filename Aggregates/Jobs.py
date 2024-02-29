from ConnectDb import formCollection

tablename = 'jobs'
collection = formCollection(tablename)

record = [
    {
    'job_id':1,
    'job_name':'Manager'
    },

{
    'job_id':2,
    'job_name':'Admin'
    },
{
    'job_id':3,
    'job_name':'Engineer'
    }
]

collection.insert_many(record)


