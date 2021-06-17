student = {1:{'name': 'Joydhar', 'Age': 23, 'Gender': 'Female'},
2:{'name': 'Antora', 'Age': 20, 'Gender': 'Female'}}

print(student)

student[3] = {}
student[3]['name'] = 'Raha'
student[3]['Age'] = 30
student[3]['Gender'] = 'Male'

print(student[3])
print(student)

del student[2]['name']
print(student)

del student[2]
print(student)