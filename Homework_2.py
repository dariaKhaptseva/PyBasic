'''
3. Дано целое, положительное, трёхзначное число. Например: 123, 867, 374.
Необходимо его перевернуть. Например, если ввели число 123,
 то должно получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами. Строки использовать НЕЛЬЗЯ!

*(НЕОБЯЗАТЕЛНО! НА ОЦЕНКУ НЕ ВЛИЯЕТ)
Микропроцессор электронных часов считает количество секунд прошедших от начала суток
(значение вводится с клавиатуры пользователем). Необходимо написать программу отображающую время
 в формате чч:мм:сс. Например: 9375 -> 2:36:15
'''

print ('Задача 1')
n =  int(input('Введіть кількість школярів: '))
k =  int(input('Введіть кількість яблок: '))
print (f'Кількість яблок, що отримає кожен школяр  {k//n} ')
print (f'Кількість яблок, що залишиться в корзині {k%n} ')
'''

'''
print ('Задача 2')
first_class_pupils_cnt =  int(input('Введіть кількість школярів в класі 1: '))
second_class_pupils_cnt =  int(input('Введіть кількість школярів в класі 2: '))
third_class_pupils_cnt =  int(input('Введіть кількість школярів в класі 3: '))
total_pupils = first_class_pupils_cnt+second_class_pupils_cnt+third_class_pupils_cnt
print (f'Кількість парт, що необхідно придбать:  {total_pupils//2+total_pupils%2}')

print ('Задача 3')
users_number = int(input('Введіть ціле трьозначне число: '))
receive_first_two_num = users_number//10
new_number2 = receive_first_two_num%10
new_number1 = receive_first_two_num//10
new_number3 = users_number%receive_first_two_num
print(new_number3,new_number2,new_number1)