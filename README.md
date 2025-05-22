
# LangDesignInterpreter

A Python-based interpreter for a programming language, developed for a Language Design and Implementation module assignment.

---

## 📘 Overview

This project implements an interpreter built in pure Python. It supports:

- Arithmetic operations
- Boolean logic
- Strings
- Variable declarations
- Control flow (`if`, `else`, `while`)
- REPL and file input

---

## 🚀 Getting Started

### Requirements

- Python 3.12+
- Git (optional, for version control)

### Run in REPL mode

```bash
python main.py
```

### Run from `.lox` file

```bash
python main.py all_stages.lox
```

---

## 📂 Project Structure

```
LangDesign/
│
├── main.py              # Entry point with REPL and file handling
├── lditoken.py          # Token and TokenType definitions
├── scanner.py           # Lexical analyser
├── parser.py            # Converts tokens to syntax tree
├── expressions.py       # AST expression classes
├── statements.py        # AST statement classes
├── interpreter.py       # Walks and evaluates the AST
├── all_stages.lox       # Test script for all language features
├── run_tests.bat        # Optional script to run all tests (Windows)
└── README.md            # This file
```

---

## ✅ Features by Stage

| Stage | Feature                       | Example                      |
|-------|-------------------------------|------------------------------|
| 1     | Arithmetic                    | `print (2 + 3) * 4`          |
| 2     | Boolean logic                 | `print true or false`        |
| 3     | Strings                       | `"hi" + " there"`            |
| 4     | Variables                     | `x = 5; print x + 10`        |
| 5     | Control flow                  | `if (x > 1) { print x; }`    |

---

## 🧪 Testing

### Sample Test Code 

```
# Stage 1: Arithmetic
print 2 + 3
print 10 - 4
print 3 * 2
print 8 / 2
print (2 + 3) * 4.5

# Stage 2: Boolean Logic
print true and false
print true or false
print 5 > 2
print 5 <= 5
print 3 < 1
print 2 == 2
print 2 != 3

# Stage 3: Strings
print "hello " + "world"
print "abc" == "abc"
print "a" != "b"

# Stage 4: Variables
x = 5
print x
x = x + 10
print x

msg = "Hi"
msg = msg + " there"
print msg

# Stage 5: Control Flow
name = "admin"
if (name == "admin") {
    print "Welcome back!"
} else {
    print "Access denied."
}

x = 0
while (x < 3) {
    print x
    x = x + 1
}
```

To run:

```bash
python main.py all_stages.lox
```

---

## 👤 Author

- Student ID: `100623586`
- Module: Language Design and Implementation


---

## 📜 License

This interpreter is part of academic coursework and not licensed for distribution outside of educational use.
