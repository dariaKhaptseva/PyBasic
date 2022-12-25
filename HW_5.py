#1

import random

list = [random.randint(1, 200) for i in range(20)]
for x in list:
    if x>100 :
        print (x, end=" ")


print()

#2
my_list = [random.randint(1, 200) for i in range(10)]
my_result = []
for x in my_list:
        if x>100:
            my_result.append(x)
print(my_result)

print()
#3
my_list3 = [random.randint(1, 200) for i in range(random.randint(0, 2))]
print(my_list3)

dlina = len(my_list3)
print(dlina)
if dlina<2:
    my_list3.append(0)
    print(my_list3)
else:

    my_list3.append(my_list3[0]+my_list3[1])
    print (my_list3)