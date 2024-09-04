menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    subtotal = sum(item['price'] for item in order)
    return subtotal

def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    tax = round(subtotal * 0.15, 2)  # Assuming 15% tax rate
    return tax

def summarize_order(order):
    print_order(order)
    names = [item['name'] for item in order]
    subtotal = sum(item['price'] for item in order)
    total = round(subtotal * (1 + 0.15), 2)
    return names, total

def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: $" + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: $" + str(tax))

    items, total = summarize_order(order)
    print("You have ordered: ", items)
    print("Total bill (including tax) is: $" + str(total))

if __name__ == "__main__":
    main()

