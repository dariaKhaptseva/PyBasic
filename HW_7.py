

persons = [{'name': 'John', 'age': 15},
              {'name': 'Matilda', 'age': 18},
              {'name': 'Fillipa', 'age': 33},
              {'name': 'Fiona', 'age': 13},
              {'name': 'Klod', 'age': 13}]

#1a
new_dict={}                     #create new dict without "name" and "age", only values, where name is key, age is value
for i in persons:
    z = (i.pop('name'), i.pop('age'))
    new_dict.update ([z])

li_name = list(new_dict.keys())
li_age = list(new_dict.values())
result = min (new_dict.values())

q = len(li_age)
li_result=list()
for x in range(q):
    if li_age[x] == result:
       li_result.append(li_name[x])
print('1a - ', li_result)
print()

#1b
li_result2 = list()
l = len(max(li_name))
for y in li_name:
    if len(y) == l:
        li_result2.append(y)
print('1b - ', li_result2)
print()

#1c
a = float
for a in li_age:
    a = sum(li_age)/len(li_age)
print('1c - ', a)
print()

#2

my_dict1 = {1:'juce',2:'vodka',3: 'jin', 4:'visky'}
my_dict2 = {2:'dance',1:'work',44:'sleep', 55:'read'}

#2a)
li1 = list(my_dict1.keys())
li2 = list(my_dict2.keys())
li3 = (li1+li2)
non_un = [x for x in li3 if li3.count(x) != 1]
un = [x for x in li3 if li3.count(x) == 1]
print('2a - ', non_un)
print()

#2b)
res2 = [y for y in li1 if li2.count(y)==0]
print('2b - ', res2)
print()

#2c)
res3 = {k: my_dict1.get(k) for k in res2 }
print('2c - ', res3)
print()

#2d)


res4 = dict()

for b in my_dict1.items():
    if b[0] not in my_dict2:
        res4[b[0]] = b[1]
    else:
        res4[b[0]] = [b[1], my_dict2[b[0]]]

my_dict2.update(res4)
print('2d - ', my_dict2)





