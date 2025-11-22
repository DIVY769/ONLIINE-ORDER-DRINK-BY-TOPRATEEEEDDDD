print("Welcome to Online Drink Order by TOPRATEEDDDD")
name = input("Please enter your name: ")
print(f"What would you like to Drink, {name}? \n\nHERE IS OUR MENU")

# Menu Dictionary
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

# Displaying Menu
print("-" * 30)
for item, price in menu.items():
    print(f"{item.title()}: Rs{price}")
print("-" * 30)

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
        print(f"Your item **{item.title()} (Rs{menu[item]})** has been added to your order.")
        print(f"Current total is **Rs{order_total}**.")
    else:
        print(f"Your selected item **{item}** does not exist in our menu. Please check the spelling.")

    if ordering:
        another_order = input("Do you want to add another item? (Yes/No): ").lower()
        if another_order != "yes":
            ordering = False

# Final Bill
print("\n" + "="*10 + " ORDER SUMMARY " + "="*10)
print(f"Hello, **{name}**.")
print("You ordered the following items:")

for drink in selected_items:
    print(f"- {drink.title()}: Rs{menu[drink]}")

print("-" * 30)
print(f"The Final Total amount to PAY is **Rs{order_total}**.")
print("Thank you for ordering with TOPRATEEEDDDD!")