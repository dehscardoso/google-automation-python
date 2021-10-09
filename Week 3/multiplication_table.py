# The multiplication_table function prints the results of a number passed to it 
# multiplied by 1 through 5. An additional requirement is that the result is not to 
# exceed 25, which is done with the break statement. Fill in the blanks to complete 
# the function to satisfy these conditions.

def multiplication_table(number):
	multiplier = 1
	while multiplier <= 5:
		result = number * multiplier 
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		multiplier += 1

multiplication_table(3)
multiplication_table(5) 
multiplication_table(8)	

