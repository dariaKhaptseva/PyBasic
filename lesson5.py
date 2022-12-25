#4*
import random
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















#6*
my_list6 = [random.randint(1, 10) for i in range(5)]
my_list7 = [random.randint(1, 10) for i in range(5)]


def elements() -> my_list6:
   print(my_list6)

#x=int
#x in my_list6
#print(my_list7)
#if (my_list6.count(x) != 1):
    #print(my_list6.count)


#print(my_list6)
