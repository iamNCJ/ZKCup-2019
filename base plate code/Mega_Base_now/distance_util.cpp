#include "base_machine.h"
#include "ultra_sonic.h"
#include "distance_util.h"


void distance_util(double dis)
{
	while (true)
	{
		if (measure_distance() > dis)
		{
			mystop();
			break;
		}
		adjust_path();
	}
}
