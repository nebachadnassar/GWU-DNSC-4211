import random

students = [
    "Rodrigo Hache Caro",
    "Garrett Harlow",
    "Carly Knutzen",
    "Andrew Li",
    "Joseph Liebe",
    "Henry Lin",
    "Souad Mahmoud Adam",
    "Manuela Mouafo",
    "Connor O'grady",
    "Varun Pandey",
    "Sam-Haendell Thosiac",
    "Agassi Ton",
    "Aiden Williams"
]

# Shuffle the list of students randomly
random.shuffle(students)

# Divide the students into two groups
group_of_7 = students[:7]
group_of_6 = students[7:]

print("Group of 7:")
for student in group_of_7:
    print(f"- {student}")

print("\nGroup of 6:")
for student in group_of_6:
    print(f"- {student}")
