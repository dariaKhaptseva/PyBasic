#*4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
 #Если my_list [1,2,3,4], то new_list [2,3,4,1]

import random
my_list = [random.randint(1,10) for i in range(10)]
new_list =[]
print (my_list)
new_list.append(my_list[-1]) #create list with last
new_list2 = my_list[:-1] #cut the last
new_list.extend(new_list2) #join
print (new_list)
print()
#6**5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
#Пересоздавать список нельзя! (используйте метод pop)
my_list5 = [random.randint(1,10) for i in range(10)]
print (my_list5)
my_list5.append(my_list5.pop(0))
print(my_list5)
print()
#*6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
#Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
#(используйте split и проверку isdigit)
my_str = ('43 jkmit 34, но меньше 56')
li = list (my_str.split())
print (li)
if li[] is
print(my_str.isdigit())
#print(li.digit)

