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

    Bank_Account.DisplayKYCInfo()
    
    Bank_Account.DisplayBankInformation()

    # print("Name of Bank : ",Bank_Account.Bank_Name)
    # print("Rate of Intrest on Fixed Deposit : ",Bank_Account.ROI_On_FD)
    
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating New Account")
    User1.CreateAccount()
    print("Creating New Account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(500)
    User2.Deposit(900)

    print("Amount of {} after deposit is {}".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit is {}".format(User2.Name,User2.Amount))
    
    User1.Withdraw(5500)
    User2.Withdraw(1900)

    print("Amount of {} after withdraw is {}".format(User1.Name,User1.Amount))
    print("Amount of {} after withdraw is {}".format(User2.Name,User2.Amount))

if __name__ == "__main__":
    main()