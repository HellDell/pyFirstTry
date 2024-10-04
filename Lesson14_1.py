# let's create a user exception error using previous solution

class GroupLimitError(Exception):

    def __init__(self, message="A group cannot contain more than 10 students!"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'First name: {self.first_name}, last name: ' \
               f'{self.last_name}, age: {self.age}, gender: {self.gender} '


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'First name: {self.first_name}, last name: {self.last_name}, ' \
               f'id student: {self.record_book}'


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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 20, 'Bill', 'Gates', 'AN146')
st4 = Student('Male', 22, 'Mark', 'Zuckerberg', 'AN147')
st5 = Student('Female', 23, 'Ada', 'Lovelace', 'AN148')
st6 = Student('Male', 24, 'Alan', 'Turing', 'AN149')
st7 = Student('Female', 28, 'Grace', 'Hopper', 'AN150')
st8 = Student('Male', 26, 'Elon', 'Musk', 'AN151')
st9 = Student('Female', 24, 'Marie', 'Curie', 'AN152')
st10 = Student('Male', 29, 'Albert', 'Einstein', 'AN153')
st11 = Student('Male', 35, 'Nikola', 'Tesla', 'AN154')
gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True
# gr.delete_student('Taylor')
# print(gr)  # Only one student
# gr.delete_student('Taylor')  # No error!

# adding students
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)

    # trying to add 11th student
    gr.add_student(st11)
except GroupLimitError as e:
    print(e)  # handle an exception and display a message

print(gr)
