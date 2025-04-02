def calculate_average(grades):
    result = str(round(sum(grades) / len(grades), 2))
    if sum(grades)/len(grades) < 75:
        result += "\nСтатус: Не успешен"
    else:
        result += "\nСтатус: Успешен"
    return result


def average_ball_of_all_students(students):
    result = 0
    n = 0
    for s in students:
        result += sum(s["grades"])
        n += 1
    result /= (3 * n)
    return round(result, 2)


def del_student_with_lowest_grades(students):
    index_counter = 0
    index_of_weekest_student = 0
    sum_grades_of_weekest_student = sum(students[0]["grades"])
    for s in students:
        if sum(s["grades"]) < sum_grades_of_weekest_student:
            sum_grades_of_weekest_student = sum(s["grades"])
            index_of_weekest_student = index_counter
        index_counter +=1
    students.pop(index_of_weekest_student)
    return


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

for s in students:
    print(f"""Cтудент: {s["name"]}
Средний балл: {calculate_average(s["grades"])}""")

print(f"""Средний балл по всем студентам: {average_ball_of_all_students(students)}""")

students.append({"name": "Joe", "grades": [82, 73, 88]})

print(f"""Средний балл по всем студентам после добавления студентки Joe [82, 73, 88]: {average_ball_of_all_students(students)}""")

del_student_with_lowest_grades(students)

print(f"""Средний балл по всем студентам после удаления слабейшего: {average_ball_of_all_students(students)}""")


