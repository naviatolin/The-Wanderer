EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 7874 5906
encoding utf-8
Sheet 1 1
Title "The Wanderer Circuit"
Date "2019-13-09"
Rev ""
Comp "Case Zito"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Motor:Motor_Servo M1_Left
U 1 1 5DF1CDD6
P 1600 2700
F 0 "M1_Left" H 1594 3044 50  0000 C CNN
F 1 "Continuous_Motor_Servo" H 1594 2953 50  0000 C CNN
F 2 "" H 1600 2510 50  0001 C CNN
F 3 "http://forums.parallax.com/uploads/attachments/46831/74481.png" H 1600 2510 50  0001 C CNN
	1    1600 2700
	-1   0    0    -1  
$EndComp
$Comp
L Motor:Motor_Servo M2_Right
U 1 1 5DF1D922
P 1550 3250
F 0 "M2_Right" H 1544 3594 50  0000 C CNN
F 1 "Continuous_Motor_Servo" H 1544 3503 50  0000 C CNN
F 2 "" H 1550 3060 50  0001 C CNN
F 3 "http://forums.parallax.com/uploads/attachments/46831/74481.png" H 1550 3060 50  0001 C CNN
	1    1550 3250
	-1   0    0    -1  
$EndComp
$Comp
L The-Wanderer-rescue:IR_sensor-Raspberry_Pi_2_or_3 U1
U 1 1 5DF263DA
P 3650 2350
F 0 "U1" H 3700 2350 50  0000 L CNN
F 1 "IR_sensor" H 3500 2450 50  0000 L CNN
F 2 "" H 3650 2450 50  0001 C CNN
F 3 "" H 3650 2450 50  0001 C CNN
	1    3650 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 2600 2150 2750
Wire Wire Line
	1900 2600 2150 2600
Wire Wire Line
	2200 2650 2250 2650
$Comp
L power:GND #PWR?
U 1 1 5DF4FBFA
P 4450 1050
F 0 "#PWR?" H 4450 800 50  0001 C CNN
F 1 "GND" H 4455 877 50  0000 C CNN
F 2 "" H 4450 1050 50  0001 C CNN
F 3 "" H 4450 1050 50  0001 C CNN
	1    4450 1050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 2850 2150 3150
Text Label 3950 2800 1    50   ~ 0
5V
Text Label 4250 2450 0    50   ~ 0
3.3V
Wire Wire Line
	4200 2450 4600 2450
Wire Wire Line
	4200 2300 4200 2450
Wire Wire Line
	4500 2150 4500 2200
Wire Wire Line
	4450 2150 4500 2150
$Comp
L Device:Voltage_Divider RN2
U 1 1 5DF3DF89
P 4200 2150
F 0 "RN2" V 3983 2150 50  0000 C CNN
F 1 "Voltage_Divider" V 4074 2150 50  0000 C CNN
F 2 "" V 4675 2150 50  0001 C CNN
F 3 "~" H 4400 2150 50  0001 C CNN
	1    4200 2150
	0    -1   1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5DF37CCA
P 4500 2200
F 0 "#PWR?" H 4500 1950 50  0001 C CNN
F 1 "GND" H 4505 2027 50  0000 C CNN
F 2 "" H 4500 2200 50  0001 C CNN
F 3 "" H 4500 2200 50  0001 C CNN
	1    4500 2200
	1    0    0    -1  
$EndComp
$Comp
L The-Wanderer-rescue:Raspi_Speaker-Raspberry_Pi_2_or_3 LS1
U 1 1 5DF1BB42
P 4400 3250
F 0 "LS1" H 4550 3350 50  0000 L CNN
F 1 "Raspi_Speaker" H 4500 3450 50  0000 C CNN
F 2 "" H 4400 3050 50  0001 C CNN
F 3 "~" H 4390 3200 50  0001 C CNN
	1    4400 3250
	-1   0    0    -1  
$EndComp
$Comp
L The-Wanderer-rescue:Raspberry_Pi_3-Raspberry_Pi_2_or_3 J1
U 1 1 5DF103EF
P 5400 2450
F 0 "J1" H 5400 3931 50  0000 C CNN
F 1 "Raspberry_Pi_3" H 5400 3840 50  0000 C CNN
F 2 "" H 5400 2450 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 5400 2450 50  0001 C CNN
	1    5400 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 2450 3500 2450
Wire Wire Line
	2200 3850 3950 3850
Wire Wire Line
	3350 2650 3400 2650
Wire Wire Line
	2800 3550 3450 3550
Wire Wire Line
	3450 3550 3450 3450
Wire Wire Line
	3450 2400 3500 2400
Wire Wire Line
	3900 2550 3900 1850
Wire Wire Line
	5200 1150 5200 900 
Wire Wire Line
	2700 900  2700 1300
Wire Wire Line
	4450 1000 4450 1050
Text Label 4050 1300 2    50   ~ 0
12V
Text Label 4100 900  0    50   ~ 0
5V
Wire Wire Line
	1900 2700 2050 2700
Connection ~ 2700 1300
Wire Wire Line
	1850 3250 2050 3250
Wire Wire Line
	2050 3250 2050 2700
Connection ~ 2050 2700
$Comp
L power:GND #PWR?
U 1 1 5DFB11C7
P 2100 3600
F 0 "#PWR?" H 2100 3350 50  0001 C CNN
F 1 "GND" H 2105 3427 50  0000 C CNN
F 2 "" H 2100 3600 50  0001 C CNN
F 3 "" H 2100 3600 50  0001 C CNN
	1    2100 3600
	1    0    0    -1  
