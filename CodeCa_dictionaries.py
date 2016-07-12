"""
animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": [],
}
print animal_sounds["dog"]
"""

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]
# print students
# print students[0]["name"], students[0]["homework"], students[0]["quizzes"], students[0]["tests"]
# print students[1]["name"], students[1]["homework"], students[1]["quizzes"], students[1]["tests"]
# print students[2]["name"], students[2]["homework"], students[2]["quizzes"], students[2]["tests"]


def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

# numbers = [12, 45, 43, 98, 0, 103]
# print average(numbers)


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    result = (homework * 0.1 + quizzes * 0.3 + tests * 0.6)
    return result
# print get_average(students[0])


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# print get_letter_grade(get_average(students[0]))


def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)


print get_class_average(students)
print get_letter_grade(get_class_average(students))
