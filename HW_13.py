class Employee:
    """
    documentation
    """
    first_name = str()
    last_name = str()
    email = str()
    skills = list()
    people_lang = list()
    coding_lang = list()

obj = Employee()


#def __init__ (self, first_name: str, last_name: str, age: int, email:str,skills:list, people_lang:list, coding_lang:list):
 #  self.last_name = last_name
  #  self.age = age
   # self.email = email
    #self.skills = skills
  #  self.people_lang = people_lang
   # self.coding_lang = coding_lang
        #print('employee!')

obj = Employee ('Ivan', 'Teles', 27, 'ivanteles@gmail.com', ['working','coding'],['uk','en'],['python','java'])
print(obj)
obj.email='ivanteles@gmail.com'
print(obj.email)






#import json

#with open("/Users/daria.khaptseva/PycharmProjects/PyBasic/employee.json", 'w') as file:
    #json.dump(obj, file)