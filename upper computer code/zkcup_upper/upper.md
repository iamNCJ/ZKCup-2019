# 中控杯上位机程序设计

## 工程概述

### 设备列举

| 设备         | 用途                                       | 通信方式   |
| ------------ | ------------------------------------------ | ---------- |
| Android手机  | ML图像识别                                 | socket TCP |
| Arduino Mega | 底盘下位机                                 | Serial串口 |
| 机械臂控制板 | 控制机械臂                                 | Serial串口 |
| Arduino Uno  | 返回超声波测距值，弥补树莓派引脚不够的缺陷 | Serial串口 |

### 程序设计

Android开发：TF + Camera2 API + Socket

下位机：Arduino(C++)

上位机（树莓派）：Python

## 文件树

```bash
.
├── Pi_upper
│   ├── test.py
│   ├── upper_main.py
│   ├── with_Android.py
│   ├── with_LeArm.py
│   ├── with_Mega_Base.py
│   └── with_Uno_Dis.py
└── upper.md
```

## 通信接口

### 1. Android

#### Pi -> Android

Socket `want_res`

#### Android -> Pi

Socket `res + conf`

res使用int类型

conf保留百分制下的小数点后两位

### 2. Mega

#### Pi -> Mega

Serial `stop` -> `mystop()`

Serial `start`

Serial `end`

Serial `reset`

Serial `goto x y` -> `if (get_x() == x && get_y == y()) mystop(); ` 会保证调用时不换内外圈

Serial `go_out` 到外圈

Serial `go_in` 到内圈

Serial `get_pos` 返回x，y坐标

### 3. Uno

Serial `Dis1` -> UltraSonicDistance1()

余下两个同理

2 -> 2

3 -> 3

### 4. LeArm

几个动作组


