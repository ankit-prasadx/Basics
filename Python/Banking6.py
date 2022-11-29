# Instance variables : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo(), Deposit(), Withdraw()
# Class vaiable : Bank_Name, ROI_On_FD
# Class method : DisplayBankInformation()
#  Static method : DisplayKYCInfo()

class Bank_Account:
    Bank_Name = "CITI Bank"
    ROI_On_FD = 6.7
    def __init__(self):
        self.Name = ""
        self.Amount = 0.0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter Your Name : ", end=" ")
        self.Name = input()
        
        print("Enter Initial Amount : ", end=" ")
        self.Amount = float(input())
        
        print("Enter Your Address : ", end=" ")
        self.Address = input()
        
        print("Enter Your Enter Account Number : ", end=" ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("_______________Your Account Information is as below_______________")
        print("Name of Account Holder : ", self.Name)
        print("Account Number : ", self.AccountNo)
        print("Address of Account Holder : ", self.Address)
        print("Current Amount in Account : ", self.Amount)        

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to Banking Console")
        print(cls.Bank_Name)
        print("Rate of Intrest we Offer on Fixed Deposit : ",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please Consider below KYC information")
        print("According to rules of Government of India you have to Submit below documents")
        print("1 : Clear and Recent Passport size photograph")
        print("2 : Photocopy of Aadhar Card")
        print("3 : Photocopy of PAN Card")
    
    def Deposit(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self,Value):
        self.Amount = self.Amount - Value

def main():
    print("_______________________________________________________________________________")
    print("___________________Banking Application___________________")
    print("_______________________________________________________________________________")
    
    print("______________Calling Static method to display KYC info______________")
    Bank_Account.DisplayKYCInfo()
    print("_______________________________________________________________________________")

    # print("_______________________________________________________________________________")
    # print("______________Accessing the class variables from main______________")
    # print("_______________________________________________________________________________")
    # print("Name of Bank : ",Bank_Account.Bank_Name)
    # print("Rate of Intrest on Fixed Deposit : ",Bank_Account.ROI_On_FD)

    print("_______________________________________________________________________________")
    print("Calling the class methods to display bank information of first account")
    print("_______________________________________________________________________________")
    Bank_Account.DisplayBankInformation()

    print("_______________________________________________________________________________")
    print("______________Creating objects of class______________")
    print("_______________________________________________________________________________")
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("_______________________________________________________________________________")
    print("Creating first Account")
    print("_______________________________________________________________________________")
    print("_______________________________________________________________________________")
    print("______________Enter Details for first Account holder______________")
    User1.CreateAccount()
    print("_______________________________________________________________________________")

    print("_______________________________________________________________________________")
    print("Creating second Account")
    print("_______________________________________________________________________________")
    print("_______________________________________________________________________________")
    print("______________Enter Details for second account holder______________")
    User2.CreateAccount()
    print("_______________________________________________________________________________")

    print("______________Calling the instance methods to display bank information of first account______________")
    User1.DisplayAccountInfo()

    
    print("______________Calling the instance methods to display bank information of second account______________")
    User2.DisplayAccountInfo()

    print("______________Depositing 500 in User1______________")
    User1.Deposit(500)

    print("______________Depositing 900 in User2______________")
    User2.Deposit(900)

    print("Amount of {} after deposit is {}".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit is {}".format(User2.Name,User2.Amount))
    

    print("______________Withdrawing 5500 from User1______________")
    User1.Withdraw(5500)

    print("______________Withdrawing 1900 from User2______________")
    User2.Withdraw(1900)

    print("Amount of {} after withdraw is {}".format(User1.Name,User1.Amount))
    print("Amount of {} after withdraw is {}".format(User2.Name,User2.Amount))


    print("_______________________________________________________________________________")
    print("___________________End of Banking Application___________________")
    print("_______________________________________________________________________________")
    


if __name__ == "__main__":
    main()