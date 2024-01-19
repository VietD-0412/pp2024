student_info = []
student_dictionary = {}


def add_student(students, student_id, dob, name):
    students = {
        'student_id': student_id,
        'name': name,
        'dob': dob,
        'marks': {}
    }
    student_info.append(students)

def add_marks(student_id, name, course_id, students, marks):
   
    for student in students:
        if student['student_id'] == student_id:
            student['marks'][course_id] = marks
            
    else: print(f"Student ID \"{student_id}\" not found")

def get_marks(students, student_id, course_id):
    for student in students:
        if student['student_id'] == student_id:
            marks = student['marks'].get(course_id)
            if marks is not None:
                return marks
            else:
                print(f"No marks found for student ID {student_id} in course ID {course_id}.")
                return None
    print(f"Student with ID {student_id} not found.")
    return None


def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student['student_id']}, Name: {student['name']}")

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course['course_id']}, Name: {course['name']}")
        



















