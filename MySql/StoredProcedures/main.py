from MySql.StoredProcedures.services.UserServices import UserServices

data = UserServices.get_all("Users")

for r in data:
    print(r)

UserServices.insert_one_my_table('Pratiyush', 22, 'pratiyush@gmail.com')

UserServices.update_age('Pratiyush', 23)

UserServices.pro_call('bikeJOINS')
