def show_start_menu(students):
    try:
        number_of_action = int(input(f"""Доступные операции:
1. показать информацию обо всех студентах.
2. добавить нового студента.
3. удалить студента с самым низким средним баллом.
4. выход.
Введите номер операции: """))
        match number_of_action:
            case 1:
                students_information(students)
            case 2:
                add_new_student(students)
            case 3:
                del_student_with_lowest_grades(students)
            case 4:
                return
            case _:
                print("Указанный номер не соответвествует ни одной операци.")
    except ValueError:
        print("Ошибка: Не верный формат данных!")
    finally:
        print('Программа завершила работу.')
    return


def students_information(students):
    print("\n")
    for s in students:
        print(f"""Cтудент: {s["name"]}
Средний балл: {round(sum(s["grades"]) / len(s["grades"]), 2)}
Статус: {"Не успешен" if round(sum(s["grades"]) / len(s["grades"]), 2) < 75 else "Успешен"}""")
    print(f"""Средний балл по всем студентам: {average_ball_of_all_students(students)}
    """)
    show_start_menu(students)
    return


def average_ball_of_all_students(students):
    result = 0
    for s in students:
        result += sum(s["grades"])
    result /= (3 * len(students))
    return round(result, 2)


def add_new_student(students):
    name_of_student = input(f"""
Введите имя студента: """)
    grades_of_student = input("Введите оценки через пробелы: ")
    grades_of_student_list = [int(num) for num in grades_of_student.split()]
    students.append({"name": name_of_student, "grades": grades_of_student_list})
    print(f"""Средний балл по всем студентам: {average_ball_of_all_students(students)}
        """)
    show_start_menu(students)
    return


def del_student_with_lowest_grades(students):
    weakest_student = min(students, key=lambda s: sum(s["grades"]))
    students.remove(weakest_student)
    print(f"\nСтудент с самым низким баллом удален.")
    print(f"""Средний балл по всем студентам: {average_ball_of_all_students(students)}
            """)
    show_start_menu(students)
    return


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]


show_start_menu(students)
