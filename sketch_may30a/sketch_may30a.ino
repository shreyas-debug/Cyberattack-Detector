#include <SoftwareSerial.h>

SoftwareSerial gsmSerial(10, 11); //RX, TX
int sig;
void setup()
{
   gsmSerial.begin(9600); // Setting the baud rate of GSM Module
   Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
   delay(500);
   Serial.println("Preparing to send SMS");
   SendInitMessage();
   sig = Serial.readString().toInt();
   if (sig){
    SendMessage(); 
   }
   
}

void loop()
{ 
}
void SendInitMessage()
{
   Serial.println("Setting the GSM in text mode");
   gsmSerial.println("AT+CMGF=1\r");
   delay(500);
   Serial.println("Sending SMS to the desired phone number!");
   gsmSerial.println("AT+CMGS=\"+8319459172\"\r");
   // Replace x with mobile number
   delay(500);
   gsmSerial.println("Transmission Started");    // SMS Text
   delay(50);
   gsmSerial.println((char)26);               // ASCII code of CTRL+Z
   delay(500);
}

void SendMessage()
{
   Serial.println("Setting the GSM in text mode");
   gsmSerial.println("AT+CMGF=1\r");
   delay(500);
   Serial.println("Sending SMS to the desired phone number!");
   gsmSerial.println("AT+CMGS=\"+918319459172\"\r");
   // Replace x with mobile number
   delay(500);
   gsmSerial.println("Fault");    // SMS Text
   delay(50);
   gsmSerial.println((char)26);               // ASCII code of CTRL+Z
   delay(500);
}
