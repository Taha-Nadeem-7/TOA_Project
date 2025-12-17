# Moore Machine Calculator

This project is a Moore Finite State Machine–based calculator implemented in Python.  
It demonstrates how arithmetic expressions are processed using formal automata concepts rather than traditional parsing techniques.

The project includes:
- A GUI calculator built using Tkinter
- A console-based Moore Machine simulation
- A standalone Windows executable (.exe) for the GUI version
- Explicit state transitions, validation, and output generation

---

## Objective

The objective of this project is to apply Theory of Automata concepts by modeling a calculator as a Moore Machine, where the output depends only on the current state.

---

## Features

- Supports basic arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Supports multi-digit operands
- Detects invalid expressions using a trap state
- Displays the current Moore Machine state in the GUI
- Available in multiple formats:
  - Python script
  - Command-line simulation
  - Standalone Windows executable (.exe)

---

## Moore Machine States

- q0 – Initial state
- q1 – Reading first operand
- q2 – Operator received
- q3 – Reading second operand
- qf / qfinish – Final (output) state
- qt – Trap (invalid expression) state

---

## GUI Version

The GUI version is developed using Tkinter and shows the current Moore Machine state during execution.

## Run using Python:
```bash
python moore_calculator.py
```
## Run Console Version
```bash
The console-based version simulates the same Moore Machine logic using terminal input.
python console_calculator.py
```
## Run using Executable
```bash
- Double-click the provided `.exe` file  
- No Python installation required
```

## Future Enhancements

In future versions, the project aims to:
- Support negative numbers
- Support decimal (floating-point) values
- Extend the Moore Machine to handle more complex expressions
- Add additional mathematical operations
- Improve input validation and overall user experience

---

## Educational Use

This project is intended for academic and educational purposes, particularly for courses related to:
- Theory of Automata
- Finite State Machines
- Moore Machines
- Formal Language Processing

---

## Author

Developed as an academic project for Theory of Automata using Python.

Muhammad Taha Nadeem  
Muhammad Maaz Salem

