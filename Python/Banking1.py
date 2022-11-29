# Instance variables : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()

class Bank_Account:
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
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating First Account")
    User1.CreateAccount()
    print("Creating First Account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()