import random
list = [random.randint(1, 200) for i in range(20)]
k = int(input('введите нечетное число от 1 до 20: '))
C = int(input('введите любое число: '))
b=k-1
z=19
print (list)
while z>k-1:
    list[z]=list[z-1]
    z=z-1
list[b] = C
list.append(random.randint(1, 200))
print (list)
