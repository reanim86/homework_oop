

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def AverageRating(self):
        aver = 0
        i = 0
        for grade_list in self.grades.values():
            for grade_lec in grade_list:
                aver += grade_lec
                i += 1
        res = aver / i
        return res

    def print_courses_progress(self):
        res = (", ".join(self.courses_in_progress))
        return res

    def print_courses_end(self):
        res = (", ".join(self.finished_courses))
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.AverageRating()}\nКурсы в ' \
              f'процессе изучения: {self.print_courses_progress()}\nЗавершенные курсы: {self.print_courses_end()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.AverageRating() < other.AverageRating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
    def AverageRating(self):
        aver = 0
        i = 0
        for grade_list in self.grades.values():
            for grade_lec in grade_list:
                aver += grade_lec
                i += 1
        res = aver / i
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.AverageRating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.AverageRating() < other.AverageRating()

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def averege_rate_student(students):
    rates_sum = 0
    i = 0
    for student in students:
        for rates in student.grades.values():
            for rate in rates:
                rates_sum += rate
                i += 1
    res = rates_sum / i
    return res

def averege_rate_lector(lectors):
    rates_sum = 0
    i = 0
    for lector in lectors:
        for rates in lector.grades.values():
            for rate in rates:
                rates_sum += rate
                i += 1
    res = rates_sum / i
    return res

cool_lector = Lecturer('Aleksei', 'Kudinov')
cool_lector.courses_attached += ['Python']

loss_lector = Lecturer('Ivan', 'Ivanov')
loss_lector.courses_attached += ['Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в обучение']
best_student.rate_hw(cool_lector, 'Python', 6)
best_student.rate_hw(cool_lector, 'Python', 8)
best_student.rate_hw(loss_lector, 'Git', 8)

loss_student = Student('Vasya', 'Pupkin', 'men')
loss_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(loss_student, 'Python', 9)

list_students = [best_student, loss_student]
list_lector = [cool_lector, loss_lector]


