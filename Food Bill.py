# Concession stand program

menu = {"pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}
cart = []
total = 0


print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        qty = int(input(f"What quantity of {food} would you like to add? :"))
        cart.append((food,qty))

print("\n------- YOUR ORDER -------")
print(f"{'Item':9} {'Qty':6} {'Price':8} {'Total':7}")
print("--------------------------")

for food, qty in cart:
    price = menu.get(food)
    item_total = price * qty
    total += item_total
    print(f"{food:10} {qty:<5} ${price:<7.2f} ${item_total:<7.2f}")

print("--------------------------")
print(f"\nGrand Total: ${total:.2f}")
