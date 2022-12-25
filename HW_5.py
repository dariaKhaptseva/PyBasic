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

print()

#4*

my_list4 = [random.randint(1, 200) for i in range(20)]
print (my_list4)
k = random.randint(0, 19)
#(my_list4.pop())
print(k)
while k<19:
    my_list4[k]=my_list4[k+1]
    k=k+1
my_list4.pop()
my_list4.pop()
print(my_list4)

print()
#5*

my_list5 = [random.randint(1,10) for i in range(10)]
print (my_list5)
k = random.randint(1, 10)
c = random.randint(1, 100)
print(k)
print(c)
counter=9
my_list5.append(my_list5 [9]) #додаємо елемент в список і пишемо в нього останній елемент інакше він затреться
while counter > k-1:
    my_list5[counter] = my_list5[counter -1]
    counter = counter - 1
my_list5[k-1] = c
my_list5.append(random.randint(1,10))
print(my_list5)
