# start: students
students = [
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},
    {"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9},
]
# end: students


# start: create_student
def create_student(name, age, gpa, major="Undecided"):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    if not 0.0 <= gpa <= 4.0:
        raise ValueError("GPA must be between 0.0 and 4.0.")
    return {"name": name, "age": age, "gpa": gpa, "major": major}


students = []
students.append(create_student("Alice Johnson", 20, 3.8, "Computer Science"))
students.append(create_student("Bob Martinez", 22, 3.6, "Mathematics"))
students.append(create_student("Charlie Davis", 21, 3.9))  # uses default major
# end: create_student


# start: find_student
def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None


result = find_student(students, "Bob Martinez")
if result:
    print(result)
# end: find_student


# start: group_by_major
by_major = {}
for student in students:
    major = student["major"]
    if major not in by_major:
        by_major[major] = []
    by_major[major].append(student)
# end: group_by_major


# start: json_conversion
import json

json_str = json.dumps(students, indent=2)
print(json_str)

data = json.loads(json_str)
# end: json_conversion
