s = [73, 67, 38, 33]

def gradingStudents(grades):
    rounded = []
    for grade in grades:
        if grade > 37:
            nextm = (grade//5 + 1) * 5
            if (nextm - grade) < 3:
                grade = nextm
        rounded.append(grade)

    return(rounded)

print(gradingStudents(s))