#08/10/13
#Oliver Tucker-Gehlert
#Prints out lb to kg conversion table from 1 to 20 pounds
#completed 08/10/13

kg=1
lb=2.2
i=1
requested=int(input("To how many places do you wish to know KiloGram to pound conversion: "))

print()
print("KiloGram to Pound weight conversion table for 1 to {0}".format(requested))

print()
print("{0:^6} {1:^6}".format("KG","LB"))
for count in range(20):
    print("{0:^6.f2} {1:^6.f2}".format(kg*i,lb*i))
    i+=1
