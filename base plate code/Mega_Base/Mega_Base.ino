// Visual Micro is in vMicro>General>Tutorial Mode
// 
/*
    Name:       Mega_Base.ino
 Created:	5/3/2019 2:26:58 PM
 Author:     DESKTOP-MPFK8RB\Tao Chiang
 */

#include "base_machine.h"
#include "ultra_sonic.h"
#include "distance_forward.h"
#include "digital_compass.h"

static String buff = "";
static bool start_flag = false;
void(*resetFunc) (void) = 0;

// The setup() function runs once each time the micro-controller starts
void setup()
{
  init_basemachine();
  init_ultrasonic();
  init_compass();

  Serial.begin(9600);
  Serial.print("Debug Mode\n");

}

void loop()
{
  if (start_flag)
  {
    //    motorA(230);
    //    motorB(-230);

    adjust_path();
//
//    Serial.println(get_x());
	if (get_x() == 3 && get_y() == 2 && get_dir() == 0 || get_x() == 3 && get_y() == 4 && get_dir() == 1 || get_x() == 1 && get_y() == 4 && get_dir() == 2 || get_x() == 1 && get_y() == 2 && get_dir() == 3) {
		//      //   Serial.println(get_x());
		turn_left();
		//      distance_forward(5);
		//      mystop();
		//      delay(10000);
		//     // mystop();
		//     // delay(10000);
			////      mystop();
			//      delay(10000);
			//distance_forward(10.00);
			//delay(10000);
	}
  }
}

void serialEvent() {
  while (Serial.available()) {
    buff = Serial.readString();
    if (buff.substring(0, 6) == "start")
    {
      start_flag = true;
    }
    else if (buff.substring(0, 4) == "end")
    {
      mystop();
      start_flag = false;
      Serial.println("Stoped!");
    }
    else if (buff.substring(0, 6) == "reset")
    {
      mystop();
      start_flag = false;
      Serial.println("Reseted!");
      resetFunc();
    }
  }
}


