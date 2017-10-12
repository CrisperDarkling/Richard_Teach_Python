# for <item> in <collection>:
#   <code block>

print("Print and increment x, where x is 0 to 9")
for x in range(10):
    print(x)
    


print("Print even numbers between 0 and 20")
for x in range(0, 20, 2):
    print(x)


print("Use for loop to iterate over a list")
for x in ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]:
    print(x)


print("Nested for loops")
for x in range(5):
    for y in range(3):
        print (x, y)