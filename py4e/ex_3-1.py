sh = input('Enter the Hour:')
sr = input('Enter the Rate:')
try:
    fh = float(sh)
    fr= float(sr)
except:
    print('Error, please enter numeric input')
    quit()
    
if fh > 40:
    reg = 40*fr
    over = (fh-40)*fr*1.5
    xp = reg + over

else:
    xp = fh*fr

print(xp)