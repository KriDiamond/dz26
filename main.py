def calculate_average(grades):
    result = str(round(sum(grades) / len(grades), 2))
    if sum(grades)/len(grades) < 75:
        result += "\nСтатус: Не успешен"
    else:
        result += "\nСтатус: Успешен"
    return result

def check_success(average_grade):
    result = "Успешен"
    if average_grade <75:
        result = "Не успешен"
    return


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

print(students)

for s in students:
    print(f"""Cтудент: {s["name"]}
Средний балл: {calculate_average(s["grades"])}""")