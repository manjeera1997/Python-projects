import os
import platform
#making listStd as global variable
global listStd
listStd=["Manju","sarada","shubham","alok"]
def manageStudent():
    x = "#"*30
    y = '='*28
    global bye
    bye = "\n {} \n# {} #\n# ===> Brought To You By <=== #\n# ====> code-projects.org <=== #\n# {} #\n {}".format(x,y,y,x)
    print("""
    
    ------------------------------------------------------------------------------
    |=============================================================================|
    |===============Welcome to Student Management System==========================|
    |=============================================================================|
    ------------------------------------------------------------------------------
    
    Enter 1 : To view Student's List
    Enter 2 : To Add New Student
    Enter 3 : To search Student
    Enter 4 : To Remove Student
    """)

    try:
        userInput = int(input("Please select and above option: "))
    except ValueError:
        print("That's not a number ")
    else:
        print("\n") #print new line
    #checking using option
    if(userInput ==1):
        print("List Students\n")
        for students in listStd:
            print("=> {}".format(students))
    elif(userInput == 2):
        newStd = input("Enter New Student: ")
        if (newStd in listStd):
            print("\nThis student { } already in the database".format(newStd))
        else:
            listStd.append(newStd)
            print("\n New Student {} successfully Added \n".format(newStd))
            for students in listStd:
                print("=>{}".format(students))
    elif(userInput == 3):
        srcStd = input("Enter student name to search: ")
        if(srcStd in listStd):
            print("\n=> Record found of student {}".format(srcStd))
        else:
            print("\n=> No Record found of student {}".format(srcStd))
    elif(userInput == 4):
        rmStd = input("\n Enter student name to Remove: ")
        if(rmStd in listStd):
            listStd.remove(rmStd)
            print("\n=> student {} successfully deleted \n".format(rmStd))
            for students in listStd:
                print("=> {}".format(students))
        else:
            print("\n=> No record found of this student {}".format(rmStd))
    elif(userInput < 1 or userInput >4):
        print("Enter valid option")
manageStudent()

def runAgain():
    runAgn = input("\nwant to run again Y/n: ")
    if(runAgn.lower()=='y'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageStudent()
        runAgain()
    else:
        print("Goodbye")
runAgain()
