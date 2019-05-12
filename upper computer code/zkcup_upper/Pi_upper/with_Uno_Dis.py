import serial

Uno_ser = None


def init_Uno():
    global Uno_ser
    try:
        Uno_ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    except:
        pass


def Dis_1():
    Uno_ser.write(b'Dis_1')
    for i in range(0, 5):
        data = Uno_ser.read_all()
        if data == '':
            continue
        else:
            dis = int(data)
            return dis
    return None


def Dis_2():
    Uno_ser.write(b'Dis_2')
    for i in range(0, 5):
        data = Uno_ser.read_all()
        if data == '':
            continue
        else:
            dis = int(data)
            return dis
    return None


def Dis_3():
    Uno_ser.write(b'Dis_3')
    for i in range(0, 5):
        data = Uno_ser.read_all()
        if data == '':
            continue
        else:
            dis = int(data)
            return dis
    return None
