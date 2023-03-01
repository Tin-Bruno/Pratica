sandwich_orders = ['presunto', 'salad', 'bacon', 'cheese', 'meat']
finally_sandwiches = []
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("Sandwich makeing: ", making_sandwich.title())

    finally_sandwiches.append(making_sandwich)
    print("\nFinally sandwiches:")

    for finally_sandwich in finally_sandwiches:
        print(finally_sandwich.title() + " to be served")
