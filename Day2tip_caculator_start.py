#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line
print("Welcome to the digital tip calculator")
total_bill = float(input("What was the total of the bill:"))
percentage = int(input("How much tip would you like to give: 10, 12 or 15?"))
num_people = int(input("How many people were in the dinner"))

after_tip = total_bill * percentage / 100
final_payment = "{:.2f}".format(after_tip / num_people)
print(f"Everyone should be paying: ${final_payment} ")


