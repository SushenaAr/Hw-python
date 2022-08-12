class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average= []

    def average_(self):
        self.grades_list= []
        for course, number in self.grades.items():
            for i in number:
                self.grades_list.append(i) 
        self.average.append(sum(self.grades_list)/ len(self.grades_list))

    def rate_lecturer(self, name, course, grade):
        if isinstance(name, Lecturer) and course in name.courses_attached and course in self.courses_in_progress:
            if course in name.grades_lec:
                name.grades_lec[course] += [grade]
            else:
                name.grades_lec[course] = [grade]
            if course in grades_lector:
                grades_lector[course] += [grade]
            else:
                grades_lector[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res= (f"Name: {self.name}\nSurname: {self.surname}\nСредняя оценка за домашние задания {self.average}"
            f"\nCourse in progress: {self.courses_in_progress}\nfinished_courses: {self.finished_courses}\n ")
        return res

    def __lt__(self, enemy):
        if not isinstance(enemy, Student):
            print("ошибка")
            return
        return self.average < enemy.average
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}
        self.average = []
    
    def average_(self):
        self.grades_list= []
        for course, number in self.grades_lec.items():
            for i in number:
                self.grades_list.append(i) 
        self.average.append(sum(self.grades_list)/ len(self.grades_list))

    def __str__(self):
        res= f"Name: {self.name}\nSurname: {self.surname}\nСредняя оценка за лекции{self.average}\n "
        return res

    def __lt__(self, enemy):
        if not isinstance(enemy, Lecturer):
            print("ошибка")
            return
        return self.average < enemy.average

       

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            if course in grades_students:
                grades_students[course] += [grade]
            else:
                grades_students[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res= f"Name: {self.name}\nSurname: {self.surname}\n "
        return res
grades_lector= {}
grades_lector_end= {}
grades_students= {}
grades_students_end= {}

def average_all_lector():
    for course, number in grades_lector.items():
           grades_lector_end[course]=sum(number)/ len(number)
    return grades_lector_end

def average_all_students():
    for course, number in grades_students.items():
        grades_students_end[course]=sum(number)/ len(number)
    return grades_students_end


best_student = Student('Ruoy','Eman', 'your_gender')
normal_student= Student("Normal", "student", "gender")
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
normal_student.courses_in_progress += ['Python']

best_reviewer= Reviewer("Best", "Guy")
normal_reviewer = Reviewer('Normal', 'Guy')
normal_reviewer.courses_attached += ['Python']
normal_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('Some', 'Buddy')
best_lecturer = Lecturer("Nick", "jef")
cool_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Python']
 

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 7)
best_student.rate_lecturer(best_lecturer, 'Python', 8)

normal_reviewer.rate_hw(normal_student, 'Python', 10)
normal_reviewer.rate_hw(normal_student, 'Python', 10)
normal_reviewer.rate_hw(best_student, 'Python', 8)
normal_reviewer.rate_hw(best_student, 'Python', 7)
normal_reviewer.rate_hw(best_student, 'Git', 7)
# Перед выполнением принта либо сравнением экземпляров применять метод average_
# так как он находит среднее значение оценок, без него не получилось бы реализовать
# сравнение отдельно от принта(так сказать база):)
normal_student.average_()
best_student.average_()
best_lecturer.average_()
cool_lecturer.average_()

print(normal_student > best_student)
print(cool_lecturer > best_lecturer)

print(normal_student)
print(best_lecturer)
print(normal_reviewer)
# Поставьте пятёрку
print(average_all_lector())
print(average_all_students())