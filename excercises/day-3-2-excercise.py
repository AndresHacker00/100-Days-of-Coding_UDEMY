height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

square_height  = height * height

bmi = round(weight / square_height) 

if bmi < 18.5:
    print("You are underweight, eat more")

elif bmi < 25:
        print("You have a normal weight, bro")

elif bmi < 30:
    print("You are obese, excercise more often")
elif bmi < 35:
    print("Oink!, you need to stop eating") 

else:
    print("you are clinically, a PIG")




