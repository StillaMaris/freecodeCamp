'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
 Once “done” is entered, print out the minimum an maximum of the numbers. 
 If the user enters anything other than a number, detect their mistake using try and except 
 and print an error message and skip to the next number.
'''
largest = None
smallest = None

while True:
    sval = input('Enter a number: ')
    if sval== 'done':
        break
    
    try:
        fval = float(sval)
        if largest == None or fval > largest:
            largest = fval
        if smallest == None or fval < smallest:
            smallest = fval
    except:
        print('Invalid input')
        continue
print('Smallest\t', smallest, '\nLargest\t', largest)