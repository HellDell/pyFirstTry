from Student import Student
from Group import Group
from Raised_exeption import GroupLimitError


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
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
assert gr.find_student('Jobs') == st1
print("OK")
gr.delete_student('Taylor')
print(gr) # Only one student
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