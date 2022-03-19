

// libraries
#include <LiquidCrystal.h>
String kai;
LiquidCrystal lcd (12, 11, 5, 4, 3, 2);

void setup() {
  
  Serial.begin(9600);
  

lcd.begin (16, 2);



}



void loop() {
   
  if (Serial.available() > 0){  
    lcd.clear();
    kai = Serial.readStringUntil("\n");
    //kal = Serial.parseFloat();
    Serial.print(kal);
    lcd.print(kal);
                       
    

    while (Serial.read() >= 0)  
    
    
    ; // do nothing
    
    
    }

  
  
}
  
  
    
    
      
   
  
  
  
 
