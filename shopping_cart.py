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
total_cost=0
quantity=0
price=0
for i in shopping_cart:
    for j in shopping_cart[i]:
        quantity+=shopping_cart[i][j]["quantity"]
        price+=shopping_cart[i][j]["price"]
        total_cost+=quantity*price
print("The total cost of items in the shopping cart is:",total_cost)




CATEGORY=input("ENTER THE CATEGORY:")
ITEM=input("ENTER THE ITEM:")
QUANTITY=int(input("ENTER THE QUANTITY:"))
PRICE=int(input("ENTER THE PRICE:"))
shopping_cart[CATEGORY][ITEM]={"quantity": QUANTITY, "price": PRICE}
print(shopping_cart)

