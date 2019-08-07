class InsufficientBalanceError(Exception):
    pass
    
class Account():
    def __init__(self, n, b, t):
        if type(self) == Account:
            raise NameError("Create objects using SA or CA")
        self.n = n
        self.b = b
        self.t = t
    def credit(self, amount):
        self.b += amount
    def __repr__(self):
        return self.__str__()
    def debit(self, amount):
        self.b -= amount    

class SA(Account):
    def __init__(self, n, b=100):
        Account.__init__(self, n, b, 'S')
        
    def debit(self, amount):
        if self.b < amount:
            raise InsufficientBalanceError("Check Balance")
        else:
            Account.debit(self,amount)
            
    def __str__(self):
        return "SA({},{},{})".format(self.n, self.b, self.t)
        
class CA(Account):
    def __init__(self, n, b=0):
        Account.__init__(self, n, b, 'C')
    def __str__(self):
        return "CA({},{},{})".format(self.n, self.b, self.t)


sa = SA('Aditya')
print(sa)
try:
    sa.debit(1000)
except InsufficientBalanceError as err:
    print("Please check the balance and continue")
    
print(sa)

ca = CA('ABC inc.')
print(ca)
ca.debit(100)
print(ca)

ac1 = Account("Aditya", 100, 'S')



#user --> sa.debit(1000) --> SA.debit(1000)
#user friendly message <-- try ... except <-- raise Error
        
#VERSION 1

#SA, CA
# SA --> def b of 100
#CA -- def b of 0

#SA --> cannot debit more than balance
#CA --> blance can go to -ve


#class SA:
#    def __init__(self, n, b=100):
#        self.n = n
#        self.b = b
#        self.t = 'S'
#    def credit(self, amount):
#        self.b += amount
#    def debit(self, amount):
#        if self.b < amount:
#            # TODO raise an exception
#            print("Insufficient Balance")
#        else:
#            self.b -= amount    
#    def __str__(self):
#        return "SA({},{},{})".format(self.n, self.b, self.t)
#    def __repr__(self):
#        return self.__str__()
#        
#class CA:
#    def __init__(self, n, b=0):
#        self.n = n
#        self.b = b
#        self.t = 'C'
#    def credit(self, amount):
#        self.b += amount
#    def debit(self, amount):
#        self.b -= amount    
#    def __str__(self):
#        return "CA({},{},{})".format(self.n, self.b, self.t)
#    def __repr__(self):
#        return self.__str__()
#        