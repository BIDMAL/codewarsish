from collections import namedtuple
n = 5
Student = namedtuple('Student', 'ID MARKS NAME CLASS')
total = 0
strings = ['1 97 Raymond 7', '2 50 Steven 4', '3 91 Adrian 9', '4 72 Stewart 5', '5 80 Peter 6']
for i in range(n):
    string = strings[i].split()
    Stud = Student(*string)
    total += int(Stud.MARKS)
print(total/n)