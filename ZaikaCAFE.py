
"""print("Welcome to Zaika")
menu = {
    "chowmin" : 70,
    "cold drinks" : 50,
    "chicken rice": 130,
    "biryani" : 140,
    "roasted Chicken" : 250,
    "pasta" : 70,
    "cold Coffee" : 60,
    "chhole rice" : 60,
    "sandwich" : 20
}
print("Our Menu:")
print("-----------------")
total_order = 0
for item,price in menu.items():
    print(f"{item}: Rs.{price}")

next_order = True
while next_order:
    order = input("Which order do you want to order? ").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} is added in your order")
        another_order = input("Which item would you like to add?press(Yes/No)").lower()
        if another_order == 'yes':
           next_order = True
        else:
          next_order = False
    else:
        print(f"{order} is not in the menu")
        another_order = input("Which item would you like to add?press(Yes/No)").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total order is :Rs.{total_order}")"""


print("Welcome in Zaika Cafe")
menu = {
    "pasta" :   60,
    "burger"    :  50,
    "rajma-rice"    :  50,
    "juice" :   40,
    "chowmin"   : 70,
    "cold-drink"    :  50,
    "biryani"   : 70,
    "cold-coffee"   : 60,
    "sandwich"  :    20
}
print("Our Menu:")
print("---------------------")
total_order = 0
for item, price in menu.items():
    print(f"{item} :    Rs.{price}")
next_order = True
while next_order:
    order = input("Enter the name of item you want to add in your order: ").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
    else:
        print(f"{order} is not available")
        another_order = input("Do you want to place another order: yes/no").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is : Rs.{total_order}")