my_string = ('0123456789')


for tens_count in my_string:
       for num_count in my_string :
            numbers = int(tens_count)*10+int(num_count)
            print (numbers, end=' ')

print ()

#a
strings = 7

print((strings * 2) * ' ' + '*')
for s in range(1, strings-1):
    for space in range((strings * 2 - s * 2)):
            print(' ', end='')
    print('*', end='')
    for space2 in range(s * 3+(s-1)):
            print(' ', end='')
    print('*')

print('',' *'*((strings*2)-(1)))

print()


#b
strings = 7

for s in range(1, strings + 1):
    for space in range(strings * 2 - s * 2):
        print(' ', end='')
    for star in range(s * 2 - 1):
        print('*', end=' ')
    print()

print()
#c
strings=13
strings1 = int ((strings+1)/2)

for s in range(1, (strings1 + 1)):
    for space in range(strings1 * 2 - s * 2):
        print(' ', end='')
    for star in range(s * 2 - 1):
        print('*', end=' ')
    print()

strings2 = int ((strings-1)/2)


for s in range(1, (strings2)):
    for space2 in range(s*2):
            print(' ', end='')
    print('*', end='')
    for space3 in range((strings2+1-s)*4-5):
            print(' ', end='')
    print('*')

#print('',' *'*((strings*2)-(1)))
print((strings-1) * ' ' + '*')
print()

#d
print('Im so sorry but I cant do this homework anymore')







