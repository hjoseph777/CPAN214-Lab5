## CPAN 214 Lab5 – Student Grades Management System

## Project Metadata
- Author: Harry Joseph
- Created: 2025-10-15
- Platform: Python 3.x
- Package Manager: None (standard library only)
- Minimum Python version: 3.6+
- Framework: Object-oriented Python with menu-driven interface

## Overview
CPAN 214 Lab5 implements a menu-driven Python application for managing student records and grades. The system uses object-oriented design with a `Student` class, supports nested dictionary structures for courses, and includes robust error handling and testing. It demonstrates functions/methods, decision structures, classes/objects, dictionary usage, and program testing as per the rubric.

## 📥 Quick Download

**Get the complete project instantly:**

[![Download Lab5](https://img.shields.io/badge/Download-Lab5Zip.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/CPAN214-Lab5/releases/download/v1/Lab5Zip.zip)

[![Download Lab5](https://img.shields.io/badge/Download-Lab5Zip.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/CPAN214-Lab5/releases/download/v1/Lab5Zip.zip)

*Complete Python project with Student Grades Management System ready to run*

## Important: Where your code lives
- The main application is in [`lab5_gradesB.py`](lab5_gradesB.py) with the Student class and menu system
- Automated test inputs are in [`input_all_scenarios.txt`](input_all_scenarios.txt) for end-to-end testing

## Project Structure & Code Reference

An interactive, collapsible view of the codebase with file structure and quick references. Click file names to open them.

<details open>
   <summary><strong>Core Files</strong></summary>

   - 🐍 [`lab5_gradesB.py`](lab5_gradesB.py) – **Main application with Student class and menu system**
   - 📝 [`input_all_scenarios.txt`](input_all_scenarios.txt) – Automated test inputs for all scenarios
</details>

<details>
   <summary><strong>Generated Files</strong></summary>

   - 📁 <strong>__pycache__/</strong> – Python bytecode cache
</details>

### File Structure & Quick Reference

```text
CPAN 214-LAB5/
├── 🐍 lab5_gradesB.py              # Main application script
│   ├── Student class               # Object-oriented student management
│   ├── Menu functions              # Interactive UI (main/sub-menus)
│   └── Error handling              # Input validation & exceptions
├── 📝 input_all_scenarios.txt      # Automated test inputs
│   └── Daisy-chained scenarios     # All test cases in sequence
└── 📁 __pycache__/                 # Python cache
```

| Icon | Type | Path | Purpose |
|------|------|------|---------|
| 🐍 | Script | [`lab5_gradesB.py`](lab5_gradesB.py) | **Main application with Student class and menus** |
| 📝 | Input | [`input_all_scenarios.txt`](input_all_scenarios.txt) | Automated test scenarios |

## Usage Instructions

### Running the Application
1. Ensure Python 3.6+ is installed.
2. Navigate to the project directory.
3. Run: `python lab5_gradesB.py`
4. Follow the menu prompts to browse students, manage records, etc.

### Testing the Application
- **Automated Tests**: Run `python lab5_gradesB.py < input_all_scenarios.txt` to execute all test scenarios automatically.

This covers browsing, viewing details, checking registration, calculating averages, adding/updating courses, and error handling (invalid IDs, grades, statuses, empty names).

## Output

Below is the complete output from running the automated test suite (`python lab5_gradesB.py < input_all_scenarios.txt`):

```
==================================================
 Student Grades Management System 
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): 
 Student Summary:
ID: S001 | Name: Alice Johnson | Avg Grade: 88.50 | Courses: 3
ID: S002 | Name: Bob Smith | Avg Grade: 78.00 | Courses: 2
ID: S003 | Name: Charlie Brown | Avg Grade: 89.50 | Courses: 3
ID: S004 | Name: Diana Prince | Avg Grade: 95.00 | Courses: 1
ID: S005 | Name: Eve Adams | Avg Grade: 88.50 | Courses: 3

==================================================
 Student Grades Management System 
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): ❌ Invalid input. Try again.
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
👤 Student Details:
Name: Alice Johnson
Age: 20
School: Tech University
Year: Junior
Courses:
  - Math 101: Grade 85.00, Status completed
  - Physics 201: Grade N/A, Status ongoing
  - CS 150: Grade 92.00, Status completed

==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5): Enter course name:  Alice Johnson is registered for Math 101.

==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):  Average Grade: 88.50

==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5): Enter course name: Enter grade (0-100 or leave blank for ongoing): Enter status (completed/ongoing):  Course 'New Cour
se' updated successfully.                                                                                                                     
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001): ❌ Student ID not found.
Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
👤 Student Details:
Name: Alice Johnson
Age: 20
School: Tech University
Year: Junior
Courses:
  - Math 101: Grade 85.00, Status completed
  - Physics 201: Grade N/A, Status ongoing
  - CS 150: Grade 92.00, Status completed
  - New Course: Grade 95.00, Status completed

==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5): Enter course name: Enter grade (0-100 or leave blank for ongoing): ❌ Grade must be 0-100 or blank.
Enter grade (0-100 or leave blank for ongoing): Enter status (completed/ongoing):  Course 'Test Course' updated successfully.

==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5): Enter course name: Enter grade (0-100 or leave blank for ongoing): Enter status (completed/ongoing): ❌ Status must be
 'completed' or 'ongoing'.                                                                                                                    Enter status (completed/ongoing):  Course 'Another Course' updated successfully.

==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3): Enter Student ID (e.g., S001):
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5): Enter course name: ❌ Course name cannot be empty.
Enter course name: Enter grade (0-100 or leave blank for ongoing): Enter status (completed/ongoing):  Course 'Test Course2' updated successful
ly.                                                                                                                                           
==================================================
 Managing Alice Johnson (ID: S001)
==================================================
1. View Student Details
2. Check Course Registration
3. Calculate Average Grade
4. Add or Update a Course
5. Back to Main Menu
==================================================
Choose an option (1-5):
==================================================
 Student Grades Management System
==================================================
1. Browse All Students
2. Dive into a Student Record
3. Exit the System
==================================================
Choose an option (1-3):  Thanks for using the system! Goodbye.
```

---

