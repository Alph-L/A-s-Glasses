import serial
from serial import Serial
import time
import matplotlib
import matplotlib.pyplot as plt
import math

ser = serial.Serial('COM7',9600)
my_time = 5 # length of time desired to read from sensor 
distList = []
angList = []
tList = [] # time values
c= 0

for x in range(0,my_time):
    if(x == 0):
        print('hi')
        read = ser.readline().decode('ascii').strip()

    else:
        read = ser.readline().decode('ascii').strip()
        readArray = read.split()

        if(len(readArray) != 2 ):
            print('failed')
        else:            
            print('point')
            dist = readArray[0] #UT
            angle = readArray[1] #UT
        
            distList.append(dist)
            tList.append(c)
            angList.append(angle)
        
            c+=1

    time.sleep(1) # change for more readings (decrease)
    # NEED TO FIGURE OUT TIMING


print(distList)
print(angList)

# plot points (in 2D)

figure = plt.figure()
altView = figure.add_subplot(projection=None)

def convToCart(r, theta):  # theta is in degrees
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    point = [x,y]
    return point 

xValList = []
yValList = []
for i in range(0,len(distList)):
    xToNum = int(float(distList[i]))
    yToNum = int(float(angList[i]))
    pt = convToCart(xToNum,yToNum)
    xValList.append(pt[0])
    yValList.append(pt[1])

for i in range(0,len(xValList)): # cartesian
    altView.scatter(xValList[i],yValList[i], color='red') # cartesian

#for i in range(0, len(distList)): # polar
#    altView.scatter(distList[i],angList[i],color='blue')

print(len(xValList))
plt.show()

