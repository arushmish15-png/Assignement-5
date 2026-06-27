student = {
    "name": "Alice",
    "marks": "85"
}

x = input("enter the student's name:")

if x == student["name"]:
    print(f"{student['name']}'s marks are: {student['marks']}")
else:
    print("student not found")
