//
// Created by Tao Chiang on 5/3/2019.
//

#include "base_machine.h"

static int x = -1, y = 2;
static int cur_dir = 0;
int dir[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

void adjust_path ()
{
    if (digitalRead (VerticalSensor1) == 0 && digitalRead (VerticalSensor3) == 1) {
        motorA (255);
        motorB (150);
    } else if (digitalRead (VerticalSensor1) == 1 && digitalRead (VerticalSensor3) == 0) {
        motorA (100);
        motorB (255);
    } else { //zhizou A:140,B:225
        motorA (140);//Right
        motorB (225);//Left
    }
}

void turn_left ()
{
    motorA (0);
    motorB (0);
    while (digitalRead (VerticalSensor1) != 0) {
        motorA (190);
        motorB (-210);
    }
    cur_dir++;
}

void turn_right ()
{
    motorA (0);
    motorB (0);
    while (digitalRead (VerticalSensor3) != 0) {
        motorA (-195);
        motorB (165);
    }
    cur_dir--;
}

int get_x ()
{
    return x;
}

int get_y ()
{
    return y;
}

void set_x (int out_x)
{
    x = out_x;
}

void set_y (int out_y)
{
    y = out_y;
}