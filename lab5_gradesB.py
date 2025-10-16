"""
Student Grades Management System – Lab 5
A clean, menu-driven tool for exploring and updating student records.
Designed with clarity, care, and a touch of curiosity.
"""

class Student:
    """A student with personal info and course enrollments."""
    
    def __init__(self, student_id, name, age, school, year, courses=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.school = school
        self.year = year
        self.courses = courses or {}

    def add_or_update_course(self, course, grade=None, status='ongoing'):
        """Add a new course or refresh an existing one."""
        if not course or not isinstance(course, str):
            raise ValueError("Course name must be a non-empty string.")
        if grade is not None and (not isinstance(grade, (int, float)) or not 0 <= grade <= 100):
            raise ValueError("Grade must be a number from 0 to 100, or left blank.")
        if status not in ('completed', 'ongoing'):
            raise ValueError("Status must be either 'completed' or 'ongoing'.")
        self.courses[course] = {'grade': grade, 'status': status}

    def is_registered_for(self, course):
        """Check if this student is taking a given course."""
        return course in self.courses

    def calculate_average(self):
        """Compute the average of completed, graded courses."""
        graded_courses = [
            info['grade'] for info in self.courses.values()
            if info['status'] == 'completed' and info['grade'] is not None
        ]
        return round(sum(graded_courses) / len(graded_courses), 2) if graded_courses else None


# 📚 Preloaded student records for quick exploration
student_database = {
    'S001': Student('S001', 'Alice Johnson', 20, 'Tech University', 'Junior', {
        'Math 101': {'grade': 85.0, 'status': 'completed'},
        'Physics 201': {'grade': None, 'status': 'ongoing'},
        'CS 150': {'grade': 92.0, 'status': 'completed'}
    }),
    'S002': Student('S002', 'Bob Smith', 19, 'Tech University', 'Sophomore', {
        'English 101': {'grade': 78.0, 'status': 'completed'},
        'History 200': {'grade': None, 'status': 'ongoing'}
    }),
    'S003': Student('S003', 'Charlie Brown', 21, 'Tech University', 'Senior', {
        'Biology 300': {'grade': 88.0, 'status': 'completed'},
        'Chemistry 250': {'grade': 91.0, 'status': 'completed'},
        'Art 100': {'grade': None, 'status': 'ongoing'}
    }),
    'S004': Student('S004', 'Diana Prince', 18, 'Tech University', 'Freshman', {
        'Intro to Programming': {'grade': 95.0, 'status': 'completed'}
    }),
    'S005': Student('S005', 'Eve Adams', 22, 'Tech University', 'Graduate', {
        'Advanced Algorithms': {'grade': 87.0, 'status': 'completed'},
        'Machine Learning': {'grade': None, 'status': 'ongoing'},
        'Data Structures': {'grade': 90.0, 'status': 'completed'}
    })
}


def show_menu(title, choices):
    """Render a clean, bordered menu."""
    border = "=" * 50
    print(f"\n{border}")
    print(f" {title} ".center(50))
    print(border)
    for key, desc in choices.items():
        print(f"{key}. {desc}")
    print(border)


def ask_user(prompt, validator=None, error_msg="Hmm, that doesn’t look right. Try again."):
    """Prompt until valid input is received."""
    while True:
        try:
            response = input(prompt).strip()
            if validator and not validator(response):
                raise ValueError(error_msg)
            return response
        except ValueError as ve:
            print(f"⚠️  {ve}")


def main_menu():
    """Launch the main interface loop."""
    options = {
        '1': 'Browse All Students',
        '2': 'Explore a Student’s Record',
        '3': 'Exit'
    }

    while True:
        show_menu("🎓 Student Grades Management System", options)
        choice = ask_user("Pick an option (1–3): ", lambda x: x in options)

        if choice == '1':
            list_all_students()
        elif choice == '2':
            explore_student()
        elif choice == '3':
            print("\nThanks for stopping by! 👋")
            break


def list_all_students():
    """Show a compact roster of all students."""
    print("\n📋 Student Roster:")
    for sid, student in student_database.items():
        avg = student.calculate_average()
        avg_display = f"{avg:.2f}" if avg is not None else "—"
        print(f"• {sid} | {student.name} | Avg: {avg_display} | {len(student.courses)} course(s)")


def explore_student():
    """Drill into a specific student’s data."""
    sid = ask_user(
        "Enter a Student ID (e.g., S001): ",
        lambda x: x in student_database,
        "No student found with that ID."
    )
    student = student_database[sid]

    actions = {
        '1': 'View Full Profile',
        '2': 'Check Course Enrollment',
        '3': 'See Grade Average',
        '4': 'Add or Update a Course',
        '5': 'Back to Main Menu'
    }

    while True:
        show_menu(f"🔍 Managing {student.name} ({sid})", actions)
        action = ask_user("Choose what to do (1–5): ", lambda x: x in actions)

        if action == '1':
            show_profile(student)
        elif action == '2':
            check_enrollment(student)
        elif action == '3':
            show_grade_average(student)
        elif action == '4':
            modify_course(student)
        elif action == '5':
            break


def show_profile(student):
    """Display a student’s full details."""
    print(f"\n👤 {student.name}")
    print(f"   Age: {student.age}")
    print(f"   School: {student.school}")
    print(f"   Year: {student.year}")
    print("   Courses:")
    for course, info in student.courses.items():
        grade = f"{info['grade']:.2f}" if info['grade'] is not None else "—"
        print(f"     • {course} → Grade: {grade}, Status: {info['status']}")


def check_enrollment(student):
    """Ask for a course and report enrollment status."""
    course = ask_user("Course name: ", lambda x: bool(x.strip()), "Course name can’t be empty.")
    enrolled = student.is_registered_for(course)
    status = "is enrolled" if enrolled else "is not enrolled"
    print(f"\n{student.name} {status} in '{course}'.")


def show_grade_average(student):
    """Display the student’s calculated average."""
    avg = student.calculate_average()
    if avg is not None:
        print(f"\n📊 Average Grade: {avg:.2f}")
    else:
        print("\n📊 No completed, graded courses yet.")


def modify_course(student):
    """Add or update a course entry."""
    course = ask_user("Course name: ", lambda x: bool(x.strip()))
    
    grade_input = ask_user(
        "Grade (0–100, or press Enter if ongoing): ",
        lambda x: x == '' or (x.replace('.', '', 1).isdigit() and 0 <= float(x) <= 100),
        "Please enter a valid grade (0–100) or leave blank."
    )
    grade = float(grade_input) if grade_input else None

    status = ask_user(
        "Status (completed/ongoing): ",
        lambda x: x in ('completed', 'ongoing'),
        "Enter 'completed' or 'ongoing'."
    )

    try:
        student.add_or_update_course(course, grade, status)
        print(f"\n✅ Course '{course}' saved successfully!")
    except ValueError as e:
        print(f"❌ Oops! {e}")


# 🚀 Kick things off
if __name__ == "__main__":
    main_menu()