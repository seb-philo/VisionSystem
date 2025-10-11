#include <Servo.h>

#define xAxis A0
#define yAxis A3
#define xMotor 9
#define yMotor 6

int potentiometer_x = 0;
int potentiometer_y = 0;  
int xMotorPos = 90;
int yMotorPos = 90;

Servo servo_x;
Servo servo_y;

void setup(){
  Serial.begin(9600);
  }

void loop()
{
  // mapping potentiometer
  int potentiometer_x = analogRead(xAxis);
  int potentiometer_y = analogRead(yAxis);
  xMotorPos = map(potentiometer_x,0,1023,85,100);
  yMotorPos = map(potentiometer_y,0,1023,85,100);

  Serial.println(xMotorPos);
  Serial.println(yMotorPos);
  
  
  // assigning inputs to motors
  servo_x.attach(xMotor);
  servo_x.write(xMotorPos+3);
  servo_y.attach(yMotor);
  servo_y.write(yMotorPos+3);
}
  
