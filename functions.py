
# 1. Create a function add that adds 2 numbers and returns the result
def add(x, y):
    return x + y
    
print(add(5, 3))


# 2. Try calling the function above with two strings, what happens?
print(add("5", "3"))

# 3. Write a function that takes one number, and returns:
#           "Big" if the number is more than 10 
#            or
#           "Small" otherwise
def compare(x):
    if x > 10:
        return "Big"
    else:
        return "Small"
        
print(compare(11))        


# 4. Write a function called are_same that takes two arguments, and returns:
#           True is the arguments are the same
#           False otherwise
def are_same(x, y):
    return x == y

print(are_same(4, 5))

# 5. Write a function called size, that takes 2 arguments x and y.
#           Return "Bigger" if x is greater than y
#           Return "Smaller" if x is less than y
#           Return "Same" if x is equal to y

def size(x, y):
    if x > y:
        return "Bigger"
    
    if x < y:
        return "Smaller"
    
    return "Same"
    
print(size(4, 4))


# Wrap a boolean expression in a function
def is_even(n):
    return n % 2 == 0

print("Is 2 even?")
print(is_even(2))

print("Is 3 even?")
print(is_even(3))

