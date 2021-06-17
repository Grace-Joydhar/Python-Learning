'''def My_Add(*num):
    initial=0
    for i in num:
        initial = initial + i
    print(initial)
My_Add(1,2,3,4)
'''

'''
def My_Str(*str):
    for i in str:
        print(i)
My_Str("My", "Name", "is", "Grace")
'''

def My_arg(str1, *str):
    print("str1 is: ",  str1)
    for i in str:
        print("*str is: ", str)

My_arg("My", "Name", "is", "Grace")