# conversion feet to inches

startFt = float(input('Enter starting value in feet '))

incrFt = float(input('Enter increment value in feet '))

endFt = float(input('Enter end value in feet '))

feet = startFt

print ('feet     inches')

while feet <= endFt:
    inches = feet * 12
    feet = feet + incrFt
    print (feet, '      ', inches)
