from ConnectDb import formCollection

workers = formCollection('Workers')
jobs = formCollection('jobs')

pipeline = [
    {
        '$lookup':{
            'from':'jobs',
            'localField':'job_id',
            'foreignField':'job_id',
            'as':'job_info'
        }
    },
    {
        '$unwind':'$job_info'
    },
{
        '$lookup':{
            'from':'salary',
            'localField':'sal_id',
            'foreignField':'sal_id',
            'as':'sal_info'
        }
    },
    {
        '$unwind':'$sal_info'
    },

    {
        '$project':{
            'id':0,
            'id': 1 ,
            'first_name':1,
            'last_name':1,
            'email':1,
            'city':1,
            'job_id':1,
            'job_name':'$job_info.job_name',
            'salary':'$sal_info.salary'
        }
    }
]

result = workers.aggregate(pipeline)

for doc in result:
    print(doc)
