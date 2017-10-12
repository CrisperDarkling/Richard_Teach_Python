
# Sum a list with recursion
def sumlist(l):
    if l == []:
        return 0
    return l[0] + sumlist(l[1:])
    
print(sumlist([1, 2, 3, 4, 5, 6]))


def flatten(l):
    flattened = []
    
    for item in l:
        if type(item) is list:
            flattened += flatten(item)
        else:
            flattened.append(item)
            
    return flattened
    
    
    
print(flatten([1, 2, [3, 4, 5]]))

print(flatten([[[1, 2, 3], [4, 5, 6, 7]], [8], [[9, 10, 11, 12], [13, 14, 15]]]))
