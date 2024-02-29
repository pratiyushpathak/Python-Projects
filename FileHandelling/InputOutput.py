
import os
import logging


def functionalities(filename, method, type, logger):
        try:
            f = open(filename, method)
            if method=='r':
                task = f.read()
                print(task)
                logger.info('File Read Successfully')

            else:
                if type == 'todolist':
                    print('<==================TodoList in Python==================>')
                    iterate = 1
                    while iterate:
                        task = input('Enter the task[Type close to exit]: ').strip()
                        if task.lower() != 'close':
                            f.write(task + '\n')
                        else:
                            iterate=0
                    logger.info('Todo List added Successfully')

                elif type == 'expenses':
                    print('<==================Expenses in Python==================>')
                    iterate = 1
                    total =0
                    while iterate:
                        task = int(input('Add Expense[Type 0 to exit]: '))
                        total += task
                        if task != 0:
                            f.write(str(task)+'\n')
                        else:
                            iterate = 0
                    f.write(str(total))
                    logger.info('Expenses added Successfully')
                    print('Total:',total)

                else:
                    print('<==================Notes in Python==================>')
                    iterate = 1
                    print('Enter the Data [Write close to exit]')
                    while iterate:
                        task = input().strip()
                        if task.lower() != 'close':
                            f.write(task + '\n')
                        else:
                            iterate = 0
                    logger.info('Notes added Successfully')



        except IOError:
            if method=='r':
                print('Error occured while reading the file')
                logger.error('Error generted wwhile reading file')

            else :
                print('Error occured while writing to the file')
                logger.error('Error generted while writing file')

        finally:
            f.close()
def start():
    os.remove('LoggerFile.log')
    logging.basicConfig(filename='LoggerFile.log', format="%(levelname)s--%(message)s--%(asctime)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")

    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    flag = True

    while flag:
        print('<==================Files in Python==================>')
        print('Select any one:')
        print('1. Read from a file')
        print('2. Write to a File')
        print('3. Show All Files')
        print('4. Delete a File')
        print('5. Rename a file')
        print('6. Exit')

        choice = input()

        match choice:
            case '1':
                file=input('Enter the File Name:').strip()

                if os.path.exists(file):
                    functionalities(file, 'r', 'read', logger)

                else:
                    print('Please Enter a correct file Name\n')
                    print('THE FILE DOESNOT EXIST!!!')
                    logger.error('File Does Not Exist for reading')

            case '2':
                writeFlag= True
                while writeFlag:
                    print('<==================Writing to a File in Python==================>')
                    print('Select any one:')
                    print('1. Todo List')
                    print('2. Expenses')
                    print('3. Notes')
                    # print('4. Delete a File')
                    # print('5. Rename a file')
                    print('4. Exit')

                    choice = input()
                    match choice:
                        case '1':
                            file = input('Enter the Todo File Name:').strip()
                            if os.path.exists(file):
                                functionalities(file, 'a', 'todolist', logger)
                                logger.info('Successfully opened a file to add more data')
                            else:
                                functionalities(file, 'w', 'todolist', logger)
                                logger.warning('New File created and written successfully')

                        case '2':
                            file = input('Enter the Expenses File Name:').strip()
                            if os.path.exists(file):
                                functionalities(file, 'a', 'expenses', logger)
                                logger.info('Successfully opened a file to add more data')
                            else:
                                functionalities(file, 'w', 'expenses', logger)
                                logger.warning('New File created and written successfully')

                        case '3':
                            file = input('Enter the Notes File Name:').strip()
                            if os.path.exists(file):
                                functionalities(file, 'a', 'notes', logger)
                                logger.info('Successfully opened a file to add more data')
                            else:
                                functionalities(file, 'w', 'notes', logger)
                                logger.warning('New File created and written successfully')

                        case '4':
                            writeFlag = False

            case '3':
                path = '/home/pratiyushp/downloads/Codes/PythonWorkspace/pythonProject/FileHandelling'
                list = os.listdir(path)
                print(list)
                logger.info('All Existing file Lists Shown')

            case '4':
                file = input('Enter the File Name:').strip()

                if os.path.exists(file):
                    os.remove(file)
                    logger.info('File deleted Successfully')
                    print('File Deleted Successfully')

                else:
                    logger.error('File Does not exist for deleting')
                    print('File does not exist')

            case '5':
                file = input('Enter the File Name:').strip()

                if os.path.exists(file):
                    input('Enter the new Name: ')
                    newName=input('Re Enter the new Name: ')
                    os.rename(file, newName)
                    print('File Renamed Successfully')
                    logger.info('File Renamed Successfully')

                else:
                    logger.error('File Does not exist for deleting')
                    print('File does not exist')

            case '6':
                logger.debug('Application to close')
                logs = open('LoggerFile.log', 'r')
                task= logs.read()
                print(task)
                logs.close()
                # os.remove('LoggerFile.log')
                flag = False

if __name__ == '__main__':
    start()