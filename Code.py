"""
    Some standard imports required for program
"""
import os
import json
import time
import sys
from datetime import datetime


def create(key,value,timeout=0):
    """
        This function is use to add the data in database
    """
    write_path = 'file.json'
    person_dict = dict()

    try:
        with open(write_path,'r') as json_file:
            data = json.load(json_file)
            print(data)


        for i in list(data):
            print(i)
            if i == key :
                print("error : Key already exist")
                break
            
            else:
                with open(write_path,'w') as json_file:
                    data[key] = value
                    print("the item1 have been created")
                    json.dump(data,json_file)
                    file_size=sys.getsizeof(data)
                
                    if(file_size > 1073741824):
                        print("file size is over limit")
                    else:
                        pass
                    


    except Exception as e:
        print (e)
        with open(write_path, 'w') as json_file: ## if file not exist this line create new file
            person_dict[key] = value
            print("the item have been created")
            json.dump(person_dict, json_file)


def read(key):
    """
        This function is use to read the data from the database
    """
    write_path = 'file.json'

    with open(write_path) as f:
        data = json.load(f)

    for i in list(data):
        if i == key :
            print('{'+f'{key} : {data[key]}'+'}')
            break
    else:
        print('Key does not exist')


def delete(key):
    """
        This function is use to delete the data from database
    """
    write_path = 'file.json'

    with open(write_path) as f:
        data = json.load(f)

    for i in list(data):
        if i == key : 
            with open(write_path,'w') as json_file:
                data.pop(key)
                print("The Item is removed")
                json.dump(data,json_file)
            break
    else:
        print('Key does not exist')



"""
    Main program start from here
"""

while(1):

    if __name__ == "__main__":
        print("1 CREATE")
        print("2 READ")
        print("3 DELETE")
        print("4 Quit")

        users_choice = int(input("Enter Your Choice : "))

        if users_choice == 1:
            key = input("Enter key for input : ")
            value = input("Enter the values corresponding to key : ")
            create(key,value)
        elif users_choice == 2:
            key = input("Enter key for input : ")
            read(key)
        elif users_choice == 3:
            key = input("Enter key for input : ")
            delete(key)
        elif users_choice==4:
            quit()
        else:
            print("Invalid option")




