#include "base_machine.h"
#include "ultra_sonic.h"
#include "Arduino.h"
#include "digital_compass.h"

static int x = -1, y = 2;
static int cur_dir = 0;
static bool on_white = false;
static bool turn_flag = true;
int dir[4][2] = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };

void init_basemachine()
{
	pinMode(IN1, OUTPUT);
	pinMode(IN2, OUTPUT);
	pinMode(IN3, OUTPUT);
	pinMode(IN4, OUTPUT);
	pinMode(ENA, OUTPUT);
	pinMode(ENB, OUTPUT);

	pinMode(VerticalSensor1, INPUT);
	pinMode(VerticalSensor2, INPUT);
	pinMode(VerticalSensor3, INPUT);
	pinMode(VerticalSensor4, INPUT);
	pinMode(HorizonSensor1, INPUT);
	pinMode(HorizonSensor2, INPUT);
	pinMode(HorizonSensor3, INPUT);
	pinMode(HorizonSensor4, INPUT);
}

void motorA(int Speed) // Right
{
	if (Speed >= 0) {
		digitalWrite(IN1, HIGH);
		digitalWrite(IN2, LOW);
		analogWrite(ENA, Speed * RATE / 100);
	}
	else {
		Speed = (-1) * Speed;
		digitalWrite(IN1, LOW);
		digitalWrite(IN2, HIGH);
		analogWrite(ENA, Speed * RATE / 100);
	}
}

void motorB(int Speed) // Left
{
	if (Speed >= 0) {
		digitalWrite(IN3, HIGH);
		digitalWrite(IN4, LOW);
		analogWrite(ENB, Speed * RATE / 100);
	}
	else {
		Speed = (-1) * Speed;
		digitalWrite(IN3, LOW);
		digitalWrite(IN4, HIGH);
		analogWrite(ENB, Speed * RATE / 100);
	}
}

void mystop()
{
	motorA(0);
	motorB(0);
}

void adjust_path()
{
	if (digitalRead(VerticalSensor1) == 0 && digitalRead(VerticalSensor3) == 1) {
		motorA(210);
		motorB(100);
	}
	else if (digitalRead(VerticalSensor1) == 1 && digitalRead(VerticalSensor3) == 0) {
		motorA(90);
		motorB(230);
	}
	else { // straight A:120,B:210
		motorA(120); // Right
		motorB(170); // Left
	}
	if (digitalRead(HorizonSensor2) == 0 && digitalRead(HorizonSensor4) == 0 && !on_white) {
		x = x + dir[cur_dir][0];
		y = y + dir[cur_dir][1];
		on_white = true;
		turn_flag = true;
	}
	else if (digitalRead(HorizonSensor2) == 1 && digitalRead(HorizonSensor4) == 1 && on_white) {
		on_white = false;
	}

}

void turn_left()
{
	int finished_turning = 0; //flag is true when both are black
	bool started_turning = false;
	int start_heading;
	//  mystop();
	//  delay(100);
	if (turn_flag) {
		//Serial.println("HAHAH");
		start_heading = get_heading();
		Serial.print("Start_heading:");
		Serial.println(start_heading);
		motorA(-160);
		motorB(-170);
		delay(10);
		mystop();
		delay(100);
		turn_flag = false;
		/*motorA(190);
		motorB(-190);*/
		while (finished_turning != 2) {//|| measure_distance()>40) //A:170 B:-190
		  //Serial.println(measure_distance());
			if (!started_turning && (abs(start_heading + 360 - get_heading()) % 360) > 45 && (abs(start_heading + 360 - get_heading()) % 360) < 100)
			{
				Serial.print("now heading:");
				Serial.println(get_heading());
				started_turning = true;
			}
			//Serial.println(measure_distance());
			if (started_turning && (digitalRead(VerticalSensor1) == 0 && finished_turning % 2 == 0 || digitalRead(VerticalSensor1) == 1 && finished_turning % 2 == 1)) {
				finished_turning++;
			}
			motorA(190);
			motorB(-190);
		}
		cur_dir = (cur_dir + 1) % 4;
	}
}

void turn_right()
{
	int flag = 0;
	if (turn_flag) {
		turn_flag = false;
		motorA(-160);
		motorB(-170);
		delay(10);
		mystop();
		delay(100);
		while (flag != 2) {
			if (digitalRead(VerticalSensor3) == 0 && flag % 2 == 0 || digitalRead(VerticalSensor3) == 1 && flag % 2 == 1) {
				flag++;
			}
			motorA(-230);
			motorB(230);
		}
		cur_dir = (cur_dir + 3) % 4;
	}
}

int get_x()
{
	return x;
}

int get_y()
{
	return y;
}

int get_dir() {
	return cur_dir;
}

void set_x(int out_x)
{
	x = out_x;
}

void set_y(int out_y)
{
	y = out_y;
}
