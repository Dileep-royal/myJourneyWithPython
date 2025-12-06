import math

DISCOUNT_APPLICABLE_AMOUNT = 500
DISCOUNT_RATE = 10
GST_RATE = 5

menu = dict({
    "coffee" : 50,
    "tea" : 30,
    "sandwich" : 180,
    "burger" : 120,
    "pastry" : 60
})

order = dict()

def display_menu(menu:dict):
    print("Item Name" + "|" +"Price")
    for key, value in menu.items():
        print(f"{key} {value} ")

def apply_gst(amount:int) -> int:
    return math.ceil((GST_RATE/100)*amount)

def apply_discount(amount:int) -> int:
    if amount > DISCOUNT_APPLICABLE_AMOUNT:
        return math.ceil((DISCOUNT_RATE/100)*amount)
    else:
        return 0

def display_bill_summary():
    print("-------------------------------------------")
    bill_amount = calculate_total_bill()
    gst_amount = apply_gst(bill_amount)
    discount_amount = apply_discount(bill_amount+gst_amount)
    print("-------------------------------------------")
    print(f"| Total before GST | {bill_amount} |")
    print(f"| After GST {GST_RATE}% | {gst_amount} |")
    print(f"| Discount | {(discount_amount)} |")
    print(f"| Final Bill | {(bill_amount+gst_amount)-discount_amount} |")
    print("-------------------------------------------")

def add_or_update_menu(item_name: str, quantity: int):
    if item_name in order:
        order[item_name] += quantity
    else:
        order[item_name] = quantity

def calculate_total_bill() -> int:
    amount = 0
    print("| Item Name | Quantity | Price | Subtotal |")
    for key, value in order.items():
        subtotal = value*menu[key]
        amount += subtotal
        print(f"| {key} | {order[key]} | {menu[key]} | {subtotal} |")
    return amount

display_menu(menu)

while(1):
    item_name = input("Enter the item name (or) over to complete the order: ")

    if item_name == "over":
        display_bill_summary()
        break

    # check is customer entered item exist in the menu
    if item_name.lower() not in menu:
        print("Entered item spelling is wrong (or) not present in the menu !!")
        continue
 
    item_quantity = int(input("Enter the quantity: "))

    add_or_update_menu(item_name, item_quantity)

    


    


