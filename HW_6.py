#'''3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы
# на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.'''
import random
my_list1 = [random.randint(1,10) for i in range(10)]
my_list2 = [random.randint(1,100) for i in range(10)]
k1 = random.randint(0, 9)
k2 = random.randint(0, 9)
print(my_list1)
print(my_list2)




ch = [x for k1,x in enumerate(my_list1) if k1%2==0]
nch = [y for k2,y in enumerate(my_list2) if not k2%2==0]
my_result = ch+nch
print(my_result)

print()
#11
#Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
#в строке ТОЛЬКО ОДИН раз.

my_str=('Peremoga nezabarom!')
print(my_str)
new = list (my_str)
print (new)
un = [letter for letter in new if  new.count(letter)==1]
print (un)
