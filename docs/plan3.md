1. 木板（40*40
   1. 机械臂
   2. 底盘
   3. 传感器（超声
   4. 控制板、树莓派
2. 超声 5 前后左右(2)
3. 电子罗盘



//  `SonicTurnLeft()` 超声波测距实现左转并走到指定位置

`adjust_path()`

`stop()`

`delay_stop()`

`turn_left()`

`turn_right()`

// `turn_back()`

```c
static x, y;
static cur_dir = 0;
int dir[4][2] = {...}
```

`get_x()`

`get_y()`

// `foward(int n)` 

// `backward(int n)`

`set_x(int out_x)`

```c
static x = -1;
void set_x(int out_x)
{
    x = out_x;
}
```



`set_y(int out_y)`



main() -> Serial…