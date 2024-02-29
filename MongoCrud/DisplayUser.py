
def show_users(collection):

    while True:
        try:
            print('==========Display Users===========')
            print('1. Display single user by userId')
            print('2. Display All Users')
            print('3. Display name and email')
            print('Display with filter')
            print('5. Go Back')
            print('==================================')

            choice = int(input('Enter your choice: '))

            print('==================================')

            match choice:
                case 1:
                    try:
                        try:
                            id = int(input('Enter the user id: '))
                        except:
                            print('Enter a valid id')
                            continue
                        query = {'_id': id}
                        print(collection.find_one(query))
                    except:
                        print('User Not Found')
                case 2:
                    result = collection.find()
                    for i in result:
                        print(i)

                case 3:
                    for i in collection.find({}, {'firstName':1, 'email': 1}):
                        print(i)
                case 4:
                    name = input('enter the First Name of user: ')
                    result = collection.find({'firstName' : {'$eq':name}})
                    for i in result:
                        print(i)
                case 5:
                    break
        except:
            print('Enter a valid numeric value')