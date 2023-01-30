#1
print('#1')
def dividing_lists():
    """
    this function divide elements of
    1 list on elements of 2 list

    :return:
    result of dividing and 2 errors
    TypeError and ZeroDivisionError
    """

divide_values = [2, 0, None, "1", True, False, [], {}]
values_to_divide = [10, "1", None, True, False, [], 0, {}]

for k in range(0, len(divide_values)):
    try:
        print(divide_values[k] / values_to_divide[k])
    except TypeError:
        print('Не можна комбінувати ці типи даних')
    except ZeroDivisionError:
        print("Ділити на нуль не можна!")

print()

#2
print('#2')
def dividing_lists2():
    """
    this function divide elements of
    1 list on elements of 2 list

    :return:
    result of dividing and any error
    or success
    """

divide_values = [2, 0, None, "1", True, False, [], {}]
values_to_divide = [10, "1", None, True, False, [], 0, {}]

for k in range(0, len(divide_values)):
    try:
        print(divide_values[k] / values_to_divide[k])
    except Exception:
        print('Щось пішло не так')
    else:
        print('Ділення пройшло успішно!')
print()
#3
print('#3')
def change_index_list():
    """
    this function find element of list
    by index

    :return:element
    or 2 types of errors
    ValueError,IndexError

    """

list_of_integers = [0, 1, 2, 3, 4, 5]
user_index = input('введіть індекс: ')
try:
    print(list_of_integers[int(user_index)])
except ValueError:
    print('Потрібно ввести ціле число!')
except IndexError:
    print('Такого індексу не існує')

print()
#4
print('#4')
def show_element_by_key():
    """
    this function shows element
    by key

    :return:element
    or KeyError

    """

person_data = {"name": "Bolt", "age": 23, "gender": "male", "born_date": "06.07.1990"}
user_key = input('введіть ключ: ')

try:
    print(person_data[user_key])
except KeyError:
    print('Такого ключа не існує')

finally:
    print('Чекаю наступного ключа')
