# Fill in the empty function so that it returns the sum of all the divisors of a number, 
# without including it. A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
  sum = 0
  i = 1
  if n == 0:
    return sum
  else:
    while n > i:
      if n % i == 0:
        sum += i
      i += 1
  return sum

print(sum_divisors(0))   # 0
print(sum_divisors(3))   # 1
print(sum_divisors(36))  # 55
print(sum_divisors(102)) # 114
