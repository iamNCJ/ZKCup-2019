import with_Android as Android
import with_LeArm as Arm
import with_Mega_Base as Base
import with_Uno_Dis as Dis
import time


def init():
    Android.init_socket()
    Arm.init_Arm()
    Base.init_Base()
    Dis.init_Uno()


recognize_res = [[], [], [], []]  # DS: 'place'([num]), [res, confidence]
position = [
    [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0)],
    [(9,0), (9,1), (9,2), (9,3), (9,4), (9,5)],
    [(9,9), (8,9), (7,9), (6,9), (5,9), (4,9)],
    [(0,9), (0,8), (0,7), (0,6), (0,5), (0,4)]
]


def recognize():
    Base.start()
    cnt = 0
    while True:
        if Dis.Dis_1() <= 10:
            Base.stop()
            res, conf = Android.get_res()
            cur_dir = Base.get_dir()
            cnt += 1
            # recognize_res.append([cur_dir, cnt, res, conf])
            recognize_res[cur_dir].append([cnt, res, conf])
            if cnt == 3:
                cnt = 0
            # TODO improve store res...
            Base.start()
        if Base.get_pos() == [4, 2]: # len(recognize_res) >= 12 or
            Base.stop()
            break


def put(dir, num, res):
    Base.go_out()
    Base.goto(x, y)  # TODO calculate x,y 1
    # Pick
    if num == 1:
        Arm.LeftPick()
    elif num == 2:
        Arm.MidPick()
    elif num == 3:
        Arm.RightPick()
    # go to put place
    for x,y in positions[dir]:  # TODO calculate x,y 2
        Base.goto(x, y)
        if Dis.Dis_2() >= 10:
            Arm.UpperPut()
        elif Dis.Dis_3() >= 10:
            Arm.LowerPut()
        else:
            continue
    Base.go_in()


if __name__ == '__main__':
    init()
    # time.sleep(10) # Race Requirement
    recognize()

    Base.start()
    while True:
        cur_dir = Base.get_dir()
        if len(recognize_res[cur_dir]):
            obj = recognize_res[cur_dir].pop()
            if obj[1]: # 0 is yellow, an distraction
                put(cur_dir, obj[0], obj[1])