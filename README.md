# My-First-Automated-ATM
"An automated Python OOP project that simulates real-world banking transactions and test cases (PIN changes, cash withdrawals, and security checks) using separate logic and execution modules
# 🏦 Automated ATM Transaction Simulation System (Pure OOP)

## 👋 About the Project
Hi everyone! I am a beginner learning **Object-Oriented Programming (OOP) in Python** as part of my journey toward building a strong foundation for Data Science. 

Instead of creating a standard interactive script that requires continuous manual user inputs (`input()`), I wanted to build something closer to production software engineering. This project is a fully automated testing pipeline that simulates multiple banking scenarios and validates them instantly.

---

## 📐 Project Architecture & Code Structure
The project is divided into two separate, clean Python modules following professional software design standards:

1. **`atm_account.py` (The Backend Core):** This module contains the main `Atm` class. It manages the user's state (account holder name, private PIN verification, and current balance tracking) using core OOP methods.
2. **`main.py` (The Automation Engine):** This file imports the `Atm` class and automatically runs a sequence of real-world banking test cases to verify if the logic behaves correctly under pressure.

---

## 🧠 Core OOP Concepts I Practiced & Mastered:
- **Class & Object Blueprinting:** Learned how to model a real-world entity (an ATM system) into reusable code frameworks.
- **State Management:** Used the `__init__` constructor and the `self` keyword to dynamically track and update states like `self.balance` across different function scopes.
- **Encapsulation & Bug Fixing:** Debugged method signatures by properly binding parameters with `self`, preparing the structure for strict data protection layouts in my upcoming builds.

---

## 🧪 Simulated Test Cases Included:
When you run the system, it automatically executes and displays logs for the following 5 business scenarios:
* **Initial Setup:** Account creation and initial cash deposit activation.
* **Test 1:** Balance check requests using a valid PIN.
* **Test 2:** Cash withdrawal requests with valid amounts and correct PIN.
* **Test 3:** Security check failure (Simulating an unauthorized person trying a wrong PIN).
* **Test 4:** Overdraft failure (Attempting to withdraw more cash than the current balance).
* **Test 5:** Security lifecycle processing (Modifying the active PIN safely).

---

## 🚀 How to Run the Project Locally
Since this project uses **Pure Python**, you do not need to install any heavy external libraries or dependencies. 

1. Download or clone this repository to your computer.
2. Open your terminal or command prompt inside the project folder.
3. Run the automation pipeline using the following command:

```bash
python main.py
