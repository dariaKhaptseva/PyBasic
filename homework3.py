'''1. Написать калькулятор для простых операций(+,-,*,/,**),
Операнды и оператор вводятся с клавиатуры отдельно(отдельные переменные)

2. По данному целому числу N распечатайте все квадраты натуральных чисел,
 не превосходящие N, в порядке возрастания.
Например:
50      1 4 9 16 25 36 49
10      1 4 9
100     1 4 9 16 25 36 49 64 81 100

3. Определить является ли введенное с клавиатуры число простым
(делится без остатка только на себя и единицу)

*(НЕОБЯЗАТЕЛНО! НА ОЦЕНКУ НЕ ВЛИЯЕТ)
Создайте приложение подбирающее правильное окончание к фразе:
 "Маша нашла в лесу {К} гриб...". K пользователь вводит с клавиатуры.
Например: Маша нашла в лесу 7 грибОВ.
Маша нашла в лесу 32 грибА.'''




#Task1
a = float (input('Input your first number:  '))
x = str (input('Input the operator +, -, *, /, **:  '))
b = float (input('Input your second number:  '))
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
if x == '+':
    print (c)
elif x == '-':
    print (d)
elif x == '*':
    print (e)
elif x == '/':
    print (f)
elif x == '**':
    print (g)
else:
    print ('The operator not found')


#Task2


n = int (input('Input an integer number :  '))

for x in range (1,n,1) :
    y = int (x*x)
    if y > n:
        break
    print (y, end = ' ')

#Task3

print(' ')
p = int (input('Input an integer number :  '))
for i in range(2, (p//2)+1):
        if p % i == 0:
            print ('your number is NOT prime')
            break
else:
    print ('your number is prime')







