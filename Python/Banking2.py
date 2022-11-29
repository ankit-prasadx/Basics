# Instance variables : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class vaiable : Bank_Name, ROI_On_FD

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



def main():

    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Intrest on Fixed Deposit : ",Bank_Account.ROI_On_FD)
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating New Account")
    User1.CreateAccount()
    print("Creating New Account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()