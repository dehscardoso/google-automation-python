# The following code can lead to an infinite loop. Fix the code so that it can finish 
# successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
  if n != 0:
    while n % 2 == 0:
      n = n / 2
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False