def show_start_menu(students):
    while True:
        try:
            number_of_action = int(input(f"""Доступные операции:
1. показать информацию обо всех студентах.
2. добавить нового студента.
3. удалить студента с самым низким средним баллом.
4. выход.
Введите номер операции: """))
            if number_of_action == 1:
                students_information(students)
            elif number_of_action == 2:
                add_new_student(students)
            elif number_of_action == 3:
                del_student_with_lowest_grades(students)
            elif number_of_action == 4:
                print("Выход из программы.")
                break
            else:
                print("Указанный номер не соответствует ни одной операции.")
        except ValueError:
            print("Ошибка: Не верный формат данных!")


def calculate_average(grades):
    return round(sum(grades) / len(grades), 2) if grades else 0


def students_information(students):
    print("\nОбучающиеся студенты:")
    for s in students:
        avg = calculate_average(s["grades"])
        status = "Успешен" if avg >= 75 else "Не успешен"
        print(f"""     Cтудент: {s["name"]}
Средний балл: {avg}
      Статус: {status}""")
    print(f"""
Средний балл по всем студентам: {average_ball_of_all_students(students)}\n""")


def average_ball_of_all_students(students):
    total_grades = sum(len(s["grades"]) for s in students)
    total_sum = sum(sum(s["grades"]) for s in students)
    return round(total_sum / total_grades, 2) if total_grades > 0 else 0


def add_new_student(students):
    name_of_student = input(f"""
Введите имя студента: """)
    while True:
        try:
            grades_of_student = input("Введите оценки через пробелы: ")
            grades_of_student_list = [int(num) for num in grades_of_student.split()]
            if all(0 <= grade <= 100 for grade in grades_of_student_list):
                break
            else:
                print("Ошибка: Оценки должны быть в диапазоне от 0 до 100.")
        except ValueError:
            print("Ошибка: Введите только числа.")
    students.append({"name": name_of_student, "grades": grades_of_student_list})
    print(f"""Cтудент по имени {name_of_student} c оценками {grades_of_student_list} добавлен в список обучающихся.

Средний балл по всем студентам: {average_ball_of_all_students(students)}\n""")


def del_student_with_lowest_grades(students):
    if not students:
        print("Нет студентов для удаления.")
        return
    weakest_student = min(students, key=lambda s: calculate_average(s["grades"]))
    students.remove(weakest_student)
    print(f"\nСтудент {weakest_student['name']} с самым низким средним баллом удален.")
    print(f"""Средний балл по всем студентам: {average_ball_of_all_students(students)}\n""")

students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]


show_start_menu(students)
