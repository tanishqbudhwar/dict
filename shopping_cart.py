shopping_cart={
    "groceries": {"milk": {"quantity": 2, "price": 5}, "bread": {"quantity": 1, "price": 3}, "eggs": {"quantity": 12, "price": 0.5}},
    "electronics": {"laptop": {"quantity": 1, "price": 1000}, "headphones": {"quantity": 2, "price": 50}},
    "clothing": {"t-shirt": {"quantity": 3, "price": 20}, "jeans": {"quantity": 2, "price": 40}}
}
# Adding a new item to the groceries category
shopping_cart["groceries"]["chips"]={"quantity": 5, "price": 2}
print(shopping_cart)



#removing an item from the electronics category
shopping_cart["groceries"].pop("milk")
print(shopping_cart)

#calculating the total cost of items in the shopping cart
total_cost = 0
for category in shopping_cart:
    for item in shopping_cart[category]:
        total_cost += shopping_cart[category][item]["quantity"] * shopping_cart[category][item]["price"]
print("The total cost of items in the shopping cart is:", total_cost)


#manually adding content 

CATEGORY = input("ENTER THE CATEGORY:")
ITEM = input("ENTER THE ITEM:")
QUANTITY = int(input("ENTER THE QUANTITY:"))
PRICE = float(input("ENTER THE PRICE:"))

# Check if category exists, if not, create it
if CATEGORY not in shopping_cart:
    shopping_cart[CATEGORY] = {}

shopping_cart[CATEGORY][ITEM] = {"quantity": QUANTITY, "price": PRICE}
print(shopping_cart)

