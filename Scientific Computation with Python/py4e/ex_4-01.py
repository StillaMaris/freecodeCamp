def computepay(hours, rate):
    if hours >40:
        pay = rate * (40 + (hours-40)*1.5)
    else:
        pay = rate * hours
    return pay

sh = input('Enter the Hour:')
sr = input('Enter the Rate:')

try:
    fh = float(sh)
    fr= float(sr)
except:
    print('Error, please enter numeric input')
    quit()

xp = computepay(fh,fr)
    
print(xp)