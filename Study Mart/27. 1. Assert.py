a = "Assert is mainly used for Eroor Handling as like Exception. But there is some different issues. For example, salary can not be less than 0. So if it is lower than 0, then a error will be occured\n"
print(a)

def MySalary(salary):
    '''assert condition, "Message"'''
assert salary > 0, "Salary can not less than zero"
    print("My salary is", salary)
MySalary(-5000)