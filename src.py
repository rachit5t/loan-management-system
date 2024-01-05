import os
import random
from datetime import datetime


# this function has menu for new users like loan calculator, loan details and apply ragistration
def new_user():
    #Printing The New User Menu
    print("---------------------")
    print("New user menu ")
    print("---------------------\n")
    print("Choose what to do")
    print("1. Loan Calculator")
    print("2. Loan detais")
    print("3. Apply registration")
    print("4. Exit\n")
    new_user_choose = input("Input ==> ")
    if new_user_choose == "1" :
        #loan Calculator
        print("---------------------")
        print("Loan calculator")
        print("---------------------\n")
        loan_amount = int(input("Type loan amount ==> "))
        years = int(input("In how many years you want to pay loan ==> "))
        annual_intrest = int(input("What is the annual intrest ==> "))
        final_loan = loan_amount + ((annual_intrest * years) / 100) * loan_amount
        monthly_pay = final_loan / (years * 12)
        print("The total Amount You will have to pay in",years,"Years is",final_loan)
        print("You must pay",monthly_pay,"Per month\n")
        any_key = input("Press enter to continue...")
        new_user()

    elif new_user_choose == "2":
        #loan details
        print("---------------------")
        print("New user menu ")
        print("---------------------\n")
        print("These are the loan plan avilable ")
        print("Loan Type\t\tIntrest rate  annually (Simple intrest)")
        print("1. Education Loan (EL)\t5% intreast")
        print("2. Car Loan (CL)\t10% intrest")
        print("3.Home Loan (HL)\t15% intrest") 
        print("4. Personal Loan (PL)\t20% intrest")
        any_key = input("Press enter to continue...")
        new_user()
    elif new_user_choose == "3":
        apply_registration()
    elif new_user_choose == "4":
        main_menu()
    else :
        print("Invalid Input Given !!!!!")
        any_key = input("Press enter to continue...")
        new_user()


















#This functions asks details with user to create account for them.
def apply_registration():
     f = open("User_details.txt","a")
     f.close()
     intrest = "0"
     print("Choose The loan type you want To take")
     print("Loan Type\t\tIntrest rate  annually (Simple intrest)")
     print("1. Education Loan (EL)\t5% intreast")
     print("2. Car Loan (CL)\t10% intrest")
     print("3. Home Loan (HL)\t15% intrest") 
     print("4. Personal Loan (PL)\t20% intrest\n")
     loan_choose = input("Input ==> ")
     if loan_choose == "1":
        intrest = "5"
     elif loan_choose == "2":
        intrest = "10"
     elif loan_choose == "3":
        intrest = "15"
     elif loan_choose == "4":
        intrest = "20"
     else:
        print("Invalid Input Given !!!!!")
        any_key = input("Press enter to continue...")
        apply_registration()
     name = str(input("Type Your name ==> "))
     email = str(input("Type Your Email address ==> "))
     contact = str(input("Type phone number => "))
     gender = str(input("Type Your gender ==> "))
     age = str(input("Type your age ==> "))
     loan = str(input("Enter The loan Amount You want ==> "))
     password = input("Plese Create a password ==> ")
     login_approval = "No"
     #counting lines for generating User id
     count = len(open('User_details.txt').readlines())
     user_id = str(count + 12340000)
     #Setting some details for loan 
     total_pay_with_intrest = "Not_Set_by_admin"
     total_paid_by_user = "0"
     monthly_installment = "Not_Set_by_admin"
     first_installment_date = "Not_set_by_admin"

     #Writing user details in file
     f = open("User_details.txt","a")
     f.write(user_id+" "+name+" "+password+" "+email+" "+contact+" "+gender+" "+age+" "+loan+" "+intrest+" "+login_approval+" "+total_pay_with_intrest+" "+total_paid_by_user+" "+monthly_installment+" "+first_installment_date+"\n")
     f.close()
     print("Your account Is under Review By the admin")
     print("Remember this for login next time...")
     print("User Id ==> ",user_id)
     print("Password ==> ",password)
     any_key = input("Press enter to continue...")
     main_menu()







