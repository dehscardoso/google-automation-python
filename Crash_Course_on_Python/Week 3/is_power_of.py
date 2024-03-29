# Fill in the blanks to make the is_power_of function return whether the number is a 
# power of the given base. Note: base is assumed to be a positive number. Tip: for 
# functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  if number < base:
    return number == 1
  result = number//base
  return is_power_of(result, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False