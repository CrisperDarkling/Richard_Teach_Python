# Create a list
# literal
print("Literal list 0 to 4")
print([0, 1, 2, 3, 4])


# range function
# A range needs to be turned into a list to print it's contents
print("range 5 as list (0 to 4)")
print(list(range(5)))


# range function start, stop
print("range 3, 8 as list (3 to 7)")
print(list(range(3, 8)))


#range function start, stop, step
print ("range 3, 17, 2 as list (3 to 15)")
print(list(range(3, 17, 2)))


# List comprehension
print("List comprehension i*2 for i in range(10)")
print([i*2 for i in range(10)])


#List comprehension with if
print("List comprehension i*2 for i in range(10) if i is even")
print([i*2 for i in range(10) if i%2==0])


# List Comprehension with Else If
print("FizzBuzz for range 1, 20")
print(["FizzBuzz"   if i%15== 0 
        else "Fizz" if i%3 == 0
        else "Buzz" if i%5 == 0 
        else i for i in range(1,20)])
        

# Nested List Comprehension        
print("Nested List Comprehension (i, j) in i range 3, j range 5")
print ([(i, j) for i in range(3) for j in range(5)])

print("Nested List Comprehension (i, j, i==j) in i range 3, j range 5")
print ([(i, j, i==j) for i in range(3) for j in range(5)])

print("Nested List Comprehension (i, j, i+j==4) in i range 3, j range 5")
print ([(i, j, i+j==4) for i in range(3) for j in range(5)])
