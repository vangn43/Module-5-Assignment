# Robust Contact Manager

## About the project

For this project, I worked on a Python contact manager that lets users add, find, and delte contacts. The original code had some problewms that could cause trhe program to crash. My goal was to fix those problems and make the program work better when someone enters something wrong.

## What I Fixed

- **Invalid Menu Input:** I used try and except ValueError so the program doesn't frash when someone enters a letter instead of a number.
-  **Missing Contacts:** I used except KeyError so the program doesn't crash when someone tries to find or delete a contact that doesn't exist.
- **Duplicate Contacts:** I added DuplicateContactError to stop users from adding the same contact twice and replacing the original phone number.
- **Unit Tests:** I created six unit tests to make sure that the different parts of the program work correctly.

## Project Files

- `buggy_contacts.py` = The original code before making any changes.
- `contact_manager.py` - The updated code with the errors fixed.
- `test_contact_manager.py` - The file  I used to test my program.
- `README.md` - information about the program and how to run it.

## How to Run the Program

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Type `python contact_manager.py` and press Enter.
5. Choose an option from the menu to add, find, or delete a contact.
6. Enter 4 when you want to exit the program.

## How to Run the Tests

To run the tests, open terminal in the proiject afolder and enter:

    python -m unittest ttest_contact_manager.py

I created six tests to check if the program can add contacts, find contacts, dewlete contacts, and handle contacts that dont exist. I also tested what happens when someone adds the same contact twice.

When I ran the tests, all six passed without any errors.

## YouTube Video:
https://www.youtube.com/watch?v=P57nOyXmvuc
