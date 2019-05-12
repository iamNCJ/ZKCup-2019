// Visual Micro is in vMicro>General>Tutorial Mode
// 
/*
    Name:       Mega_Base.ino
 Created:	5/3/2019 2:26:58 PM
 Author:     DESKTOP-MPFK8RB\Tao Chiang
 */

#include "base_machine.h"
#include "ultra_sonic.h"
#include "distance_util.h"

static String buff = "";
static bool start_flag = false;
void(*resetFunc) (void) = 0;

// The setup() function runs once each time the micro-controller starts
void setup()
{
  init_basemachine();
  init_ultrasonic();
//  init_compass();

  Serial.begin(9600);
  Serial.print("Debug Mode\n");

}

void loop()
{
  if (start_flag)
  {
    adjust_path();
	if (get_x() == 4 && get_y() == 2 && get_dir() == 0 || get_x() == 3 && get_y() == 4 && get_dir() == 1 || get_x() == 1 && get_y() == 4 && get_dir() == 2 || get_x() == 1 && get_y() == 2 && get_dir() == 3) {
    Serial.println("photo");
    mystop();
    delay(10000);
		turn_left();
    distance_util(1000);
    Serial.println("catch");
    delay(10000);
    back_to_line();
  }
}
}

void serialEvent() 
{
  while (Serial.available()) {
    buff = Serial.readString();
    if (buff.substring(0, 6) == "start")
    {
      delay(10000);
      Serial.println("started");
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
