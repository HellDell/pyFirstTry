from Raised_exeption import GroupLimitError

class Group:

    MAX_STUDENTS = 10  # max student num in a group

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= Group.MAX_STUDENTS:
            raise GroupLimitError()  # raise an exception
        if student not in self.group:  # check for re-addition here
            self.group.append(student)
        else:
            print(f"Student {student.last_name} is already in the group")

    def __str__(self):
        students_str = ""
        for student in self.group:
            students_str += str(student) + "\n"
        return f"Number: {self.number}\n{students_str}"

    def delete_student(self, last_name):
        student_remove = self.find_student(last_name)
        if student_remove:
            self.group.remove(student_remove)

            print(f"Student {student_remove.last_name} deleted")
        else:
            print(f"Student with last name {last_name} not found")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None