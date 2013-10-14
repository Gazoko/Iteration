#14/10/13
#Oliver Tucker-Gehlert
#Asks for number of stars to be displayed per row and number of rows to display.
#Completed 14/10/13

stars=int(input("How many stars do you wish to display: "))
rows=int(input("How many rows do you wish stars to be displayed in: "))

print()
for rows in range(rows):
    print("*"*stars)