$EndComp
Text Label 2050 2050 1    50   ~ 0
5V
Wire Wire Line
	2150 2750 2250 2750
Wire Wire Line
	2200 2650 2200 3850
Wire Wire Line
	2050 2700 2050 1300
$Comp
L The-Wanderer-rescue:Arduino_UNO_R3-POE_Elias A1
U 1 1 5DEEA028
P 2800 2450
F 0 "A1" H 2800 1261 50  0000 C CNN
F 1 "Arduino_UNO_R3" H 2800 1170 50  0000 C CIB
F 2 "Module:Arduino_UNO_R3" H 3350 1300 50  0001 L CNN
F 3 "" H 2600 3500 50  0001 C CNN
	1    2800 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 1300 2700 1300
Wire Wire Line
	2150 2850 2250 2850
Wire Wire Line
	1850 3150 2150 3150
Wire Wire Line
	1900 2800 2100 2800
Wire Wire Line
	1850 3350 2100 3350
Wire Wire Line
	2100 2800 2100 3350
Connection ~ 2100 3350
Wire Wire Line
	2100 3350 2100 3600
Text Label 3350 3850 0    50   ~ 0
battOutputPin
Text Label 3950 1850 0    50   ~ 0
cameraPin
Text Label 3450 1850 3    50   ~ 0
battInputPin
$Comp
L power:GND #PWR?
U 1 1 5E00B01D
P 5000 3800
F 0 "#PWR?" H 5000 3550 50  0001 C CNN
F 1 "GND" H 5005 3627 50  0000 C CNN
F 2 "" H 5000 3800 50  0001 C CNN
F 3 "" H 5000 3800 50  0001 C CNN
	1    5000 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 3750 5000 3800
$Comp
L power:GND #PWR?
U 1 1 5E00CC84
P 3550 3450
F 0 "#PWR?" H 3550 3200 50  0001 C CNN
F 1 "GND" H 3555 3277 50  0000 C CNN
F 2 "" H 3550 3450 50  0001 C CNN
F 3 "" H 3550 3450 50  0001 C CNN
	1    3550 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 3450 3450 3450
Connection ~ 3450 3450
Wire Wire Line
	3450 3450 3450 2400
$Comp
L Raspberry_Pi_2_or_3:5V_2A_Voltage_Converter B1
U 1 1 5DF0F40C
P 4300 1500
F 0 "B1" V 4350 1500 50  0000 R CNN
F 1 "5V_2A_Voltage_Converter" V 4500 2050 50  0000 R CNN
F 2 "" H 4300 1500 50  0001 C CNN
F 3 "" H 4300 1500 50  0001 C CNN
	1    4300 1500
	0    -1   1    0   
$EndComp
Wire Wire Line
	3850 1000 4150 1000
Wire Wire Line
	4150 1300 4150 1000
Connection ~ 4150 1000
Wire Wire Line
	4150 1000 4450 1000
Wire Wire Line
	4200 1300 4200 900 
Connection ~ 4200 900 
Wire Wire Line
	4200 900  5200 900 
Wire Wire Line
	4050 1300 3850 1300
$Comp
L power:GND #PWR?
U 1 1 5DF40BC2
P 3550 1950
F 0 "#PWR?" H 3550 1700 50  0001 C CNN
F 1 "GND" H 3555 1777 50  0000 C CNN
F 2 "" H 3550 1950 50  0001 C CNN
F 3 "" H 3550 1950 50  0001 C CNN
	1    3550 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 1300 2700 1400
Wire Wire Line
	3550 1300 3550 1450
Wire Wire Line
	3500 2200 3500 2350
Wire Wire Line
	3000 1400 3750 1400
Text Label 3050 1400 0    50   ~ 0
5V_Arduino
$Comp
L Device:Battery_Cell BT1
U 1 1 5DF2AE3F
P 3850 1100
F 0 "BT1" H 3950 1200 50  0000 L CNN
F 1 "Lipo_battery_12V" H 3900 1100 50  0000 L CNN
F 2 "" V 3850 1160 50  0001 C CNN
F 3 "~" V 3850 1160 50  0001 C CNN
	1    3850 1100
	-1   0    0    1   
$EndComp
$Comp
L Device:Voltage_Divider RN1
U 1 1 5DF40BBC
P 3550 1700
F 0 "RN1" V 3650 1850 50  0000 C CNN
F 1 "Voltage_Divider" V 3424 1700 50  0000 C CNN
F 2 "" V 4025 1700 50  0001 C CNN
F 3 "~" H 3750 1700 50  0001 C CNN
	1    3550 1700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3500 2200 3750 2200
Wire Wire Line
	3750 1400 3750 2200
Wire Wire Line
	3950 2150 3950 3850
Wire Wire Line
	3900 1850 4600 1850
Wire Wire Line
	3350 2550 3900 2550
Wire Wire Line
	3550 1300 3850 1300
Connection ~ 3850 1300
Wire Wire Line
	2700 900  4200 900 
Text Label 3400 1800 1    50   ~ 0
5V
Wire Wire Line
	3400 1700 3400 1850
Wire Wire Line
	3400 1850 3450 1850
Wire Wire Line
	3450 1850 3450 2350
Wire Wire Line
	3450 2350 3400 2350
Wire Wire Line
	3400 2350 3400 2650
$EndSCHEMATC
