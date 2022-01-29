import mysql.connector 
from datetime import datetime

from funcs import *

# CONNECTION
db = mysql.connector.connect(host="localhost",
                            user=usern,
                            passwd=pwd,
                            database="Librarios",
                            auth_plugin = "mysql_native_password"
                            )

mycursor=db.cursor()

# CREATING ENVIRONMENT

mycursor.execute("CREATE DATABASE IF NOT EXISTS Librarios")

mycursor.execute("CREATE TABLE IF NOT EXISTS library (id int PRIMARY KEY AUTO_INCREMENT,"
                "issued_on datetime NOT NULL, name varchar(40), book varchar(50), phone_no int(15) UNSIGNED )")

if db.is_connected():
    print("\nConnected to database successfully...")

else:
    print("\nCouldn't connect to database, Try again...")

greet()

def men():
    inp=input("\nEnter 'm' for menu or press enter to exit program : ")
    if inp.lower() == 'm':
        gen()
    else:
        exit()

# MAIN FUNCTION

def gen():
    act = input('''

---------------------------MENU------------------------------

Enter the number corresponding to action you want to perform :

    \n1. To create an entry
    \n2. To view entries
    \n3. To edit any entry
    \n4. To delete any entry
    \n0. To exit the program
    
 ---> ''')

    # Adding values

    if act == '1':
        name = getn()
        book = getb()
        ph_no = getp()
        mycursor.execute(val_entry,(datetime.now(), name, book, ph_no))
        db.commit()
        print("\nEntries added ! ")
        men()

    # Viewing saved data
         
    elif act == '2':
        mycursor.execute(sel_all)
        for row in mycursor:
            print("\n---------------------------------\n          Id : ",row[0], "\n   Issued on : ",row[1], "\n        Name : ",row[2], "\n        Book : ",row[3], "\nPhone Number : ",row[4] )
        opt=input('''\nEnter 'p' to view phone number of person 
                     \nEnter 'b' to view book issued to person
\n ---> ''')

        if opt.lower( ) == 'p':
            choicn=input("\nEnter name of person you wanna view phone number of : ")
            mycursor.execute(f'''SELECT EXISTS(SELECT * FROM library WHERE name="{choicn}")''')
            for x in mycursor:               
                if x == (0,):
                    print("\nTry entering a valid name...\n")
                    exit()
                else:
                    pass
            mycursor.execute(sel_phno%(choicn))
            for x in mycursor:
                print(f'\nThe phone number of {choicn} is : ',x[0])
                men()
        
        elif opt.lower() == 'b':
            choicn=input("\nEnter name of person you wanna view book of : ")
            mycursor.execute(f'''SELECT EXISTS(SELECT * FROM library WHERE name="{choicn}")''')
            for x in mycursor:               
                if x == (0,):
                    print("\nTry entering a valid name...\n")
                    exit()
                else:
                    pass
            mycursor.execute(sel_book%(choicn))
            for x in mycursor:
                print(f'The book issued to {choicn} is : ',x[0])
                men()
        else:
            men()   
         
    # Editing entered data

    elif act == '3':
        opt=input('''\nEnter 'p' to edit phone number of person 
                     \nEnter 'b' to edit book issued to person 
\n ---> ''') 
        if opt.lower() == 'p':
            choicn=input("\nEnter name of person you wanna edit phone number of : ")
            mycursor.execute(f'''SELECT EXISTS(SELECT * FROM library WHERE name="{choicn}")''')
            for x in mycursor:               
                if x == (0,):
                    print("\nTry entering a valid name...\n")
                    exit()
                else:
                    pass
            phno=input("\nEnter the new phone number : ")
            mycursor.execute(updt_phno%(phno,choicn))
            db.commit()
            print("\nChanges saved succesfully ! \n")
            men()


        elif opt.lower() == 'b':
            choicn=input("\nEnter name of person you wanna edit book issued to : ")
            mycursor.execute(f'''SELECT EXISTS(SELECT * FROM library WHERE name="{choicn}")''')
            for x in mycursor:               
                if x == (0,):
                    print("\nTry entering a valid name...\n")
                    exit()                   
                else:
                    pass
            book=input("\nEnter the new book's name : ")
            mycursor.execute(updt_book%(book,choicn))
            db.commit()
            print("\nChanges saved succesfully ! \n")
            men()
        else:
            men()     
    
    # Deleting data

    elif act == '4':
        choicn=input('\nEnter name of person you wanna delete entry of : ')
        mycursor.execute(f'''SELECT EXISTS(SELECT * FROM library WHERE name="{choicn}")''')
        for x in mycursor:               
            if x == (0,):
                print("\nTry entering a valid name...\n")
                exit()
            else:
                pass
        mycursor.execute("DELETE FROM library WHERE name='%s'"%(choicn))
        print("\nEntry deleted successfully ! \n")
        men()
    
    # Exiting program

    elif act == '0':
        exit()

    else:
        print("\nTry entering a value from above...\n")
        men()


gen()

# Hope you enjoyed my Library Managment Program

    









        


 













    



 






       






















    







    
