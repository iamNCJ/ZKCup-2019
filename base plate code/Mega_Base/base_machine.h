#pragma once
#define ENA 2
#define ENB 3
#define IN1 28
#define IN2 29
#define IN3 39
#define IN4 38
#define VerticalSensor1 44 // V.ǰ��
#define VerticalSensor2 45 // V.����
#define VerticalSensor3 42 // V.ǰ��
#define VerticalSensor4 43 // V.���� 
#define HorizonSensor1  22 // H.ǰ��
#define HorizonSensor2  23 // H.����
#define HorizonSensor3  24 // H.ǰ��
#define HorizonSensor4  25 // H.����
#define RATE 80

void init_basemachine();

void motorA(int Speed);

void motorB(int Speed);

void mystop();

void adjust_path();

void turn_left();

void turn_right();

int get_x();

int get_y();

int get_dir();

void set_x(int out_x);

void set_y(int out_y);
