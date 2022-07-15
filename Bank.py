import os
from datetime import date,timedelta
import datetime
import re
import random

def loanCalculator():
    correct = True
    while correct:
        print("1.Education loan\n2.Personal loan\n3.Car loan\n4.Home loan")
        ch = int(input("Enter which loan type you wan to calculate: "))
        loanAmount = int(input("Enter the desired loan amount(with RM as unit): "))
        loanperiod = int(input("Enter the desired loan period with year unit: "))
        loanmontlypay = loanperiod*12
        if ch == 1:
            ELmonthlyPayment = loanAmount*1.75/loanmontlypay
            print("The montly amount that should pay is",ELmonthlyPayment)
            return 1,ELmonthlyPayment,loanperiod
        elif ch == 2:
            PLmonthlyPayment = loanAmount*0.08/loanmontlypay
            print("The montly amount that should pay is",PLmonthlyPayment)
            return 2,PLmonthlyPayment,loanperiod
        elif ch == 3:
            CLmonthlyPayment = loanAmount*0.04/loanmontlypay
            print("The montly amount that should pay is",CLmonthlyPayment)
            return 3,CLmonthlyPayment,loanperiod
        elif ch == 4:
            HLmonthlyPayment = loanAmount*0.0425/loanmontlypay
            print("The montly amount that should pay is",HLmonthlyPayment)
            return 4,HLmonthlyPayment,loanperiod


def registration():
    name = str(input("Enter the account holder name: "))
    userid = str(input("Enter a unique user id with 4 digit number: "))
    totalamount = str(input("Enter the loan amount: "))
    instalmentamount = int(input("Enter your instalment amount: "))
    birthdate = str(input("Enter your birthday: "))
    password = str(input("Enter a new password: "))
    gender = str(input("Write your gender Male/Female/Better not to tell: "))
    contact_num = str(input("Enter your contact number: "))
    home_address= str(input("Enter your home address: "))
    with open('customers_information.txt','a')as file:
        value1,value2,loanperiod = loanCalculator()
        value2 = str(value2)
        loanperiod = str(loanperiod)
        if value1 == 1:
            file.write("\nEducationLoan"+ ",")
            file.write(value2 + "," + loanperiod +",") #value1 = ch,return value2 = variable
        elif value1 == 2:
            file.write("\nPersonalLoan"+ ",")
            file.write(value2 + "," + loanperiod +",")
        elif value1 == 3:
            file.write("\nCarLoan"+ ",")
            file.write(value2 + "," + loanperiod +",")
        elif value1 == 4:
            file.write("\nHomeLoan"+ ",")
            file.write(value2 + "," + loanperiod +",")
        file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(name,userid,totalamount,instalmentamount,birthdate,password,gender,contact_num,home_address))
        print("\nRequest Sent to Admin")

'''
def viewRegistration():
    ch = int(input("Press 1 to view new customer's registration request,2 to return to menu: "))
    if ch == 1:
        print("*****CUSTOMERS INFORMATION****")
        with open('customers_information.txt','r') as f:
            print(f.read())
    else:
        admin()
'''       

def checkOverdue(user_id):
    today = date.today()
    today = str(today)
    with open('loandetails.txt','r')as f5:
        for line in f5.readlines():
            line = line.split(" ")
            if user_id == line[2]:
                duedate = line[6]
                overtime = duedate + today
                if str(overtime) < str(duedate):
                    return 'o'

def payloan(user_id):
    today = date.today()
    today = str(today)
    print("Loan Amount")
    with open ('registered_customers.txt','r')as file:
        for lines in file.readlines():
            typelist = lines.split(',')
            if user_id == typelist[3]:
                loanType1 = typelist[0]  
                loanAmount = typelist[1] 
                print(loanAmount)
                ch = int(input('Press 1 to pay the loan:\nPress 2 to exit: '))
                if ch == 1:
                    pay = int(input("How much do you wan to pay? "))
                    loanAmount = float(loanAmount)
                    transaction = loanAmount - pay
                    transaction = str(transaction)
                    pay = str(pay)
                    with open("alltransact.txt",'a')as file:
                        checkduedate = checkOverdue(user_id)
                        if checkduedate == 'o':
                            print('Instalment is overdue!')
                        else:
                            line = ("\n" + user_id + " " + transaction+ " " + pay + " " + loanType1 + " " + today) 
                            file.write(line)
                            print("Thank you for payment!\n")
                            replace = open ('replacement.txt','a')
                            olddata = open('registered_customers.txt','r')
                            o_data = olddata.read()
                            replace.writelines(o_data)
                            replace.close()
                            with open('replacement.txt','r+') as previous:
                                for line in previous.readlines():
                                    line = line.split(',')
                                    if user_id == line[3]:
                                        newamount = re.sub(line[1], str(transaction) , o_data)
                            new = open ('registered_customers.txt' , 'w')
                            new.write(newamount)
                            new.close()
                            os.remove('replacement.txt')
                else:
                    registeredcustomer(user_id)
                        
                

