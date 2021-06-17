all_info = [('1', 'Grace', 23), ('2', 'Smita', 28), ('3', 'Antora', 25)]

unzip_all_info = list(zip(*all_info))
print(unzip_all_info)

serial = unzip_all_info[0]
name = unzip_all_info[1]
age = unzip_all_info[2]

print(serial)
print(name)
print(age)