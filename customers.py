import random


class Customer:
    num_of_customers = 0

    def __init__(self, _id=0, debt=False):
        self.debt = debt
        self._id = _id
        Customer.num_of_customers += 1
        self._id = Customer.num_of_customers
        customers.append(self)

    def pay_debt(self):
        self.debt = False

    def owe_debt(self):
        self.debt = True




customers = []


customer_1 = Customer()
customer_2 = Customer()
customer_3 = Customer()
customer_4 = Customer()
customer_5 = Customer()
customer_6 = Customer()
customer_7 = Customer()
customer_8 = Customer()
customer_9 = Customer()
customer_10 = Customer()


def bills_due(cust_list):#generate pending debt in 5 random customers
    for i in range(5):
        cust_list[random.randint(0, 9)].owe_debt()
             

