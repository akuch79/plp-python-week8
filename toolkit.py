
import random


# Tool 1: Simple Calculator
# This tool performs basic mathematical calculations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = number1 + number2
            print(f"Result: {number1} + {number2} = {result}")

        elif operation == "2":
            result = number1 - number2
            print(f"Result: {number1} - {number2} = {result}")

        elif operation == "3":
            result = number1 * number2
            print(f"Result: {number1} * {number2} = {result}")

        elif operation == "4":
            if number2 != 0:
                result = number1 / number2
                print(f"Result: {number1} / {number2} = {result}")
            else:
                print("Sorry, you cannot divide by zero.")

        else:
            print("Invalid operation. Please choose 1-4.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# This tool allows users to add, view and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter your task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            print("\nYour Tasks:")

            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select 1-4.")


# Tool 3: Number Guessing Game
# This tool allows users to guess a randomly selected number.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("\n--- NUMBER GUESSING GAME ---")
    print("I have selected a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print(f"Congratulations! You guessed {secret_number} correctly!")
                break

            elif guess < secret_number:
                print("Your guess is too low. Try again!")

            else:
                print("Your guess is too high. Try again!")

            attempts -= 1

            if attempts > 0:
                print(f"You have {attempts} attempts remaining.")

        except ValueError:
            print("Please enter a whole number.")

    if attempts == 0:
        print(f"Game over! The correct number was {secret_number}.")


# Tool 4: Name Formatter
# This tool formats a person's name into title case.
def name_formatter():
    print("\n--- NAME FORMATTER ---")

    full_name = input("Enter your full name: ")

    if full_name.strip():
        formatted_name = full_name.strip().title()
        print(f"Your formatted name is: {formatted_name}")
    else:
        print("Please enter a name.")


# Main program: Displays the menu and runs the selected tool.
def main():
    print("=" * 40)
    print("WELCOME TO MY PERSONAL MINI-TOOLKIT!")
    print("Created by Margaret Akuch Deng")
    print("=" * 40)

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Name Formatter")
        print("5. Quit")
        print("===============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            name_formatter()

        elif choice == "5":
            print("\nThank you for using my Personal Mini-Toolkit!")
            print("Goodbye! Have a wonderful day.")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice.")
            print("Please select an option between 1 and 5.")


# Start the program.
if __name__ == "__main__":
    main()
