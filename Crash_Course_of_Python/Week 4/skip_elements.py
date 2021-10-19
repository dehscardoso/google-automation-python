# The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. Complete this function to do that, using the for loop 
# to iterate through the input list.

def skip_elements(elements):
	new_list = []
	i = 0
	for i in range(len(elements)):
		if i % 2 == 0:
			new_list.append(elements[i])
			i += 2
	return new_list

	

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


