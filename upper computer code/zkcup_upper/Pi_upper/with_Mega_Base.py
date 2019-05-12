import serial

Base_ser = None


def init_Base():
    global Base_ser
    try:
        Base_ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    except:
        pass


def stop():
    Base_ser.write(b'stop')


def start():
    Base_ser.write(b'start')


def end():
    Base_ser.write(b'end')


def reset():
    Base_ser.write(b'reset')


def goto(x, y):
    msg = 'goto ' + str(x) + str(y)
    Base_ser.write(serial.to_bytes(msg))


def go_out():
    Base_ser.write(b'go_out')


def go_in():
    Base_ser.write(b'go_in')

def get_pos():
    Base_ser.write(b'get_pos')
    for i in range(0, 5):
        data = Base_ser.read_all()
        if data == '':
            continue
        else:
            msg = str(data)
            x,y = msg.split()
            return [int(x), int(y)]
    return None


def get_dir():
    Base_ser.write(b'get_dir')
    for i in range(0, 5):
        data = Base_ser.read_all()
        if data == '':
            continue
        else:
            msg = str(data)
            return int(msg)
    return None