def checkloandetails(user_id):
    with open('loandetails.txt','r') as file:
        for line in file.readlines():
            line = line.split(' ')
            if user_id == line[2]:
                print(line)

                        
def viewownTransaction(user_id):
    ch = int(input('Press 1 to view own transaction. '))
    if ch == 1:
        with open("alltransact.txt","r")as file:
            for line in file.readlines():
                line = line.split(" ")
                if user_id == line[0]:
                    print("Payment"+ " " + 'RM' + line[2] + " " + "Date" + " " + line[4])

def viewspecificTransaction():
    with open('registered_customers.txt','r')as file:
        for line in file.readlines():
            line = line.split(',')
            print(line[3])
        ch = str(input("Enter the name of the user to view his transaction: "))
        with open('alltransact.txt','r')as f1:
            for line1 in f1.readlines():
                line1 = line1.split(" ")
                if ch == line1[0]:
                    print("Transaction" + " " + 'RM' + line1[2] + " " + "Date" + line1[4])


def viewloantypeTransaction():
    with open('alltransact.txt','r')as file:
        ch = str(input("Enter the loan type to show its transaction,EducationLoan/PersonalLoan/CarLoan/HomeLoan with same letter: "))
        for line in file:
            line = line.rstrip()
            if ch in line:
                print(line + '\n')

def viewallTransaction():
    with open('alltransact.txt','r')as file:
        for line in file.readlines():
            line = line.split(" ")
            print(line)

def viewallloantypeTransaction():        
    with open('alltransact.txt','r')as file:
        for line in file.readlines():
            line = line.split(" ")
            print("RM" + line[2] + " " + line[3])

def checkownStatus(user_id):
    ch = int(input('Press 1 to check loan status. '))
    if ch == 1:
        with open("loandetails.txt","r")as file:
            for line in file.readlines():
                line = line.split(" ")
                if user_id == line[2]:
                    print("LoanID\tDueDate")
                    print(line[5] + "\t" + line[6])

def checkloanuserexists(username):
    userData1 = []
    data1 = open("loandetails.txt",'r')
    for line1 in data1:
        temporaryList1 = line1.split(" ")
        userData1.append(temporaryList1)
    for i in range(len(userData1)):
        if str(userData1[i][2]) == username:
            return 'f'


def provider():
    today = date.today()
    duedate = today + timedelta(days = 30)
    today = str(today)
    duedate = str(duedate)
    loanid = random.randint(0,9999)
    with open('registered_customers.txt','r')as data:
        for line in data.readlines():
            line = line.split(",")
            installmentamount = line[4]
            print(line[3] + " " + "LoanAmount" + " " + line[5] + " " + "Loan Type" + " " + line[0] + " " + "LoanPeriod(Y)" + " " + line[2])
        username = input("Enter the name to provide loan id,payment,instalmentamount, duedate: ")
        checkexists = checkloanuserexists(username)
        if checkexists != 'f':
            with open('loandetails.txt','a')as f1:
                f1.write('\n'+today + " ")
                value1,value2,loanperiod = loanCalculator()
                value2 = str(value2)
                loanperiod = str(loanperiod)
                if value1 == 1:
                    f1.write("EducationLoan"+ " ")
                    f1.write(username + " " + "RM" + value2 + " " + "RM" + installmentamount + " " + str(loanid) + " " + duedate  + " " + "PayInTime" + " " + loanperiod) #value1 = ch,return value2 = variable
                elif value1 == 2:
                    f1.write("PersonalLoan"+ " ")
                    f1.write(username + " " + "RM" + value2 + " " + "RM" + installmentamount + " " + str(loanid)+ " " + duedate + " " + "PayInTime" + " " + loanperiod)
                elif value1 == 3:
                    f1.write("CarLoan"+ " ")
                    f1.write(username + " " + "RM" + value2 + " " + "RM" + installmentamount + " " + str(loanid)+ " " + duedate + " " + "PayInTime" + " " + loanperiod)
                elif value1 == 4:
                    f1.write("HomeLoan"+ " ")
                    f1.write(username + " " + "RM" + value2 + " " + "RM" + installmentamount + " " + str(loanid)+ " " + duedate + " " + "PayInTime"+ " " + loanperiod)
        else:
            print('User loan is already provided')




def checkuserexists():
    userid = []
    ids = []
    data = open("registered_customers.txt",'r')
    for line1 in data:
        line2 = line1.split(',')
        userid.append(line2[4])
    data.close()
    with open('customers_information.txt','r')as data:
        for line in data.readlines():
            line = line.split(",")
            ids.append(line[4])
    found = [x for x in userid + ids if x not in ids or x not in userid]
    return found
    

 

