def unregister_student(file_path, student_name, course_name):
    # Read contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Set flags
    found_student, found_course = False, False

    # Find student & course
    for i, line in enumerate(lines):
        if line.strip() == f'Student: {student_name}':
            found_student = True
        elif found_student and line.strip() == f'Course: {course_name}':
            lines.pop(i)  # Remove the course line
            found_course = True
            break

    # Write modified data back to the text file
    if found_student and found_course:
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Student '{student_name}' or course '{course_name}' not found.")


def get_students_by_course(file_path, course_name):
    students = []
    current_student = None

    # Read contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Parse data
    for line in lines:
        line = line.strip()

        if line.startswith('Student:'):
            current_student = line.replace('Student: ', '')
        elif line.startswith('Course:') and line.replace('Course: ', '') == course_name:
            students.append(current_student)

    return students


# Test
file_path = 'Student Database\students.txt'
student_name = 'John Doe'
course_name = 'Mathematics'

# Unregister
unregister_student(file_path, student_name, course_name)

# Filter course
course_students = get_students_by_course(file_path, course_name)
print(f"Students registered for {course_name}: {course_students}")
