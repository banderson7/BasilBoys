#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

int photocellReading;
int photocellPin = 0;


unsigned long sampleTime = 60*5*1000UL;

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{

  Temperature();
  Humidity();
  Photocell();
  delay(2000);
}

void Temperature()
{
  Serial.print("C: ");
  Serial.print(dht.readTemperature());
  Serial.print(",");
  Serial.print("F: ");
  Serial.print(dht.readTemperature(true));
  Serial.print(",");
}

void Humidity()
{
  Serial.print("H: ");
  Serial.print(dht.readHumidity());
  Serial.print(",");
}

void Photocell()
{
  photocellReading = analogRead(photocellPin);
  
  Serial.print("Light: ");
  Serial.println(photocellReading);
} 
