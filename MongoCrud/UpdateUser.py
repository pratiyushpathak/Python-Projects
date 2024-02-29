
def update_user(collection):

    while True:
        try:
            print('==========Update Users===========')
            print('1. Update Single User')
            print('2. Update Multiple Users')
            print('3. Go Back')
            print('==================================')

            choice = int(input('Enter Your Choice: '))

            print('==================================')

            match choice:
                case 1:
                    try:
                        id = int(input('Enter the id of user to be updated: '))
                    except:
                        print('Invalid Id! Please Try Again')
                        continue
                    query = {'_id': {'$eq':id}}
                    present_data = collection.find_one(query)
                    print('Which Constraint You want to change? ')
                    print('1. First Name')
                    print('2. Last Name')
                    print('3. Email')
                    key = int(input('Enter the constraint to be changed: '))
                    if key == 1 or key == 2 or key == 3:
                            match key:
                                case 1:
                                    new_data = {'$set': {'firstName': value}}
                                case 2:
                                    new_data = {'$set': {'lastName': value}}
                                case 3:
                                    new_data = {'$set': {'email': value}}
                    else:
                            print('Invalid Data')
                            continue
                    value = input('Enter the new value: ')
                    collection.update_one(present_data, new_data)
                    print('Data SuccessFully Updated')
                    print(collection.find_one(query))

                case 2:
                    n = int(input('Enter the number of users to be updated: '))
                    for i in range(n):
                        id = input('Enter the id of user to be updated: ')
                        query = {'_id': {'$eq': id}}
                        present_data = collection.find_one(query)

                        key = int(input('Enter the constraint to be changed: '))
                        if key == 1 or key == 2 or key == 3:
                            match key:
                                case 1:
                                    new_data = {'$set': {'firstName': value}}
                                case 2:
                                    new_data = {'$set': {'lastName': value}}
                                case 3:
                                    new_data = {'$set': {'email': value}}
                        else:
                            print('Invalid Data')
                            continue
                        value = input('Enter the new value: ')
                        collection.update_one(present_data, new_data)
                    print('Data SuccessFully Updated')
                    result = collection.find()
                    for i in result:
                        print(i)
                case 3:
                    break
        except:
            print('Enter a valid numeric value')

