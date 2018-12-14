             #ATM project

           #methods or function
#start of method
available_balance = 20000

def dogMenu():
    print("Please wait... \n Have your cash \n TRANSACTION COMPLETED")
    
def withdraw():
    withdraw_ammount = 0
    print("Welcome to withdraw")
    operation_1 = int(input("\n.1 SAVINGS \n.2 CURRENT \n"))
    user_input = int(input("Select ammount :\n1. 500 \n2. 1,000 \n3. 2,000 \n4. 5,000 \n5. 10,000 \n6. 15,000 \n7. 20,000 \n8. OTHERS \n"))
    if (operation_1 == 1 or operation_1 == 2) :
        if(user_input == 1): withdraw_ammount = 500
        elif(user_input == 2): withdraw_ammount = 1000
        elif(user_input == 3): withdraw_ammount = 2000
        elif(user_input == 4): withdraw_ammount = 5000
        elif(user_input == 5): withdraw_ammount = 10000
        elif(user_input == 6): withdraw_ammount = 15000
        elif(user_input == 7): withdraw_ammount = 20000
        
        if(withdraw_ammount == 0 ): print("Invalid input")
        elif(withdraw_ammount > available_balance):  print("Insurficient fund")
        else :
            print("please wait...")
            print("Hello user please take your cash")
            print("Transaction completed, have your card")
            
            
        

    else: print("Invalid input")
         
    
def transfer():
     print("Welcome To Transfer Section")
     bank_name = ""
     bank_type= int(input("\n1. ACCESS BANK \n2. SKY BANK \n3. UNION BANK \n4. GARANTY TRUST BANK \n5. POLLARIS BANK \n6. DIAMOND BANK \n"))
     
     if(bank_type == 1): bank_name = "ACCESS BANK"
     elif(bank_type == 2): bank_name = "SKY BANK"
     elif(bank_type == 3): bank_name = "UNION BANK"
     elif(bank_type == 4): bank_name = "GARANTY TRUST BANK"
     elif(bank_type == 5): bank_name = "POLLARIS BANK"
     elif(bank_type == 6): bank_name = "DIAMOND BANK"

     else:
         print("Invalid Input")
     print("Selected bank type is : ", bank_name)
     account_number =int(input("Please enter account number: "))
     amount = int(input("Please enter amount : "))
     print("Please wait... \n Transfer completed and", amount," as been sent to" , account_number )

def balance():
     print("Balance of user: #5'000")
     

def operationMenu():
     #statements
     print("Welcome Oluwawolemi Kolawole")
     operation_2 = int(input("What operation would you like to perform?: \n1.Withdrawal \n2.Transfer \n3.Check balance \n Enter number of operation:"))
     if (operation_2 == 1) : withdraw()
     
     elif(operation_2==2): transfer()
     elif(operation_2==3): balance()

     else :
         print("wrong input")
#end of method

#Start of Password 
print("Welcome to ZENITH BANK")

password= (input("Please enter your pin \n"))

if(password == "1234"):  operationMenu()

else:
     print("Wrong password")
     print("Take your card")
   
     








     
          



 
