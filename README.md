# ONLIINE-ORDER-DRINK-BY-TOPRATEEEEDDDD
#It greets the user, displays a drink menu with prices (highlighting two best-selling items), and uses a loop to accept orders. The program validates user input, calculates a running total, and finally prints an itemized order summary with the total bill amount.
# CODE TITLE
Online Drink Order by TOPRATEEDDDD
# OVERVIEW OF THE PROJECT
This project is a console-based application designed to simulate a digital ordering system for a beverage shop. It automates the interaction between a customer and the shop by displaying a menu, accepting orders, validating item availability, and calculating the final bill. The system is built to handle multiple item orders in a single session and provides a real-time running total of the costs, ensuring a transparent and efficient user experience.
# FEATURES
Dynamic Menu Display: Automatically formats and prints the available drinks and their prices from a stored dictionary.
User Personalization: Captures and addresses the user by name throughout the session.
Input Validation: Checks if the user's selected drink exists in the menu. If an item is invalid, it prompts the user to check the spelling without crashing.
Case-Insensitivity: Handles user input robustly, allowing customers to type "Expresso", "EXPRESSO", or "expresso" without errors.
Real-time Billing: Maintains a running total of the bill as items are added.
Multiple Item Ordering: Uses a loop to allow customers to order as many drinks as they want in a single session.
Order Summary: Generates a detailed final receipt listing all selected items and the grand total payable.
# TECHNOLOGY/TOOL USED
Programming Language: Python 3.x
Core Concepts:
Dictionaries: For storing menu items and prices efficiently.
Control Flow: while loops for the ordering process and if/else statements for validation.
String Manipulation: Methods like .lower() and .title() for formatting text.
Formatted Strings (f-strings): For clean and dynamic output display.
# Steps to Install & Run the Project
Prerequisites: Ensure you have Python installed on your computer. You can download it from python.org.
Create the File:
Open a text editor (like Notepad, VS Code, or Sublime Text).
Copy the provided code into the editor.
Save the file with a .py extension, for example: drink_order.py.
Open Terminal/Command Prompt:
Navigate to the folder where you saved the file.
Run the Code:
Type the following command and press Enter:
# Instructions for Testing
To verify the code is working correctly, try the following test scenarios:
Standard Order:
Input: Enter your name (e.g., "John").
Action: When asked for a drink, type cappucchino.
Prompt: When asked to add another item, type yes.
Action: Type kitkat-shake.
Prompt: When asked to add another, type no.
Expected Result: The system should print a summary showing both drinks and a total of Rs200.
Invalid Item Check:
Action: When asked for a drink, type Apple Juice (an item not on the menu).
Expected Result: The system should display: "Your selected item apple juice does not exist in our menu. Please check the spelling."
Case Sensitivity Check:
Action: Type COLD-COFFEE (all uppercase).
Expected Result: The system should successfully recognize the item and add Rs110 to your bill.
Finishing Early:
Action: When asked for a drink, type done.
Expected Result: The loop should end immediately and show the final bill (or 0 if nothing was ordered).
