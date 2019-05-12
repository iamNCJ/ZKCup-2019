#include "base_machine.h"
#include "ultra_sonic.h"
#include "distance_forward.h"


void distance_forward(double dis)
{
	while (true)
	{
		if (measure_distance() < dis)
		{
			mystop();
			break;
		}
		adjust_path();
	}
}
