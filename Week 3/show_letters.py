# The show_letters function should print out each letter of a word on a separate line. 
# Fill in the blanks to make that happen.

def show_letters(word):
	for i in range (0,len(word)):
		print(word[i])

show_letters("Hello")
# Should print one line per letter