def students_information(students):
    for s in students:
        print(f"""Cтудент: {s["name"]}
Средний балл: {round(sum(s["grades"]) / len(s["grades"]), 2)}
Статус: {"Не успешен" if round(sum(s["grades"]) / len(s["grades"]), 2) < 75 else "Успешен"}""")
    return


def average_ball_of_all_students(students):
    result = 0
    for s in students:
        result += sum(s["grades"])
    result /= (3 * len(students))
    return round(result, 2)


def del_student_with_lowest_grades(students):
    weakest_student = min(students, key=lambda s: sum(s["grades"]))
    students.remove(weakest_student)
    return


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

students_information(students)

print(f"""Средний балл по всем студентам: {average_ball_of_all_students(students)}""")

students.append({"name": "Joe", "grades": [82, 73, 88]})

print(f"""Средний балл по всем студентам после добавления студентки Joe [82, 73, 88]: {average_ball_of_all_students(students)}""")

del_student_with_lowest_grades(students)

print(f"""Средний балл по всем студентам после удаления слабейшего: {average_ball_of_all_students(students)}""")


