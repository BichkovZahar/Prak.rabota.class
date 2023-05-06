class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, count):
        if count > 0:
            self.balance += count
        else:
            print("Неприпустима сума для внесення!")

    def finish(self, count):
        if count > 0:
            if self.balance >= count:
                self.balance -= count
            else:
                print("Недостатньо коштів на рахунку!")
        else:
            print("Неприпустима сума для зняття!")

    def get_balance(self):
        return self.balance
rezult = BankAccount("Olga" , balance=0)
rezult.finish(100)
rezult.deposit(-100)
print(rezult.get_balance())

