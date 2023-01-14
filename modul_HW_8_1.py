
li1 = list(['John', 'Mary', 'Fil', 'Paul'])
result = list()


def rev_nechet_str() -> list:
    """
    This function return new list of string items
    for even index - the same
    for odd index - reversed
    
    :return: result
    """
for i, x in enumerate(li1):
    if i % 2 == 0:
        result.append (li1[i])

    else:
        result.append(x[::-1])

#print(result)
print()

#2
li2 = list(['John', 'Aro', 'Fil', 'Paul'])
result2 = list()

def a_string_first_item() -> list:
    """
    This function return new list of string items
    if they starts from "A"

    :return: result
    """

for k, y in enumerate(li2):
    if y[0] == 'A':
        result2.append(li2[k])
#print(result2)
print()

#3
result3 = list()
def a_string_any_item() -> list:
    """
    This function return new list of string items
    if they have "a"

    :return: result
    """

for k, y in enumerate(li2):
    if 'A' in y or 'a' in y:
        result3.append(li2[k])

#print(result3)
print()

#4
li3 = list(['John', 45, 288.5, 'Paul'])
result4 = list()
def string_or_int_def() -> list:
    """
    This function return new list of only string items


    :return: result
    """

for k, y in enumerate(li3):
    if type(y) == str:
        result4.append(li3[k])

#print(result4)
print()


#5
str5 = ('Hello crazy world!')
result5 = list()
def create_li_unique_items() -> list:
    """
    This function return new list of unique items
    in string

    :return: result
    """

my_set = set(str5)

for x in my_set:
    if str5.count(x) == 1:
        result5 +=x

#print(result5)
print()

#6
def create_li_nonun_letter_2str() -> list:
    """
    This function return new list of
    nonunique items 2 strings

    :return: result
    """

str6 = ('Hello crazy world!')
str7 = ('I just wondering how!')
li6 = list(str6)
li7 = list(str7)
result6 = {letter for letter in li6  if li7.count(letter) >= 1}
#print (result6)
print()

#7
def create_li_nonun_letter_2str_1time() -> list:
    """
    This function return new list of
    nonunique items 2 strings
    but 1 time in each

    :return: result
    """

str6 = ('Hello crazy world!')
str7 = ('I just wondering how!')
li6 = list(str6)
li7 = list(str7)
result7 = {letter for letter in li6  if li7.count(letter) == 1}
#print (result7)
print()
