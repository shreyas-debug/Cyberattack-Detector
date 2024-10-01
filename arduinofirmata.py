import pyfirmata
import pandas as pd
import numpy as np
import time
import serial

board = pyfirmata.Arduino('COM7')
df = pd.read_csv('feeds.csv')
#arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
a = np.array(df['field1'])
b = np.array(df['field2'])
cf=0
cp=0

#def write_read(x):
#    arduino.write(bytes(x, 'utf-8'))
#    time.sleep(1)
#    data = arduino.readline()
#    return data
    

for i in range(len(a)):
    try:
        if float(a[i]) > 0.0:
            cf+=1
            print('0')
            #faultyValues = write_read('0')
            board.digital[9].write(1)
            time.sleep(1)
            #sig = write_read(1)
        else:
            cp+=1
            print('1')
            #passedValues = write_read('1')
            board.digital[9].write(0)
            time.sleep(1)
            
    except:
        pass
#board.digital[9].write(0)
    
print("Passed Packets:",cp)
print("Faulty Packets:",cf)