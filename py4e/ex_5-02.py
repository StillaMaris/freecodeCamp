'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
 Once “done” is entered, print out the total, count, and average of the numbers. 
 If the user enters anything other than a number, detect their mistake using try and except 
 and print an error message and skip to the next number.
'''
num = 0 
tot = 0.0 

while True:
    sval = input('Enter a number: ') #string value
    if sval == 'done':
        break
    try:
        fval = float(sval) #float value
    except:
        print('Invalid input')
        continue
    num += 1
    tot += fval

print(' Tot\t num\tmean \n', tot, num, tot/num)





    
    


