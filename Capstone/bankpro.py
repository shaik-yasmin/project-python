class Bank:
    def balance(self):
        try:
            user1_amount = 250
        except :
            print("actual amount of user1",self.user1_amount)
            balance=self.amount+self.dep-self.wd
            print("available balance",balance)
    def deposite(self,dep):
        try:
            user1_amount = 250
        except:
          self.dep=dep
          if self.dep>2000:
                print("ur depositing more than 2000")

    def withdraw(self,wd):
        try:
            user1_amount = 250
        except:
          self.wd=wd
          if self.wd>250:
            print("u can't withdraw more than 250")
bank=Bank()
bank.deposite(1200)
bank.withdraw(300)
bank.balance()
