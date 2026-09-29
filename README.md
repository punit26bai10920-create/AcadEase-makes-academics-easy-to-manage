ACADEASE: STUDENT MANAGEMENT SYSTEM  

A simple command-line program written in Python for managing student
records. It stores students in memory, lets you add new ones, look them
up by registration number, and find the top scorer.
FEATURES
--------
1. Show all students: lists the names of every student.
2. Add student: enter a name, registration number, branch, and marks
   for four subjects.
3. Search student: look up a student by registration number and view
   their branch and marks.
4. Show highest scorer: finds the student with the highest total marks.
5. Exit: ends the program.
REQUIREMENTS
------------
- Python 3.x (no external libraries needed)

HOW TO RUN
----------
    python main.py

Type a number (1-5) at the prompt and press Enter. The menu keeps
running until you choose 5.


EXAMPLE
-------
Enter your choice:3
Enter the registration number:26BMR10003
Name: Krit
Branch: Robotics and AI
Calculus: 98
CSE: 87
EVs: 90
English: 85


DATA STRUCTURE
--------------
Each student is a dictionary in the "students" list:

    Name                 - Student's name (string)
    Registration number  - Unique ID (string)
    Branch               - Student's branch (string)
    Calculus             - Calculus marks (int)
    CSE                  - CSE marks (int)
    EVs                  - EVs marks (int)
    English              - English marks (int)

The program starts with three sample students: Gagnesh, Punit, and Krit.


LIMITATIONS
-----------
- Data is not saved; added students are lost when the program exits.
- Non-numeric input for the menu or marks crashes the program.
- Duplicate registration numbers are allowed.
- Marks are not range-checked.


POSSIBLE IMPROVEMENTS
---------------------
- Save/load data with a JSON or CSV file.
- Add input validation using try/except.
- Prevent duplicate registration numbers.
- Show full details in "Show all students".
- Add edit and delete options.
