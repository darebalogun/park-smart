#include <HCSR04.h>// include ultrasonic sensor library

////Ultrasonic initial settings
////Initialize Ultrasonic Sensors and the pins it uses
#define trigPin1 A5//trigger pin for ultrasonic sensor 1 connected to pin A5
#define echoPin1 A4//echo Pin for ultrasonic sensor 1 connected to pin A4
#define trigPin2 2//trigger pin for ultrasonic sensor 2 connected to pin 2
#define echoPin2 3//echo Pin for ultrasonic sensor 2 connected to pin 3


UltraSonicDistanceSensor distanceSensor1(trigPin1, echoPin1);
UltraSonicDistanceSensor distanceSensor2(trigPin2, echoPin2);


double getDistance(int sensor)
{
    if (sensor == 1)
    { 
        return distanceSensor1.measureDistanceCm();
    }
    else if (sensor == 2)
    {
        return distanceSensor2.measureDistanceCm();
    }
}
