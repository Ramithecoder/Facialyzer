/*
  Analog Input
 Demonstrates analog input by reading an analog sensor on analog pin 0 and
 turning on and off a light emitting diode(LED)  connected to digital pin 13. 
 The amount of time the LED will be on and off depends on
 the value obtained by analogRead(). 
 
 The circuit:
 * Potentiometer attached to analog input 0
 * center pin of the potentiometer to the analog pin
 * one side pin (either one) to ground
 * the other side pin to +5V
 * LED anode (long leg) attached to digital output 13
 * LED cathode (short leg) attached to ground
 
 * Note: because most Arduinos have a built-in LED attached 
 to pin 13 on the board, the LED is optional.
 
 
 Created by David Cuartielles
 modified 30 Aug 2011
 By Tom Igoe
 
 This example code is in the public domain.
 
 http://arduino.cc/en/Tutorial/AnalogInput
 
 */

int sensorPin = A0;    // select the input pin for the potentiometer
int infopin = 8;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor
int threshold = 600;

void setup() {
  Serial.begin(9600);
  // declare the ledPin as an OUTPUT:
  pinMode(infopin, OUTPUT);  
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin); 
  if (sensorValue > threshold){
    Serial.println ("Drunk");
    digitalWrite(infopin, HIGH);
  }
  else {
    Serial.println ("Sober");
    digitalWrite(infopin, LOW);
  }
  
  //Serial.println(sensorValue);  
  delay(100);                
}
