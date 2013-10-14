#14/10/13
#Oliver Tucker-Gehlert
#Calculates factorial for given positive value of n where factorial is n!#
#Completed 14/10/13

##import math

total=0
i=0

print("""I can calulate factorials for you in the format n!
where n is a positive integer""")

print()
n=input("Please enter the value of n you wish to be calculated: ")
factorialRange=n

n=int(n)
##total=math.factorial(n) #This could be used with 'import math' instead of the below for loop
for i in range(1,n):
    n=i*n
print("The value of {0}! is equal to {1}.".format(factorialRange,n))
