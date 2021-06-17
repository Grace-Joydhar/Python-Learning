#Video 15 and 16 are related to Dictonary.

a = "\nit is a colletion which is unodered, changeable and indexed. It will represent by {...} Bracket. " \
    "\nIt carreis unique keys  {ex: name} but the values could be same {'Grace}. Key and values will be defined by collon (:)"
print(a)

d1 = {'Name' : 'Grace', 'Age':25, 'B-Date': 25}
print(d1)
print(d1['Age'])

b = "\nDictionary can carry different types of keys: str, int, float, bool and so on: "
print(b)

d2 = {'name':'Joydhar', 5:5, 10.5:10.5, True:True, (2,3):5}
print(d2)
print(d2[(2,3)])

c= "\nCopy values: "
print(c)
d3 = d2.copy()
print(d3)

x = len(d2)
print(x)

d = "\nTo add a new value:"
print(d)
d2['Varsity'] = 'Daffodil'
print(d2)

e = "\nTo delete a item:"
print(e)
d2.pop('Varsity')
print(d2)

f = "\nClear function used to clear all the values from a list: "
print(f)
d1.clear()
print(d1)

'''g = "\nDelete function used to delete the whole list: "
del d1
print(d1)'''

g = "\nCheck a value with get function: "
print(g)
print(d2.get('name'))

h = "\nTo check all the items: "
print(h)
print(d2.items())

i = "\nTo find out keys: "
print(i)
print(d2.keys())
