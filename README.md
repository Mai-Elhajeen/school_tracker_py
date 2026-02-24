# 🎓 Student & Course Management System

A simple Object-Oriented Python application to manage students, courses, and grades using file-based storage.

---

## 📌 Project Overview

This project is a console-based system built with **Python OOP principles** to:

* Register new students
* Create courses
* Assign students to courses
* Store and load data from files
* Calculate student averages
* Display ranked or non-ranked students

The goal of this project is to practice:

* Object-Oriented Programming (OOP)
* File Handling
* Data Modeling
* Error Handling
* Clean Code Structure

---

## 🏗️ Project Structure

```
student_tracker/
│
├── data/
│   ├── students.txt
│   └── courses.txt
│
├── models/
│   ├── human.py
│   ├── student.py
│   └── course.py
│
├── utils/
│   └── file_handler.py
│
└── main.py
```

---

## ⚙️ Features

✅ Add new students with multiple scores

✅ Create new courses

✅ Assign students to courses

✅ Show all students

✅ Show all courses

✅ Display ranked students by average

✅ Persistent storage using `.txt` files

✅ Exception handling for file operations

---

## 🧠 OOP Concepts Used

* Inheritance (`Student` inherits from `Human`)
* Encapsulation (class-based data control)
* Method overriding
* Modular design
* Separation of concerns

---

## 📂 Data Format

### `students.txt`

```
student_id,name,year_of_birth,score1|score2|score3
```

Example:

```
S1,Mai,2002,88|91|79
S2,Ahmad,2001,85|90
```

---

### `courses.txt`

```
course_id,course_name,student_id|student_id|student_id
```

Example:

```
C1,Python,S1|S2
C2,Algorithms,S2
```

---

## ▶️ How to Run the Project

1️⃣ Clone the repository:

```bash
git clone https://github.com/your-username/student-tracker.git
```

2️⃣ Navigate to the project folder:

```bash
cd student-tracker
```

3️⃣ Run the program:

```bash
python main.py
```

---

## 📋 Menu Example

```
1. Show all students
2. Show all courses
3. Show students in class
4. Register a new student
5. Create new class
6. Save and exit
```

---

## 💾 Saving Data

Data is saved automatically when choosing:

```
6 → Save and Exit
```

---

## 📜 License

This project is for educational purposes.
