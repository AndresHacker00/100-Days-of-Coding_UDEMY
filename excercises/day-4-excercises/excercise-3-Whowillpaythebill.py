import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#num_items = len(names) 

# elementos_random = random.randint(0, num_items - 1)
# persona_pagar = names[elementos_random]


# print(f"La persona ha pagar sera:" + persona_pagar)

persona_pagar = random.choice(names)
print(f"La persona ha pagar es:" + persona_pagar)