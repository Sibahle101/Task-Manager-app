
# The project is created to help a small business manage tasks assigned to each member of the team,
# it works with 2 text files. User.txt and Task.txt
# The User.text already has the default user with username, 'admin' and password, 'adm1n' you can use these credentials to test the program.


# Login process using username and password


print("\nWelcome to task manager")

username = ""
password = ""
login = False

    

# Executes login process until correct credentials are entered

while login == False:
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_details = username + ", " + password
    

# Loops through each line to verify credentials
    
    with open("user.txt","r") as f:
        
        for line in f:

           line = line.strip()

           if line == login_details and username == "admin":
                login = True
       

                if login == True:
                    access_granted = input("\nPlease select one of the following options: \nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ne - exit \ns - display statistics\n")
                    
# For non-admin users function to register new user and statistics is removed            
      
           elif line == login_details and username != "admin":
               login = True
            
               if login == True:
                   access_granted = input("\nPlease select one of the following options: \na - add task \nva - view all tasks \nvm - view my tasks \ne - exit\n")
        
    
    if login == False:
        print("Incorrect details, please check your username or password and try again")        


# Requires new user to register

if access_granted == "r":
    
    file = open("user.txt", "a+")

    new_user_username = input("\nEnter new username: ")
    new_user_password = input("Enter new password: ")
    confirm_password = input("Confirm the password: ")


    # Adds new users

    if new_user_password == confirm_password:
        file.write("\n" + new_user_username + ", " + new_user_password)
        
        print("\nYou have successfully registered.")


    else:
        print("Password does not match")


    file.close()



# Adds new tasks using user's input in appropriate format    

from datetime import datetime


if access_granted == "a":

    file = open("tasks.txt", "a+")
    
    user_resp = input("\nEnter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_descrip = input("Enter description of the task: ")
    task_due_date = input("Enter due date of the task: ")


    # Datetime function is used to set starting date of a new task as a current date
    
    now = datetime.now()
    now = now.strftime("%d %B %Y")

    
    file.write("\n" + user_resp + ", " + task_title + ", " + task_descrip + ", " + now + ", " + task_due_date + ", No")
    
    print("\nNew task has been assigned to the user.")
    
    file.close()


# Accesses tasks.txt to extract information about tasks in easy to read format    

elif access_granted == "va":

    with open("tasks.txt", "r+") as f:

        for line in f:

            # lines in tasks.txt file are split to access required information

            a,b,c,d,e,f = line.split(", ")

            print("")
            print("User responsible          - " + a)
            print("Title of the task         - " + b)
            print("Description of the task   - " + c)
            print("Assignment date           - " + d)
            print("Due date                  - " + e)
            print("Has been completed        - " + f)




# Program displays only tasks assigned to the user that is currently logged in            

elif access_granted == "vm":

    with open("tasks.txt", "r+") as f:

        for line in f:

            # Splits lines to access required information and displays in appropriate format
            
            a,b,c,d,e,f = line.split(", ")

            # Displays information related to current user

            if a == username:
                print("")
                print("Title of the task         - " + b)
                print("Description of the task   - " + c)
                print("Assignment date           - " + d)
                print("Due date                  - " + e)
                print("Has been completed        - " + f)


elif  access_granted == "e":
    print("Thank you for using task manager, Goodbye")


# Shows statistics of all tasks and users in easy to read format
                
elif access_granted == "s":



    
    with open("tasks.txt", "r+") as f:

        # Loops through each line and creates 2 lists, number of users and number of tasks

        users, tasks = [], []

        for line in f:

            # splits line to extract only first 2 elements
            
            line = line.split(", ")

            user = line[0]
            task = line[1]

            # adds element count to the appropriate list

            users.append(user)
            tasks.append(task)
    

        # Set if function is used to avoid duplicates in the lists to return true value
            
        print("\nTotal number of users:  {}".format(len(list(set(users)))))
        print("Total number of tasks:  {}".format(len(list(set(tasks)))))


        # References
# Retrieved  17 February 2021, to check a username and password from a text file.
# https://stackoverflow.com/questions/52337934/checking-a-username-and-password-from-a-text-file/52337976

# Retrieved 17 February 2021, To check ways to remove duplicates. 
# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/

# Retrieved 01 March 2021, For Strftime(Format) DateTime, TimeDelta. 
# https://www.guru99.com/date-time-and-datetime-classes-in-python.html


              











      
        

 

        
