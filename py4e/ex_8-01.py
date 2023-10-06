'''
Exercise 1: Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None. 
Then write a function called middle that takes a list and returns a new list that 
contains all but the first and last elements.
'''

x = [1, 2, 3, 4, 5, 6, 7]

def chop(list):
    del list[0]
    del list[-1]

chop(x)
print(x)


def middle(list):
    return list[1:-1]

print(middle(x))