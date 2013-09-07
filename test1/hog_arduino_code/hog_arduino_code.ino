/*
  Blink
 Turns on an LED on for one second, then off for one second, repeatedly.
 
 This example code is in the public domain.
 */

// Pin 2 has a pump attached.
// give it a name:
int pump_in = 2;
int pump_out = 4;
int incomingbyte;
// set initial boolean status of pump
boolean pump_in_on = false;
boolean pump_out_on = false;

// the setup routine runs once when you press reset:
void setup() {               
  // initialize the serial connection to arduino:
  Serial.begin(115200); 
  // initialize the digital pin as an output.
  pinMode(pump_in, OUTPUT);
  pinMode(pump_out, OUTPUT);  
}

// the loop routine runs over and over again forever:
void loop() {
  // get letter from hog1.py
  if(Serial.available()>0)
  {
    incomingbyte=Serial.read();
  }
  
  // change boolean status of the pumps
  if(incomingbyte == 'U')
  {
    pump_in_on = true;
    pump_out_on = false;
  }
    if(incomingbyte == 'D')
  {
    pump_out_on = true;
    pump_in_on = false;
  }
  if(incomingbyte == 'N')
  {
    pump_out_on = false;
    pump_in_on = false;
  }
  
  // test pump statuses and turn on appropriate arduino pin
  if(pump_in_on == true)
  {
    digitalWrite(pump_in, HIGH);
  }
  if(pump_in_on == false)
  {
    digitalWrite(pump_in, LOW);
  }
  if(pump_out_on == true)
  {
    digitalWrite(pump_out, HIGH);
  }
  if(pump_out_on == false)
  {
    digitalWrite(pump_out, LOW);
  }
  //delay(100000);               // wait for a while - may need this
}
