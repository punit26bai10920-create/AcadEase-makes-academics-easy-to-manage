ACADEASE: STUDENT MANAGEMENT SYSTEM
===================================

A simple command-line program written in Python that makes academic records
easy to manage. It stores student details in memory and lets you view, add,
and search students, and find the top scorer.


FEATURES
--------
1. Show all students   - Prints the names of all students in the list
2. Add student         - Adds a new student (name, registration number,
                         branch, Physics and Chemistry marks)
3. Search student      - Looks up a student by registration number and shows
                         name, branch, and marks
4. Show highest scorer - Finds the student with the highest combined
                         Physics + Chemistry marks
5. Exit                - Ends the session


REQUIREMENTS
------------
- Python 3.6 or higher
- No external libraries needed


HOW TO RUN
----------
    python AcadEase_makes_academics_easy_to_manage.py

Then enter the number of the option you want when prompted:

    STUDENT MANAGEMENT SYSTEM
    1. Show all students
    2. Add student
    3.Search student
    4. Show highest scorer
    5. Exit
    Enter your choice:


DATA STRUCTURE
--------------
Each student is stored as a dictionary inside the "students" list:

    {
        'Name': 'Krit',
        'Registration number': '26BMR10003',
        'Branch': 'Robotics and AI',
        'Physics': 98,
        'Chemistry': 87
    }

Pre-loaded students:

    Name     Registration No.   Branch             Physics   Chemistry
    -------  -----------------  -----------------  -------   ---------
    Gagnesh  26BAI19976         AI-ML              50        50
    Punit    26BAI10920         Computer Science   78        68
    Krit     26BMR10003         Robotics and AI    98        87


EXAMPLE USAGE
-------------
Search a student (option 3):

    Enter your choice:3
    Enter the registration number:26BAI10920
    Name: Punit
    Branch: Computer Science
    Physics: 78
    Chemistry: 68


KNOWN ISSUES
------------
This is a beginner project, and a few things still need fixing:

1. Add student crashes (option 2): the code appends to "info_students",
   which doesn't exist. It should append to "students".

2. Search only covers the first 3 students (option 3): it is hard-coded to
   indexes 0, 1, and 2. Any unknown registration number falls into the
   "else" and shows students[3], which raises an error if the list has only
   3 students. Newly added students can't be found.

3. Highest scorer is wrong (option 4): the print statement sits outside the
   loop, so it shows the name of the LAST student in the list rather than
   the one with the top score.

4. Exit doesn't work (option 5): the loop has no "break", so the program
   keeps asking for input. The "Thank You" message is attached to "while"
   via "else" and is never reached.

5. No input validation: entering a non-number at the menu or in the marks
   fields crashes the program.


SUGGESTED IMPROVEMENTS
----------------------
- Search using a loop over "students" instead of fixed indexes, with a
  "student not found" message
- Track the top scorer's name inside the loop for option 4
- Add "break" for option 5
- Wrap number inputs in try/except
- Save data to a file (CSV or JSON) so records persist between runs
- Add more subjects, and options to update or delete students

