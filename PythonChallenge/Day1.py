"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

'''
requirement:
1)make those function:
is_on_list
get_x
add_x
remove_x

2)Do not change anything inside of the "DO NOT TOUCH AREA"
'''

'''
result:
Is Wed on 'days' list? True
The fourth item in 'days' is: Thu
['Mon','Tue','Wed','Thu','Fri','Sat','Sun','Sat']
['Tue','Wed','Thu','Fri','Sat','Sun','Sat']
'''

def is_on_list(x, y):
    return y in x

def get_x(x, y):
    return x[y]

def add_x(x, y):
    x.append("Sat")

def remove_x(x, y):
    x.remove(y)
        

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #