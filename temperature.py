import sys
import time
import numpy as np
import matplotlib.pyplot as plt

units = input("Inputs units (F,R,C,K): ")
units = units.upper()
if not(units == 'F' or units == 'R' or units == 'C' or units == 'K'):
    print('Invalid inputs'+ units)
    print('Terminating program....')
    sys.exit()

print('Enter temperatures as empty string when done')
stime = np.array([])
stemp = np.array([])
while True:
    # ask for new temperature
    temp = input('Input temperature in ' + units+ ': ')

    # validate temperature input

    try:
        temp = float(temp)
    except:
        break
    # convert the units to K

    if units == 'C':
        temp = temp + 273.15
    elif units == 'F':
        temp = (temp-32.0)*5.0/9.0 + 273.15
    elif units == 'R':
        temp = (temp-32.0)*5.0/9.0

    newTime = time.clock()

    #store the values
    stime = np.append(stime,newTime)
    stemp = np.append(stemp,temp)

plt.plot(stime,stemp,'ro')
plt.xlabel('Time (sec)')
plt.ylabel('Temperature (K) ')
plt.show()
plt.show()

print("Max" + str(np.max(stemp)))
print("Min" + str(np.min(stemp)))
print("Avg" + str(np.mean(stemp)))

                  
    
    
    
