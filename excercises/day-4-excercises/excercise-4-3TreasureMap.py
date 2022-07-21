row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# c = int(position[0])
# r  = int(position[1])

# map[c][r] = "x"

horizontal = int(position[0])
vertical = int(position[1])

map[horizontal - 1][vertical -  1] = "x"



print(f"{row1}\n{row2}\n{row3}")
