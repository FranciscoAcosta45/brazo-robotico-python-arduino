#include <Servo.h>

Servo servo1;
Servo servo2;
int posicionX, posicionY;
String data;
byte pos;
void setup() {
  servo1.attach(4);
  servo2.attach(7);
  Serial.begin(9600);
  servo1.write(90);
}

void loop() {
  if(Serial.available()){
      data = Serial.readString();
      pos = data.indexOf(',');
      posicionX = (int)(0.3 * data.substring(0,pos).toFloat());
      posicionY = (int)(0.3 * data.substring(pos+1).toFloat());
      if(posicionX > 0){
          servo1.write(posicionX);
          servo2.write(posicionY);
        }
      delay(1000);  
    }  
    delay(500);
}
