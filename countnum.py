# Program to count the numbers 
# divisible by Num2 in a given range 

def count(N1,N2,N3): 
	
	# Variable to store the counter 
	counter = 0; 

	# Running a loop from A to B 
	# and check if a number is 
	# divisible by M. 
	for i in range(N1,N2): 
		if (i % N3 == 0): 
			counter = counter + 1

	return counter 

# Driver code 
# A and B define the range, 
# M is the dividend 
N1= int(input("Enter the First Number From Where the count Should Start: "))
N2= int(input("Enter the Last Number Upto  the count Continue: "))
N3= int(input("Enter the Number To Count the Divisibles:  "))

# Printing the result 
print(count
      (N1,N2,N3)) 
