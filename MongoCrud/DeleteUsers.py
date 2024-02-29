
def delete_user(collection):
    while True:
        try:
            print('==========Delete Users===========')
            print('1. Delete 1 User')
            print('2. Delete Multiple users')
            print('3. Go Back')
            print('==================================')

            choice = int(input('Enter Your CHOICE: '))

            print('==================================')

            match choice:
                case 1:
                    try:
                        id = input('Enter the id you want to delete: ')
                        query = {'_id': id}
                        collection.delete_one(query)
                        print('User with id ', id, 'Deleted from database')
                    except:
                        print('Enter a valid numeric value')
                        continue

                case 2:
                    try:
                        n = int(input('Enter the number of users: '))
                        l=[]
                        for i in range(n):
                            id = input('Enter the id you want to delete: ' )
                            l.append(id)
                            query = {'_id': id}
                            collection.delete_one(query)
                        print('User with ids ', l, 'Deleted from database')
                    except:
                        print('Enter a valid numeric value')
                        continue

                case 3:
                    break
        except:
            print('Enter a valid Numeric Value')
