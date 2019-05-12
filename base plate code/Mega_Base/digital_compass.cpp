#include "QMC5883L.h"
//#include "Wire.h"
#include "Arduino.h"
#include "digital_compass.h"

static QMC5883L compass;

void init_compass()
{
	Wire.begin();

	compass.init();
	compass.setSamplingRate(50);
	
	/*Serial.println("QMC5883L Compass Demo");
	Serial.println("Turn compass in all directions to calibrate....");*/
}

int get_heading()
{
	return compass.readHeading();
}
