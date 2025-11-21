# ONLIINE-ORDER-DRINK-BY-TOPRATEEEEDDDD
#It greets the user, displays a drink menu with prices (highlighting two best-selling items), and uses a loop to accept orders. The program validates user input, calculates a running total, and finally prints an itemized order summary with the total bill amount.
#CODE
print("welcome to Online Drink Order by TOPRATEEEEDDDD!!!!")
name = input("Please enter your name: ")
print(f"what would you like to Drink, {name}? \n\nHERE IS OUR MENU")

menu = {
    'water melon seasonal': 100,
    'pineapple-juice': 100,
    'mix-fruite-juice': 120,
    'orange-juice': 160,
    'cappucchino': 70,
    'expresso': 70,
    'rose-shake': 100,
    'black-current-shake': 100,
    'kitkat-shake': 130,
    'oreo-milk-shake': 140,
    'cold-coffee': 110,
    'cold-coffee-with-icecream': 130,
    'iced-cold-coffee': 120,
}

print("water melon seasonal: Rs100")
print("pineapple-juice: Rs100")
print("mix-fruite-juice: Rs120")
print("orange-juice: Rs160")
print("cappucchino: Rs70")
print("expresso: Rs70")
print("rose-shake: Rs100")
print("black-current-shake: Rs100")
print("kitkat-shake: Rs130  *** MOST SELLING ITEM ***")
print("oreo-milk-shake: Rs140")
print("cold-coffee: Rs110  *** MOST SELLING ITEM ***")
print("cold-coffee-with-icecream: Rs130")
print("iced-cold-coffee: Rs120")

order_total = 0
ordering = True
selected_items = []

while ordering:
    item = input("\nEnter the name of item you would like to drink (or 'done' to finish): ").lower()

    if item == 'done':
        ordering = False
        continue

    if item in menu:
        order_total += menu[item]
        selected_items.append(item)
        print(f"Your item {item} (Rs{menu[item]}) has been added to your order.")
        print(f"Current total is Rs{order_total}.")
    else:
        print(f"Your selected item {item} does not exist in our menu. Please check the spelling.")

    another_order = input("Do you want to add another item? (Yes/No): ").lower()
    if another_order != "yes":
        ordering = False

print("\n--- ORDER SUMMARY ---")
print(f"Hello, {name}.")
print("You ordered the following items:")
for drink in selected_items:
    print(f"- {drink.title()}: Rs{menu[drink]}")
print("---")
print(f"The Final Total amount to PAY is Rs{order_total}.")
print("Thank you for ordering with TOPRATEEEEDDDD!!!!!!")
