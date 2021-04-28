



print('''Hello Customer, welcome to the Central Bank of Liberia ''')
name = input("What is your name? /n  ") 
from hello import login
import random
accountNumber = random.randrange(111111111111,999999999999)


database_User = { 
    "Abel": "passwordAbel" ,
    "Koquoi": "passwordKoquoi",
    "Grace": "passwordGrace",
    "Mogana": "passwordMogana",
    "Chris" : "passwordChris ",
    "Angeline":"passwordAngeline",
    "Naomi" : "passwordNaomi",
    "Gloria":"passwordGloria",
    "Emmanuel_N_B_Flomo": "passwordEmmanuel"
    }


    
#if (name in database_User): 
    
def init():
    while IsValidOptionSelected == False:
        haveAccount = int(input("Do you have account with us: 1(yes) 2(No) /n  "))
        if (haveAccount  == 1):


            if name in database_User: 
                login()
          

        elif (haveAccount == 2): 
            IsValidOptionSelected = True
            register()


        else:
            print("You have selected invalid option") 




def login():
    print('login to your account')
    print("******* login ******")
    input ("What is your name?/n  ")
    input("What is your password:/n  ")



      

def register() :
    print("****** register ****** ") 
    email = input ("What is your email address? /n  ") 
    first_name = input("What is your first name? /n  ") 
    last_name = input("What is your last name? /n  ")
    password = input("Create password for yourself: /n  ") 

    accountNumber = GenerateAccountNumber()
    database_User[accountNumber] = [first_name,last_name,email,password] 
    random.randrange.(111111111111,999999999999)
    print("Your account has been created")
    print("== ==================== ==")
    print("Your account number is:",  accountNumber )
    print("Make sure you keep it safe")
    login()
    bankOperation() 


def bankOperation(user): 
    print(" Welcome",( user[0],user[1]))
    Selectedoption = input("What would you like to do, (1) Deposit, (2) Withdraw, (3) Logout, (4) Exit")

    if (Selectedoption == 1):
        OperationDeposit() 

    elif Selectedoption == 2:
        OperationWithdraw()

    elif Selectedoption == 3:
        login()
    elif Selectedoption == 4:
        exit ()
    else:
        bankOperation()
        print("Selected option invalid")          



def OperationWithdraw():
     print ("Withdraw")


def OperationDeposit():
    print('Deposit')    
    
def GenerateAccountNumber(): 
    print('Generating Account Number') 
     ### Actual Banking System ###
    print(GenerateAccountNumber()) 
    init()
