'''
Modify the program that prompts the user for the file name so that it prints a funny
message when the user types in the exact file name “na na boo boo”.
The program should behave normally for all other files which exist and don’t exist.
 Here is a sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
'''

fname = input('Enter the file name: ')

if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU! - You have been punk\'d!')
    quit()
try:
    fhandle = open(fname)
except:
    print('Invalid name.')
    quit()

fhandle = open(fname)

count = 0
sums = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        dotpos = line.find(':')
        fnum = float(line[dotpos + 1 : ].rstrip())
        count += 1
        sums += fnum

print('You have ', count, 'files')
print('Average spam confidence:', sums/count)
