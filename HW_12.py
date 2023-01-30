import string

MyFile = "/Users/daria.khaptseva/PycharmProjects/PyBasic/HW11_file.txt"
li = list(['the','sleep'])

def change2_word_file_from_list() -> None:
    """
    This function find word from the given list
    in file and replace it with ****

    :return: none
    """
new_file = open("/Users/daria.khaptseva/PycharmProjects/PyBasic/new_file.txt",'w+')
with open("/Users/daria.khaptseva/PycharmProjects/PyBasic/HW11_file.txt", 'r') as MyFile:
    data = MyFile.read()


import re

data = re.sub(r'(?i)(the|sleep)\b','---', data)

#print(data)
new_file.write(data)

#2
#def words_count_index() -> dict:
    #"""
    #This function return count of
    #each word in file and make it an index

    #:return: result
    #"""

result = dict()
data4 = list()
with open("/Users/daria.khaptseva/PycharmProjects/PyBasic/HW11_file.txt", 'r') as MyFile:
    data2 = MyFile.read()
    data3 = data2.split()                   #dividing by 1 word
    for word in data3:
        for punc in string.punctuation:     #removing punctuation
            if punc in word:
                word = word.replace(punc, '')
        data4.append(word.lower())             #lower case



    for word in data4:                          #creat dict
        counter = 0
        for word2 in data4:
            if word == word2:
                counter = counter + 1

        result.update({word:counter})
    #print('2 -  ', result)

import json

with open("/Users/daria.khaptseva/PycharmProjects/PyBasic/stat.json", 'w') as file2:
    json.dump(result, file2)



#3
import csv


with open("/Users/daria.khaptseva/PycharmProjects/PyBasic/stat.csv", 'wt', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=result.keys(),delimiter=';')
        writer.writeheader()
        writer.writerow(result)







