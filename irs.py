# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 02/08/2018
# Title: irs
# Description: User inputs hours worked, Program converts hours worked multipled by rate, Outputs total wages

hours_worked = float(input('Enter hours worked '))

if (hours_worked > 0 and hours_worked <= 40):
    wage = (10 * hours_worked)

elif (hours_worked > 40 and hours_worked <= 50):
    over_time = (hours_worked - 40)
    wage = (15 * over_time) + (10 * (hours_worked-over_time))

elif (hours_worked > 50):
    over_time = (hours_worked - 40)
    extra_time = (over_time - 10)
    wage = ((hours_worked - over_time) * 10) + ((over_time - extra_time) * 15) + (extra_time * 20)
    
else:
    print ('Invalid input\n'
           'Have a nice day')
    exit()

print ('Total wages for employee $''%.2f' % wage)

##Enter hours worked 35
##Total wages for employee $350.00

##Enter hours worked 42
##Total wages for employee $430.00

##Enter hours worked 68
##Total wages for employee $910.00

##Enter hours worked -12345
##Invalid input
##Have a nice day
