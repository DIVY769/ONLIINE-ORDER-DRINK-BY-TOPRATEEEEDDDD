# PROBLEM STATEMENT
This response outlines the project details based on the Python code you provided. This breakdown is suitable for inclusion in a project report or documentation file.

Problem Statement
Manual order processing in cafes and beverage shops is prone to errors, particularly in price calculation and order tracking. Employees often need to memorize prices or consult physical menus repeatedly, which slows down service. Furthermore, calculating the total bill manually can lead to arithmetic mistakes, resulting in financial discrepancies and customer dissatisfaction. There is a need for a digital solution that automates menu display, price retrieval, and bill calculation to ensure accuracy and efficiency.
# SCOPE OF THE PROJECT
The scope of the "Online Drink Order by TOPRATEEDDDD" project is to develop a console-based application that simulates a Point of Sale (POS) system for a specific drink menu.
In-Scope:
Displaying a predefined list of beverages with their respective prices.
Allowing users to input their name for a personalized experience.
Accepting user input for drink selection and validating it against the menu.
Calculating the cumulative total cost of all ordered items.
Generating a final order summary (bill) displaying items purchased and the grand total.
Out-of-Scope:
Payment gateway integration (actual money transfer).
Inventory management (tracking stock levels).
Database connectivity (saving order history after the program closes).
Graphical User Interface (GUI).
# TARGET USER
Cafe Staff/Cashiers: Employees who need a quick tool to calculate customer orders without manual math.
Self-Service Kiosk Users: Customers who prefer to interact with a digital terminal to place their own drink orders.
Small Business Owners: Owners of small juice bars or cafes looking for a cost-effective, simple digital ordering prototype.
# HIGH LEVEL FEATURE
Automated Menu Display: The system instantly formats and presents the complete menu with prices upon startup, eliminating the need for physical price lists.
Dynamic Bill Calculation: As users select items, the system updates the total cost in real-time (order_total += menu[item]), providing immediate feedback on current spending.
Input Validation & Error Handling: The application includes logic to check if a requested item exists in the menu dictionary. If a user mistypes an item, the system notifies them ("does not exist in our menu") rather than crashing.
Case-Insensitive Ordering: The system converts all user inputs to lowercase (.lower()), ensuring that typing "Expresso", "EXPRESSO", or "expresso" all result in a successful order.
Order Summary Receipt: At the end of the transaction, the loop terminates and prints a structured summary listing every item ordered (selected_items) alongside the final amount due.
