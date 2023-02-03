
import json

class Employee:
    """
    documentation
    """

    firstname = str()
    lastname = str()
    age = int()
    email = str()
    skills = list()
    people_lang = list()
    coding_lang = list()

    def __init__(self,
                 firstname: str,
                 lastname: str,
                 age: int,
                 email: str,
                 skills: list,
                 people_lang: list,
                 coding_lang: list):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def write_employee_json():
        """


        :return:
        """
        with open("/Users/daria.khaptseva/PycharmProjects/PyBasic/employee2.json", 'w') as file:
            data = {'firstname': firstname,
                    'lastname': self.lastname,
                    'age': self.age,
                    'email': self.email,
                    'skills': self.skills,
                    'people_lang': self.people_lang,
                    'coding_lang': self.coding_lang}

            json.dumps(data,file)



    write_employee_json()



