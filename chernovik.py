import csv

with open('files/test.csv', 'wt') as file:
     writer = csv.DictWriter(file, fieldnames=user.keys(), delimiter=';')
     writer.writeheader()
     writer.writerow(user)


def read_from_csv(filename: str) -> list:
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data


def write_to_csv(filename: str, data: list):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in data:
            writer.writerow(row)


def add_grade_to_stud_list(subj: str):
    student_list = read_from_csv('files/Книга2.csv')
    student_list[0].append(subj)
    for stud_number in range(1, len(student_list)):
        student_list[stud_number].append(randint(1, 13))
    write_to_csv('files/Книга2.csv', student_list)


add_grade_to_stud_list('Физкультура')