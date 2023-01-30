divide_values = [2, 0, None, "1", True, False, [], {}]
values_to_divide = [10, "1", None, True, False, [], 0, {}]

for k in range(0, len(divide_values)):
    try:
        print(divide_values[k] / values_to_divide[k])
    except TypeError:
        print('Не можна комбінувати ці типи даних')
    except ZeroDivisionError:
        print("Ділити на нуль не можна!")


#2


