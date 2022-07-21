import random


Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [Rock, Paper, Scissors] 

choice =  int(input("What do you choose: Type 0 for Rock, Type 1 for Paper, Type 2 for Scissor.\n"))
print (options[choice])

cpu = random.randint(0,2) 
print(f"Cpu chose:")
print(options[cpu])

if choice >= 3:
    print("You chose a invalid move")

if choice == 0 and cpu ==1:
    print("You lost")
    
elif choice == 1 and cpu ==0:
    print("You won")

elif choice ==2 and cpu ==1:
    print("You won") 

elif choice == 1 and cpu == 2:
    print("You lost")    

else:
    choice == cpu    
    print("Its a draw")
        
      


    




    
    
    


    






    







