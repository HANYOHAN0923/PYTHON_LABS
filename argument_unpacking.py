def printNum(a,b,c):
    print(a)
    print(b)
    print(c)
    return 0

list_x = [10,20,30]
printNum(*list_x)
printNum(*[10,20,30])

# printNum(*[10,20]) TypeError: print_numbers() missing 1 required positional argument: 'c'

