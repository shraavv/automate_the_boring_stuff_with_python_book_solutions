import pyinputplus as pyip

total_cost = 0

while True:
    bread_cost = 0
    bread = pyip.inputMenu(['White', 'Wheat', 'Sourdough'])
    if bread.lower() == 'White'.lower():
        bread_cost += 15
    elif bread.lower() == 'Wheat'.lower():
        bread_cost += 20
    elif bread.lower() == 'Sourdough'.lower():
        bread_cost += 25

    protein_cost = 0
    protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'])
    if protein.lower() == 'Chicken'.lower():
        protein_cost += 50
    elif protein.lower() == 'Turkey'.lower():
        protein_cost += 70
    elif protein.lower() == 'Ham'.lower():
        protein_cost += 70
    elif protein.lower() == 'Tofu'.lower():
        protein_cost += 40

    cheese_cost = 0
    cheese = pyip.inputYesNo("Do you want cheese? ")
    if cheese.lower() == "yes":
        cheese_type = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'])
        if cheese_type.lower() == 'Cheddar'.lower():
            cheese_cost += 40
        elif cheese_type.lower() == 'Swiss'.lower():
            cheese_cost += 60
        elif cheese_type.lower() == 'Mozzarella'.lower():
            cheese_cost += 70

    add_cost = 0
    additional = pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato? ")
    if additional.lower() == 'yes':
        add_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
        if add_type.lower() == 'mayo'.lower():
            add_cost += 20
        elif add_type.lower() == 'mustard'.lower():
            add_cost += 30
        elif add_type.lower() == 'lettuce'.lower():
            add_cost += 25
        elif add_type.lower() == 'tomato'.lower():
            add_cost += 30

    total_cost = bread_cost + protein_cost + cheese_cost + add_cost

    num = pyip.inputInt("How many sandwiches do you want? ")
    if num >= 1:
        total_cost *= num
        print('The total cost of your sandwich is ₹',total_cost)
        break
    else:
        print("Invalid input, Please enter a valid number of sandwiches.")
