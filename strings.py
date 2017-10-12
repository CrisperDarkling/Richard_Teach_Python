
# STRINGS

# Declare a string
s = "ABCDEFGHIJKLM"

# Access an individual character
# Strings are zero based
# First A
print(s[0])
# Last M
print(s[12])

# Slice part of a string
# From character 2 ( the third character, C) up to but not including char 7 (H)
# CDEFG
print(s[2: 7])

# Slice part of a string
# From character 4 ( the fifth character, E) to the end of the string
# EFGHIJKLM
print(s[4:])

# From the start up to but not including character 4 ( the fifth character, E)
# ABCD
print(s[:4])
