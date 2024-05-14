'''Define a class called student. Display the marks details of top five students using
inheritance.'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class TopFiveStudents(Student):
    def __init__(self, students):
        self.students = students
        super().__init__(None, None)  # Call the constructor of the parent class with dummy values
    
    def display_top_five(self):
        sorted_students = sorted(self.students, key=lambda x: x.marks, reverse=True)
        print("Top Five Students:")
        for i, student in enumerate(sorted_students[:5], start=1):
            print(f"{i}. Name: {student.name}, Marks: {student.marks}")

# Example usage:
if __name__ == "__main__":
    students = [
        Student("Alice", 90),
        Student("Bob", 85),
        Student("Charlie", 95),
        Student("David", 92),
        Student("Eve", 88)
    ]

    top_five_students = TopFiveStudents(students)
    top_five_students.display_top_five()
