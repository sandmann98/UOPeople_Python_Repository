# Programming Assignment Unit 4

# Python Program

# Return True if x is divisible by y, otherwise False def is_divisible(x, y):
if x % y == 0: return True
else:
return False

# Return True if a is an integer power of b, otherwise False # Expects both arguments to be nonzero
def is_power(a, b):
if a == b: # base case where a/b == 1 return True
elif b == 1: # base case where b == 1 but a does not return False
else:
return is_divisible(a, b) and is_power(a/b, b)

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

