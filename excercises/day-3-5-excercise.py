import difflib

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

prueba_extrema = name1 + name2 
lower_cases = prueba_extrema.lower

t = prueba_extrema.count("T")
r = prueba_extrema.count("R")
u = prueba_extrema.count("U")
e = prueba_extrema.count("E")

first_digit = t + r + u + e

l = prueba_extrema.count("L")
o = prueba_extrema.count("O")
v = prueba_extrema.count("V")
e = prueba_extrema.count("E")

second_digit = l+o+v+e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90): 
    print(f"Your score is {score}, You go like mentos and coke")

elif (score > 40) and (score < 60):
    print(f"Your score is {score}, Youre alright together")

else:
    print(f"Your score is {score}")



