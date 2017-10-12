
# while <boolean expression>:
#   <code block>

print("Print and increment x, while < 10")
x = 0
while x < 10:
    print(x)
    x += 1
    

print("Keep searching until a prime number is found")

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    
# Change x to change where the search starts from     
x = 1000
while not prime(x):
    x += 1

print("{0} is a prime number".format(x))