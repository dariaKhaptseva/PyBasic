import encodings
import json
import csv


class Employee:
    """
    documentation
    """

    def __init__(
            self,
            firstname: str,
            lastname: str,
            age: int,
            email: str,
            skills: list,
            people_lang: list,
            coding_lang: list,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def __str__(self):
        return f': {self.firstname}\n{self.lastname}\n{self.age}\n{self.email}\n{self.skills}\n{self.coding_lang}\n{self.people_lang}'


    def write_employee_json(self):
        """
        :return:
        """
        with open("employee.json", 'w') as file:
            data = {
                'firstname': self.firstname,
                'lastname': self.lastname,
                'age': self.age,
                'email': self.email,
                'skills': self.skills,
                'people_lang': self.people_lang,
                'coding_lang': self.coding_lang,
            }

            json.dump(data, file,ensure_ascii=False)

    def write_employee_csv(self):
        """
        :return:
        """
        with open("employee.csv", 'wt', newline="") as file:
            data = {
                'firstname': self.firstname,
                'lastname': self.lastname,
                'age': self.age,
                'email': self.email,
                'skills': self.skills,
                'people_lang': self.people_lang,
                'coding_lang': self.coding_lang,
            }

            writer = csv.DictWriter(file, fieldnames=data.keys(), delimiter=';')
            writer.writeheader()
            writer.writerow(data)


obj = Employee(
    firstname="Ivasik",
    lastname="Telesik",
    age=19,
    email="email@email.com",
    skills=["ходить","кодить"],
    people_lang=["українська", "англійська"],
    coding_lang=["python", "java"],
    )
obj.write_employee_json()
obj.write_employee_csv()
