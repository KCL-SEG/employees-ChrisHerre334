"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type='salary', salary=0, hourly_wage=0, hours_worked=0, bonus=0, contracts_landed=0, commission_per_contract=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        total_pay = 0

        if self.contract_type == 'salary':
            total_pay = self.salary
        elif self.contract_type == 'hourly':
            total_pay = self.hourly_wage * self.hours_worked
        
        if self.bonus:
            total_pay += self.bonus
        elif self.contracts_landed and self.commission_per_contract:
            commission = self.contracts_landed * self.commission_per_contract
            total_pay += commission

        return total_pay
        

    def __str__(self):
        pay_description = f"{self.name} works on "

        if self.contract_type == 'salary':
            pay_description += f"a monthly salary of {self.salary}."
        elif self.contract_type == 'hourly':
            pay_description += f"a contract of {self.hours_worked} hours at {self.hourly_wage}/hour."
        else:
            pay_description += "an unknown contract type."

        total_pay = self.get_pay()

        if self.bonus:
            pay_description += f" and receives a bonus commission of {self.bonus}."

        if self.contracts_landed and self.commission_per_contract:
            pay_description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract."

        pay_description += f" Their total pay is {total_pay}."

        return pay_description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', hourly_wage=25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', salary=3000, contracts_landed=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'houry', hourly_wage=25, hours_worked=150, contracts_landed=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', salary=200, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'houry', hourly_wage=30, hours_worked=120, bonus=600)
