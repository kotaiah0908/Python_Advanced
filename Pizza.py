# Introduction to python mocules
# creating a function

def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepparoni')
make_pizza('corn','extracheese','olives')


def make_pizza(size,*toppings):
    """summarize the pizzas are about to make"""
    print(f"\n Mkaing a {size}-inch pizza with the following toppings")

    for topping in toppings:
        print(f" -- {topping}")

make_pizza(12,'corn','tomotos','olives')
make_pizza(16,'extracheese','chicken')

