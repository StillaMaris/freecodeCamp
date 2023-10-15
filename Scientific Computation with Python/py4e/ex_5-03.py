'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
 Once “done” is entered, print out the minimum an maximum of the numbers. 
 If the user enters anything other than a number, detect their mistake using try and except 
 and print an error message and skip to the next number.
'''

def largest_number(list):
    largest_so_far = None
    for i in list:
        if largest_so_far is None or i > largest_so_far:
            largest_so_far = i
    return largest_so_far

def smallest_number(list):
    smallest = None
    for value in list:
        if smallest is None or value < smallest:
            smallest = value
    return smallest


list_of_number = []
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
        list_of_number.append(fval)
    except:
        print('invalid input')
        continue

#print(list_of_number)

print('min:\t', smallest_number(list_of_number),'\nmax\t',largest_number(list_of_number))
