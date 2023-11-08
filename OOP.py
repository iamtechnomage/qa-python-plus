class PlatformUser:
    platform_name = "Yandex Practicum"

    def __init__(self, name: str, age: int):
        """
        Default Yandex Practicum user class
        Parent class for students and teachers
            :param name: name of user
            :param age: users age
        """
        self.name = name
        self.age = age

    def get_user_info(self):
        return {"name": self.name,
                "age": self.age}


class Student(PlatformUser):
    def __init__(self, name: str,
                 age: int,
                 student_id: int,
                 student_courses: list = []):
        # super().__init__(name=name,
        #                  age=age)
        self.name = name
        self.age = age
        self.student_id = student_id
        self.student_courses = student_courses

    def enroll_course(self, course_name):
        self.student_courses.append(course_name)

    def get_student_info(self):
        student_main_info = super().get_user_info()
        student_additional_info = {"student_id": self.student_id,
                                   "student_courses": self.student_courses}
        return {**student_main_info, **student_additional_info}


class Teacher(PlatformUser):
    def __init__(self, name: str,
                 age: int,
                 employee_id: int,
                 taught_courses: list = [str]):
        super().__init__(name=name,
                         age=age)
        self.employee_id = employee_id
        self.taught_courses = taught_courses

    def assign_course(self, course):
        self.taught_courses.append(course)

    def get_teacher_info(self):
        teacher_main_info = super().get_user_info()
        teacher_additional_info = {"employee_id": self.employee_id,
                                   "taught_courses": self.taught_courses}
        return {**teacher_main_info, **teacher_additional_info}


class Research:
    def conduct_research(self):
        return f"{self.name} is conducting research!"


class ExpertTeacher(Teacher, Research):
    def __init__(self, name, age, employee_id):
        super().__init__(name=name,
                         age=age,
                         employee_id=employee_id)

    def assign_course(self, course):
        if isinstance(course, Course):
            super().assign_course(course)
            return self
        else:
            return self.conduct_research()


class Course:
    def __init__(self, name):
        self.name: str = name
        self.students: list = [Student]
        self.teacher: Teacher

    @classmethod
    def create_course(cls, name, teacher):
        course = cls(name=name)
        course.teacher = teacher
        return course


if __name__ == "__main__":
    student1 = Student(name="vanya", age=18, student_id=1, student_courses=[])
    print(student1.get_student_info())
