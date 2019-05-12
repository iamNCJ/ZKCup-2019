#include "ultra_sonic.h"
#include "Arduino.h"

void init_ultrasonic()
{
	pinMode(Trig, OUTPUT);
	pinMode(Echo, INPUT);
}

double measure_distance()
{
	double distance;
	digitalWrite(Trig, LOW);
	delayMicroseconds(2);
	digitalWrite(Trig, HIGH);
	delayMicroseconds(10);
	digitalWrite(Trig, LOW);

	distance = (double(pulseIn(Echo, HIGH))) * 17 / 1000;
	return distance;
}