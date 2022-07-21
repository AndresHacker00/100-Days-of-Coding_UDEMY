print("Welcome to treasure island")
print('''
           mm###########mmm
        m####################m
      m#####`"#m m###"""'######
     ######*"  "   "   "mm#######
   m####"  ,             m"#######m
  m#### m*" ,'  ;     ,   "########m
  ####### m*   m  |#m  ;  m ########
 |######### mm#  |####  #m##########|
  ###########|  |######m############
  "##########|  |##################"
   "#########  |## /##############"
     ########|  # |/ m###########
      "#######      ###########"
        """"""       """""""""


''')

answer = input("Where do you wanna go?: Left or Right.\n")

if answer:
    answer == "left"
    print("Perfecto! You can pass")

    answer2 = input("There seems something fishy about the road. Stay or Swim?\n")

    if answer2:
        answer2 == "Stay"
        print("You saw that, there was a big ass Trout!\n")

        answer3 = input("""You have been long on this journey. Congrats but this is the level that will
        define your future. Choose a door: Blue, its blue like the sky, Yellow: Pika, pikaa, Red: Hell\n""")
        
        
        if answer3 == "Blue":
            print("Grhaww, Grhaww", "Game Over, you have been eaten by beasts\n")


        elif answer3 == "Yellow":
            print("Lets pass to the side quest")

            answer4  = input("Theres some fruits spilled around the street. Mangos or Banana?")

            if answer4 == "Mangos":
                print("You have won the island")

            if answer4 == "Banana":
                print("Well atleast you can visit us, someday")

    
    else:
        print("You have encountered yourself with the giga Trout, proceed to be the trouts dinner")


else: 
    print("You have fallen on a big ass hole")