def approve():     
    with open('customers_information.txt','r')as data:
        print("UserIDnumber\tUsername")
        for line in data.readlines():
            line2 = line
            line = line.split(",")
            checkuserin = checkuserexists()
            for x in checkuserin:
                if x == line[4]:
                    print(line[4] + "\t\t" + line[3])
    ch = str(input("Enter the UserIDnumber to approve,Press 2 to return: "))
    with open('customers_information.txt','r')as data1:
        for line1 in data1.readlines():
            line2 = line1
            line1 = line1.split(",")
            if ch == line1[4]:
                with open('registered_customers.txt','a+')as f1:
                    f1.write("\n%s"%(line2))
                    print('User approved!')
                
                        #else:
                        # print('user is already approved')
                    

            


        


def registeredcustomer(user_id):
    MakeLoop = True
    while MakeLoop:
        print("*****WELCOME Registered Customer*****")
        ch = int(input("\nEnter 1 to check loan details\nEnter 2 to pay the loan\nEnter 3 to view own transaction\nEnter 4 to check loan status\nEnter 5 to exit: "))
        if ch == 1:
            checkloandetails(user_id)
        elif ch == 2:
            payloan(user_id)
        elif ch == 3:
            viewownTransaction(user_id)
        elif ch == 4:
            checkownStatus(user_id)
        else:
            MakeLoop = False




def checkUsercode(user_id,password):    #id and password
    data = open("adminfile.txt",'r')
    userData = []
    for line in data.readlines():
        line = line.split(' ')
        #temporaryList = line.split()
        #userData.append(temporaryList)
    for i in range(len(line)): 
        if str(line[0]) == user_id and str(line[1]) == password:
            return 'a'
    userData1 = []
    data1 = open("registered_customers.txt",'r')
    for line1 in data1:
        temporaryList1 = line1.split(",")
        userData1.append(temporaryList1)
    for i in range(len(userData1)):
        if str(userData1[i][3]) == user_id and str(userData1[i][8]) == password:
            return 'r'
    


def admin():
    MakeLoop = True
    while MakeLoop:
        print("*****WELCOME ADMIN*****")
        ch = int(input("1.View customers registration request.\n2.Provide Loan ID, instalment Date and instalment Amount per month to registered customers\n3.View all transactions of specific customer\n4.View specific loan type transaction\n5.View all transaction\n6.View all loan type transaction.\n7.Exit\nEnter the number: "))
        if ch == 1:
            approve()
        elif ch == 2:
            provider()
        elif ch == 3:
            viewspecificTransaction()
        elif ch == 4:
            viewloantypeTransaction()
        elif ch == 5:
            viewallTransaction()
        elif ch == 6:
            viewallloantypeTransaction()
        else:
            MakeLoop = False
            login()

def newcustomers():
    MakeLoop = True
    while MakeLoop:
        ch = int(input("1.Check Loan details\n2.Use loan calculator\n3.Registration\n4.Back to Login menu\n5.Exit\nEnter the number: "))
        if ch == 1:
            ch1 = int(input("1. Education loan\n2. Personal loan\n3. Home loan\n4. Car loan\n5.Back to menu: "))
            if ch1 == 1:
                with open("el.txt",'rb')as f:
                    print(f.read())
            elif ch1 == 2:
                with open("pl.txt",'rb')as f:
                    print(f.read())
            elif ch1 == 3:
                with open("hl.txt",'rb')as f:
                    print(f.read())
            elif ch1 == 4:
                with open("cl.txt",'rb')as f:
                    print(f.read())             
        elif ch == 2:
            loanCalculator()
        elif ch == 3:
            registration()
        elif ch == 4:
            login()
        elif ch == 5:
            print("Thanks for coming Malaysia Bank.")
            MakeLoop = False
        else:
            print("\nPlease enter a correct choice: ")


def login():
    MakeLoop = True
    while MakeLoop:
        print("**********************************")
        print(" ----Welcome to Malaysia Bank----")
        print("==================================")
        print("1.Login\n2. New customers\n3. Exit")
        choice = int(input("Press 1 to Login, Press 2 to new customers section,Press 3 to exit: "))
        if choice == 1:
            user_id = str(input("Enter Login Id: "))
            password = str(input("Enter User Password: "))

            checkUserType = checkUsercode(user_id,password)
            if checkUserType == None:
                print("User id or Password Wrong!")
            else:
                if checkUserType == 'a':
                    admin()
                elif checkUserType == 'r':
                    registeredcustomer(user_id)                
        elif choice == 2:
            newcustomers()
        elif choice == 3:
            print("Thanks for coming to Malaysia Bank.")
            MakeLoop = False
        else:
            print("Please enter a correct choice")

login()

