# 🐍 Python Fundamentals – Data Types, Variables & OOP

This repository contains Python programs that demonstrate the **core fundamentals of Python programming**, including:

* Python Variables
* Python Data Types
* Type Conversion
* Operators
* Conditional Statements
* Loops
* Functions
* Object Oriented Programming (OOP)

This project is mainly created for **learning and practice purposes**.

---

# 📚 Topics Covered

## 1. Variables in Python

Variables are used to store data values.

Example:

```python
name = "Abhi"
age = 21
price = 99.5
```

Concepts covered:

* Variable declaration
* Naming rules
* Dynamic typing

---

## 2. Python Data Types

Python supports multiple built-in data types.

### Basic Data Types

* int
* float
* str
* bool

Example:

```python
x = 10        # int
y = 10.5      # float
name = "Python"
is_active = True
```

### Collection Data Types

* list
* tuple
* set
* dictionary

Example:

```python
numbers = [1,2,3,4]
fruits = ("apple","banana")
unique = {1,2,3}
student = {"name":"Abhi","age":21}
```

---

## 3. Type Conversion

Python allows converting one data type into another.

Example:

```python
x = int("10")
y = float(5)
z = str(100)
```

---

## 4. Operators

Python supports different types of operators.

Arithmetic Operators

```
+  -  *  /  %  //  **
```

Comparison Operators

```
==  !=  >  <  >=  <=
```

Logical Operators

```
and  or  not
```

---

## 5. Conditional Statements

Used to make decisions in programs.

Example:

```python
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

## 6. Loops

Loops are used to repeat tasks.

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

# 🧠 Object Oriented Programming (OOP)

OOP is a programming paradigm based on objects and classes.

Concepts covered in this project:

* Classes
* Objects
* Constructors
* Inheritance
* Encapsulation
* Polymorphism

---

## Class and Object Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student("Abhi", 21)
s1.show()
```

---

## Inheritance Example

```python
class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

d = Dog()
d.speak()
d.bark()
```

---

# 📂 Project Structure

```
python-fundamentals/
│
├── variables.py
├── data_types.py
├── operators.py
├── conditions.py
├── loops.py
├── functions.py
├── oop.py
└── README.md
```

---

# ▶️ How to Run

1. Install Python
2. Clone the repository

```
git clone https://github.com/your-username/your-repository-name.git
```

3. Open project folder

```
cd your-repository-name
```

4. Run any file

```
python variables.py
```

---

# 🎯 Purpose of This Repository

This repository is created to:

* Practice Python basics
* Understand programming concepts
* Prepare for interviews
* Help beginners learn Python easily

---

# ⭐ If you like this project

Give this repository a **star on GitHub**.
