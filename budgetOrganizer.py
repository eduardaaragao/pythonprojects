# This script in Python takes in the budget you have

print("-=-=-=-=-=-=-=-= Budget Organizer -=-=-=-=-=-=-=-=")

budget = float(input("Please, tell me what is the budget you have: "))
months = int(input("Type in the months of this budget: "))
quantity = int(input("How many categories would you like? "))
categories = {}
for i in range(quantity):
    category = str(input("Type in the category: "))
    percentage = float(input("What is the percentage of this category? (if 30%, type just 30)\n"))
    categories[category] = (budget * (percentage/100))

for x, y in categories.items():
    print(x, y/months)

    print("This will be your monthly budget: \n")

f = open("budget.txt", "a")

f.write("This will be your monthly budget: \n")

for x, y in categories.items():
    f.write(x)
    f.write("\t")
    f.write(str(y/months))
    f.write("\n")