#This function is for verifying id and pssword for login. The details are read from user_details.txt file.
def User_signin():
    input_id = str(input("Type the id ==> "))
    input_password = str(input("Type The password ==> "))
    #checking for validity of id and password given by user
    f = open("User_details.txt","r")
    for read in f :
        word = read.split()
        if word[0] == input_id and word[2] == input_password:
            if word[9] != "Yes":
                print("You are Not aproved by admin..")
                any_key = input("Press enter to continue...")
                f.close()
                main_menu()
            f.close()
            User_interface(input_id)
    print("Invalid user id or password Given !!!!!")
    any_key = input("Press enter to continue...")
    f.close()
    User_signin()
 



#This is the menu avilable for users after sucessfull login.
def User_interface(input_id):
    print("---------------------")
    print("User Interface")
    print("---------------------\n")
    print("Choose from These options")
    print("1. Print Loan Details ")
    print("2. Pay Installment Amount")
    print("3. Print My Transaction History ")
    print("4. Exit To main Menu\n")
    user_choose = input("Input ==> ")
    if user_choose == "1":
        #Print User Loan relates all details
         f = open("User_details.txt","r")
         for read in f :
            word = read.split()
            if word[0] == input_id:
             print("All Your Details Are printed..")
             print("User Id ==>",word[0])
             print("Username ==>",word[1])
             print("Password ==>",word[2])
             print("Email ==>",word[3])
             print("Phone number ==>",word[4])
             print("Gender ==>",word[5])
             print("Age ==>",word[6])
             print("Loan Taken ==>",word[7])
             print("Intrest Rate ==>",word[8])
             if word[8] == "5":
                 print("Loan Type ==> Educational Loan")
             elif word[8] == "10":
                 print("Loan Type ==> Car loan")
             elif word[8] == "15":
                 print("Loan Type ==> Home loan")
             elif word[8] == "20":
                print("loan Type ==> Personal Loan")
             print("Total Amount To pay With intrest ==>",word[10])
             print("Total Amount Paid ==>",word[11])
             print("Amount To pay monthly ==>",word[12])
             print("First Installment Date ==>",word[13])
             print("\nPlease note that you will have to pay another installment \nevery 1 month after first installment date ")
         f.close()    
         any_key = input("Press enter to continue...")
         User_interface(input_id)

    elif user_choose == "2":
        f = open("User_details.txt","r")
        for read in f :
            word = read.split()
            if word[0] == input_id:
                print("Do You sure want to pay installment amount of",word[12])
                print("1. Yes")
                print("2. No")
                choose = input("Input ==>")
                if choose == "1":
                    f.close()
                    pay_installment(input_id)
                    User_interface(input_id)
                elif choose == "2":
                    User_interface(input_id)
                else:
                    print("Invalid input Given !!!!!")
                    any_key = input("Press enter to continue...")
                    User_interface(input_id)
    elif user_choose == "3":
        h = open("History.txt","r")
        print("User_id\t\tPaid amount\t\tDate Paid")
        for read in h :
            word = read.split()
            if word[0] == input_id:
                print(word[0],"\t\t",word[1],"\t\t",word[2])
        h.close()
        any_key = input("Press enter to continue...")
        User_interface(input_id)
    elif user_choose == "4":
        main_menu()
    else:
        print("Invalid Input Given !!!!!")
        any_key = input("Press enter to continue...")
        User_interface(input_id)
    
    



#This helps in updating the payment details.
def pay_installment(input_id):
    #Updating User Loan payment info
        f = open("User_details.txt","r")       
        for read in f :
            word = read.split()
            if word[0] == input_id:
                approved = 1
                g = open("User_details2.txt","a")
                word[11] = str(int(word[11]) + int(word[12]))
                g.write(word[0]+" "+word[1]+" "+word[2]+" "+word[3]+" "+word[4]+" "+word[5]+" "+word[6]+" "+word[7]+" "+word[8]+" "+word[9]+" "+word[10]+" "+word[11]+" "+word[12]+" "+word[13]+"\n") 
                tranjection_history(input_id,word[12],word[8])
                g.close()  
            else:
                g = open("User_details2.txt","a")
                g.write(word[0]+" "+word[1]+" "+word[2]+" "+word[3]+" "+word[4]+" "+word[5]+" "+word[6]+" "+word[7]+" "+word[8]+" "+word[9]+" "+word[10]+" "+word[11]+" "+word[12]+" "+word[13]+"\n")
                g.close()
        f.close()
        f.close()
        f.close()
        f.close()
        f.close()
        f.close()
        f.close()
        os.remove('User_details.txt')
        os.rename('User_details2.txt', 'User_details.txt')
        print("Congratulations Payment sucess")
        any_key = input("Press enter to continue...")
        User_interface(input_id)

    

