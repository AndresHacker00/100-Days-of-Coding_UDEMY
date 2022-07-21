from re import L, S


print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")

budget = 0

if size:
    size == "S"
    budget += 15

elif size:
    size == "M"
    budget += 20

elif size:
    size == "L"
    budget += 25

wants_pepperoni = input("Do you want pepperoni? Y or N. That would be $2") 

if wants_pepperoni == 'Y':
    if size == "S":
        budget += 2
    else: 
        budget += 4

wants_cheese= input("Do you want cheese? Y or N. That would be $1") 

if wants_cheese == "Y":
    budget += 2


print(f"That would be a total of {budget}" + "Thank you for visiting us, come back soon!")





