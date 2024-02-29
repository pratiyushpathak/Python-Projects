
def add_user(collection):
    while True:
        try:
            print('==========Add Users===========')
            print('1. Insert 1 user')
            print('2. Inser Multiple Users')
            print('3. Go Back')
            print('==================================')

            choice = int(input('Enter your CHOICE: '))

            print('==================================')
            match choice:
                case 1:
                    try:
                        id = int(input('Enter ID: '))
                        f_name = input('Enter First name: ')
                        l_name = input('Enter Last name: ')
                        email = input('Enter Email: ')
                    except:
                        print('enter a valid numeric id')
                        continue

                    record = {
                        '_id':id,
                        'firstName': f_name,
                        'lastName': l_name,
                        'email': email
                    }
                    collection.insert_one(record)
                    print('employee ',id, 'details inserted')

                case 2:
                    n = int(input('Enter the number of users: '))
                    l = []
                    for i in range(n):
                        id = input('Enter ID: ')
                        f_name = input('Enter First name: ')
                        l_name = input('Enter Last name: ')
                        email = input('Enter Email: ')

                        record = {
                            '_id': id,
                            'firstName': f_name,
                            'lastName': l_name,
                            'email': email
                        }

                        l.append(record)
                    collection.insert_many(l)
                    print('All the users have been added to database')

                case 3:
                    break
        except:
            print('Enter a valid numeric value')