#This function stores the tranjection history in history.txt.
def tranjection_history(input_id,installment_money,intrest):
    h = open("History.txt","a")
    now = datetime.now()
    date = now.strftime("%Y/%m/%d")
    h.write(input_id+" "+installment_money+" "+date+" "+intrest+"\n")
    h.close()








#This function checks admin id and password.
def admin_login():
    input_id = input("Type The Username ==> ")
    input_password = input("Type the password ==> ")
    if input_id == "Admin" and input_password == "Admin":
        admin_interface()
    else:
        print("Either username or password is Incorrect")
        any_key = input("Press enter to continue...")
        admin_login()












#This function provides admin options.
def admin_interface():
    print("---------------------")
    print("Admin Interface")
    print("---------------------\n")
    print("1. Ragistration Request")
    print("2. Approve Requestes")
    print("3. View all transactions of specific customer")
    print("4. View all transactions of specific Loan type (EL/CL/HL/PL)")
    print("5. View all transaction")
    print("6. Set Loan Info")
    print("7. Exit\n")
    admin_choose = input("Input ==> ")

    if admin_choose == "1":
        #Reading all user ragistration Requestes from file 
        f = open("User_details.txt","r")
        print("User Id || Username || Password || Email || Phone Number || Gender || Age || Loan || Intrest || Total amt with intrest || Total paid By user || Monthly installment amount || First Installment Date")
        for read in f :
            word = read.split()
            if word[9] != "Yes":
                print(word[0],"||",word[1],"||",word[2],"||",word[3],"||",word[4],"||",word[5],"||",word[6],"||",word[7],"||",word[8],"||",word[10],"||",word[11],"||",word[12],"||",word[13])
        f.close()
        any_key = input("Press enter to continue...")
        admin_interface()

    elif admin_choose == "2":
        approved = 0
        
        #Updating User request to approved
        approve_id = str(input("Input User Id whom you want to approve ==> "))
        f = open("User_details.txt","r")       
        for read in f :
            word = read.split()
            if word[0] == approve_id:
                approved = 1
                g = open("User_details2.txt","a")
                g.write(word[0]+" "+word[1]+" "+word[2]+" "+word[3]+" "+word[4]+" "+word[5]+" "+word[6]+" "+word[7]+" "+word[8]+" "+"Yes"+" "+word[10]+" "+word[11]+" "+word[12]+" "+word[13]+"\n") 
                g.close()  
            else:
                g = open("User_details2.txt","a")
                g.write(word[0]+" "+word[1]+" "+word[2]+" "+word[3]+" "+word[4]+" "+word[5]+" "+word[6]+" "+word[7]+" "+word[8]+" "+word[9]+" "+word[10]+" "+word[11]+" "+word[12]+" "+word[13]+"\n")
                g.close()
        f.close()
        f.close()
        f.close()
        f.close()
        f.close()
        f.close()
        os.remove('User_details.txt')
        os.rename('User_details2.txt', 'User_details.txt')
        if approved == 1:
            print("Approved Register Request")
            any_key = input("Press enter to continue...")
            admin_interface()

        print(" Invalid (id does not exist)")
        any_key = input("Press enter to continue...")
        admin_interface()

    elif admin_choose == "3":
        h = open("History.txt","r")
        input_id = input("Give an id ==>")
        print("User_id\t\tPaid amount\t\tDate Paid")
        for read in h :
            word = read.split()
            if word[0] == input_id:
                print(word[0],"\t\t",word[1],"\t\t",word[2])
        h.close()
        any_key = input("Press enter to continue...")
        admin_interface()

    elif admin_choose == "4":
        print("Which Loan plan to search for")
        print("1. Educatioal Loan")
        print("2. Car loan")
        print("3. hoam loan")
        print("4. personal loan\n")
        choose_loan = str(input("Input ==>"))
        loan_search = "0"
        if choose_loan == "1":
            loan_search = "5"
        elif choose_loan == "2":
            loan_search = "10"
        elif choose_loan == "3":
            loan_search = "15"
        elif choose_loan == "4":
            loan_search = "20"
        else:
            any_key = input("Press enter to continue...")
            admin_interface()

        h = open("History.txt","r")
        print("User_id\t\tPaid amount\t\tDate Paid")
        for read in h :
            word= read.split()
            if word[3] == loan_search:
                print(word[0],"\t\t",word[1],"\t\t",word[2])
        h.close()
        any_key = input("Press enter to continue...")
        admin_interface()

    elif admin_choose == "5":
        h = open("History.txt","r")
        print("User_id\t\tPaid amount\t\tDate Paid")
        for read in h :
            word = read.split()
            print(word[0],"\t\t",word[1],"\t\t",word[2])
        h.close()
        any_key = input("Press enter to continue...")
        admin_interface()

    elif admin_choose == "6":
        user = str(input("Type user Id To update Details ==>"))
        loan_with_intrest  = str(input("Type Total Amount to pay with intrest ==>"))
        installment_amount = str(input("Type monthly installment amount ==>"))
        first_installment = str(input("Type first imstallment date (no space) ==>"))
        f = open("User_details.txt","r") 
        approved = 0      
        for read in f :
            word = read.split()
            if word[0] == user:
                approved = 1
                g = open("User_details2.txt","a")
                g.write(word[0]+" "+word[1]+" "+word[2]+" "+word[3]+" "+word[4]+" "+word[5]+" "+word[6]+" "+word[7]+" "+word[8]+" "+"Yes"+" "+loan_with_intrest+" "+word[11]+" "+installment_amount+" "+first_installment+"\n") 
                g.close()  
            else:
                g = open("User_details2.txt","a")
                g.write(word[0]+" "+word[1]+" "+word[2]+" "+word[3]+" "+word[4]+" "+word[5]+" "+word[6]+" "+word[7]+" "+word[8]+" "+word[9]+" "+word[10]+" "+word[11]+" "+word[12]+" "+word[13]+"\n")
                g.close()
        f.close()
        f.close()
        f.close()
        os.remove('User_details.txt')
        os.rename('User_details2.txt', 'User_details.txt')
        if approved == 1:
            print("Updated User loan details")
            any_key = input("Press enter to continue...")
            admin_interface()

        print(" Invalid (id does not exist)")
        any_key = input("Press enter to continue...")
        admin_interface()
    elif admin_choose == "7":
        main_menu()

    else:
        print("Invalid Input Given !!!!!")
        any_key = input("Press enter to continue...")
        admin_interface()

















#This function asks for exit confirmation before exit.
def Exit():
    print("You sure want to ext")
    print("1. Yes")
    print("2. No\n")
    exit_choose = str(input("Input ==>"))
    if exit_choose == "1":
        print("Exitting...")
        exit()
    elif exit_choose == "2":
        main_menu()
    else:
         print("Invalid Input Given !!!!!")
         any_key = input("Press enter to continue...")
         Exit()














#Printing main menu. This menu is the first menu that gets displayed after user opens application
def main_menu():
    print("Welcome to Malaysia Bank Online Loan Management System (MBOLMS)")
    print("-----------------------------------------------------------------")
    print("Select Your Desired Option")
    print("1. New User")
    print("2. Registred User")
    print("3. Admin Login")
    print("4. Exit \n")
    main_choose = input("Input ==> ")
    if main_choose == "1":
        new_user()
    elif main_choose == "2":
        User_signin()
    elif main_choose == "3":
        admin_login()
    elif main_choose == "4":
        Exit()
    else:
        print("Invalid Input Given !!!!!")
        any_key = input("Press enter to continue...")
        main_menu()






main_menu()