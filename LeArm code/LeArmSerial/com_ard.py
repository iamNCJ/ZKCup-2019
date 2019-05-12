import serial    #import serial module
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1);   #open named port at 9600,1s timeot

#try and exceptstructure are exception handler
try:
  while 1:
    ser.write('s');#writ a string to port
    response = ser.readall();#read a string from port
    print response;
except:
ser.close();


import serial
ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

# try:
while 1:
    # ser.write(b'test')
    ser.write(serial.to_bytes([0x55, 0x55, 0x17, 0x03,
                               0x06, 0xE8, 0x03, 0x01,
                               0xC4, 0x09, 0x02, 0xDC,
                               0x05, 0x03, 0x4D, 0x02,
                               0x04, 0xF4, 0x01, 0x05,
                               0xF4, 0x01, 0x06, 0xDC,
                               0x05]))
    # response = ser.readall()
    # print(response)
# except:
#    ser.close()