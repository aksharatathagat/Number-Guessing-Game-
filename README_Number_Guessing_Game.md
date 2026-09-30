# Number Guessing Game

## CSE Project

### 1. Project Overview

The **Number Guessing Game** is a simple beginner-level Python project
developed as part of a CSE programming project. The program randomly
selects a number between 1 and 100, and the user has to guess the
selected number.

After every incorrect guess, the program gives a hint by telling the
user whether the entered number is **too low** or **too high**. The game
continues until the user guesses the correct number.

------------------------------------------------------------------------

## 2. Objectives

The main objectives of this project are:

-   To understand the basic syntax of Python.
-   To use Python's `random` module.
-   To understand variables and user input.
-   To implement `if-else` conditional statements.
-   To implement a `while` loop.
-   To create a simple interactive command-line program.
-   To develop basic problem-solving and programming skills.

------------------------------------------------------------------------

## 3. Technologies Used

-   **Programming Language:** Python
-   **Module Used:** `random`
-   **IDE:** Visual Studio Code
-   **Interface:** Command Line / Integrated Terminal

------------------------------------------------------------------------

## 4. How the Program Works

The program follows these basic steps:

1.  Import the `random` module.
2.  Generate a random number between 1 and 100.
3.  Display instructions to the user.
4.  Ask the user to enter a guess.
5.  Compare the guess with the randomly generated number.
6.  If the guess is lower, display **"Your guess is too low."**
7.  If the guess is higher, display **"Your guess is too high."**
8.  Ask the user to enter another guess.
9.  Continue until the correct number is guessed.
10. Display a congratulations message when the user wins.

------------------------------------------------------------------------

## 5. Source Code

``` python
import random

number = random.randint(1, 100)

print("Welcome to the random number generator!")
print("I have chosen a number between 1 and 100.")
print("Try to guess the number.")

guess = int(input("Enter your guess: "))

while guess != number:

    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    guess = int(input("Enter your guess: "))

print("Congratulations!")
print("You guessed the correct number:", number)
```

------------------------------------------------------------------------

## 6. Sample Input and Output

### Sample Run

``` text
Welcome to the random number generator!
I have chosen a number between 1 and 100.
Try to guess the number.
Enter your guess: 30
Your guess is too low.
Enter your guess: 70
Your guess is too high.
Enter your guess: 57
Congratulations!
You guessed the correct number: 57
```

**Note:** The actual correct number changes every time the program is
executed because it is generated randomly.

------------------------------------------------------------------------

## 7. Requirements

To run this project, the following are required:

-   Python 3.x
-   Visual Studio Code or another Python-supported IDE
-   A computer with a command-line terminal

No external Python packages are required because the program uses
Python's built-in `random` module.

------------------------------------------------------------------------

## 8. How to Run

### Step 1: Open the project folder

Open the project folder in Visual Studio Code.

### Step 2: Open the terminal

In VS Code, select:

**Terminal → New Terminal**

### Step 3: Run the program

If the Python file is named `code.py`, enter:

``` text
python code.py
```

If the file is named `guess.py`, enter:

``` text
python guess.py
```

### Step 4: Enter guesses

Enter a number between 1 and 100 whenever the program asks for a guess.

------------------------------------------------------------------------

## 9. Functional Requirements

-   The system should generate a random number between 1 and 100.
-   The system should accept a numerical guess from the user.
-   The system should compare the user's guess with the generated
    number.
-   The system should display whether the guess is too low or too high.
-   The system should continue accepting guesses until the correct
    number is entered.
-   The system should display a congratulations message after a
    successful guess.

------------------------------------------------------------------------

## 10. Non-Functional Requirements

-   The program should be simple and easy to use.
-   The program should provide clear instructions and feedback.
-   The program should respond immediately to user input.
-   The program should use minimal system resources.
-   The source code should be readable and understandable for beginners.

------------------------------------------------------------------------

## 11. Concepts Demonstrated

This project demonstrates the following basic programming concepts:

-   Variables
-   Input and output
-   Data types
-   Random number generation
-   Conditional statements
-   `while` loops
-   Comparison operators
-   User interaction
-   Basic program logic

------------------------------------------------------------------------

## 12. Limitations

The current version of the program has some limitations:

-   It accepts only integer inputs.
-   It does not handle invalid or non-numeric input.
-   It does not count the number of attempts.
-   It does not provide a difficulty level.
-   It does not allow the user to play multiple rounds automatically.

------------------------------------------------------------------------

## 13. Future Enhancements

The project can be improved in the future by adding:

-   Attempt counting.
-   Difficulty levels such as Easy, Medium, and Hard.
-   Input validation for invalid entries.
-   A play-again option.
-   A scoring system.
-   A maximum number of attempts.
-   A graphical user interface (GUI).
-   High-score tracking.

------------------------------------------------------------------------

## 14. Conclusion

The Number Guessing Game is a simple Python project that demonstrates
the practical use of fundamental programming concepts. It helped in
understanding random number generation, conditional logic, loops,
variables, and user input.

Although the project is simple, it provides a good foundation for
developing more advanced Python applications in the future.

------------------------------------------------------------------------

## 15. Author

**CSE Project - Number Guessing Game**

**Language:** Python\
**IDE:** Visual Studio Code
