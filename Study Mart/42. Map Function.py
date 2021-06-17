def mul_five_times(number):
    return number*5
num = [1,2,3,4,5]

result = list(map(mul_five_times, num))
print(result)