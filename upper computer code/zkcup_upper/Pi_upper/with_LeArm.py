import serial
import time

RESET = [0x55, 0x55, 0x17, 0x03,
         0x06, 0xE8, 0x03, 0x01,
         0xC4, 0x09, 0x02, 0xDC,
         0x05, 0x03, 0x4D, 0x02,
         0x04, 0xF4, 0x01, 0x05,
         0xF4, 0x01, 0x06, 0xDC,
         0x05]
AHEADPOS_1 = [0x55, 0x55, 0x17, 0x03,
              0x06, 0xE8, 0x03, 0x01,
              0xC4, 0x09, 0x02, 0xDC,
              0x05, 0x03, 0x4D, 0x02,
              0x04, 0xF4, 0x01, 0x05,
              0xF4, 0x01, 0x06, 0xDC,
              0x05]
AHEADPOS_2 = [0x55, 0x55, 0x17, 0x03,
              0x06, 0xE8, 0x03, 0x01,
              0x00, 0x07, 0x02, 0xDC,
              0x05, 0x03, 0x9B, 0x06,
              0x04, 0x94, 0x03, 0x05,
              0x5F, 0x07, 0x06, 0xDC,
              0x05]
AHEADPOS_3 = [0x55, 0x55, 0x17, 0x03,
              0x06, 0xE8, 0x03, 0x01,
              0xC4, 0x09, 0x02, 0xDC,
              0x05, 0x03, 0x9B, 0x06,
              0x04, 0x94, 0x03, 0x05,
              0x5F, 0x07, 0x06, 0xDC,
              0x05]

LeArm_ser = None


def init_Arm():
    global LeArm_ser
    try:
        LeArm_ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    except:
        pass


def LeftPick():
    try:
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_1))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_2))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_3))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        return True
    except:
        return False


def MidPick():
    try:
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_1))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_2))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_3))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        return True
    except:
        return False


def RightPick():
    try:
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_1))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_2))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_3))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        return True
    except:
        return False


def UpperPut():
    try:
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_1))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_2))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_3))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        return True
    except:
        return False


def LowerPut():
    try:
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_1))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_2))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(AHEADPOS_3))
        time.sleep(1)
        LeArm_ser.write(serial.to_bytes(RESET))
        time.sleep(1)
        return True
    except:
        return False
