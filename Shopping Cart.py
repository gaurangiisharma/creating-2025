foods=[]
prices=[]
quantities=[]
total_price=0
discount_rate=0.1  # 10% discount
while True:
    food=input("Enter food item (or 'done' to finish): ")
    if food.lower()=='done':
        break
    price=float(input(f"Enter price for {food}: "))
    quantity=int(input(f"Enter quantity for {food}: "))
    foods.append(food)
    prices.append(price)
    quantities.append(quantity)
    total_price+=price*quantity
print("\nShopping Cart Summary:")
print(f"{'Item':<15}{'Price':<10}{'Quantity':<10}{'Total':<10}")
for i in range(len(foods)):
    item_total=prices[i]*quantities[i]
    print(f"{foods[i]:<15}${prices[i]:<9.2f}{quantities[i]:<10}{item_total:<10.2f}")
# Apply discount if total price exceeds $100
if total_price > 100:
    discount=total_price*discount_rate
    total_price-=discount
    print(f"\nDiscount Applied: -${discount:.2f}")
print(f"\nTotal Price: ${total_price:.2f}")