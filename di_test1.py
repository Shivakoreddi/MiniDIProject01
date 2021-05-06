class Employees:

    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email = first+'.'+last+'@Company.com'


    def fullname(self):

        return '{} {}'.format(self.first,self.last)

emp_1 = Employees('Shiva','Koreddi',180000)
emp_2 = Employees('Srav','Koreddi',180000)

print(emp_1.email)
print(emp_1.fullname())
