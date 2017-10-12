# if <boolean expression>:
#   <code block>
if 1 == 1:
    print("1 == 1")


# if <boolean expression>:
#   <code block>
# else:
#   <code block>
if 1 == 2:
    print("1 == 2")
else:
    print("1 != 2")


# if <boolean expression>:
#   <code block>
# elif:
#   <code block>
# elif:
#   <code block>
# else:
#   <code block>

# Modify the value of x to see different results
x = 27
if x > 30:
    print("Greater than 30")
elif x > 20:
    print("Greater than 20")
elif x > 10:
    print("Greater than 10")
elif x >= 0:
    print("0 or more")
else:
    print("Negative")
