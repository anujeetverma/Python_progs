#Parent Class
class User():
    def __init__(self,name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Name")
        print("")
        print("Name : ",self.name)
        print("Age : ", self.age)
        print("Gender : ",self.gender)

        

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age ,gender)
        self.balance=0


    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("account balance has been updated : $ ", self.balance)

    def show_balance(self):
        self.show_details
        print(self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount >self.balance:
            print("Insufficent balance , Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account Balance has been updated : $", self.balance)






