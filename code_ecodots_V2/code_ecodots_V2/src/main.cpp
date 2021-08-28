#include<Arduino.h>
#include <Nextion.h>
#include<SPI.h>
#include"SD.h"
#include"loadCell.h"
#include"googleSheets.h"
#include<EEPROM.h>
#include<sim868.h>
#include<DHTsensor.h>
#include <ESP32Servo.h>

Servo servo;
String ph_number="";
float Lat=33.9794, Long=73.7772;

#define MQ2_PIN 39

#define relayPIN 19

#define KEY0 "0"
#define KEY1 "1"
#define KEY2 "2"
#define KEY3 "3"
#define KEY4 "4"
#define KEY5 "5"
#define KEY6 "6"
#define KEY7 "7"
#define KEY8 "8"
#define KEY9 "9"
float instWeight=0;
#define ENTERKEY "E"
int smoke=0;
//Things to change
/*
const char * ssid = "Seixas_Net";
const char * password = "Mayum647";
*/
const char * ssid = "Teste";
const char * password = "12345678";
float cum_weight;

// Intervalo de300 millisegundos
int intervalo = 5000;

// Variáveis para o Blynk Without delay
long previousMillis = 0;
long currentMillis = 0;

NexPage page0 = NexPage(0, 0, "page0");

NexText t0 = NexText(0, 14, "t0");
NexText t1 = NexText(0, 3, "t0");
NexText t2 = NexText(0, 4, "t0");

NexHotspot m0    = NexHotspot(0, 2, "key0");
NexHotspot m1    = NexHotspot(0, 3, "key1");
NexHotspot m2    = NexHotspot(0, 4, "key2");
NexHotspot m3    = NexHotspot(0, 5, "key3");
NexHotspot m4    = NexHotspot(0, 6, "key4");
NexHotspot m5    = NexHotspot(0, 7, "key5");
NexHotspot m6    = NexHotspot(0, 8, "key6");
NexHotspot m7    = NexHotspot(0, 9, "key7");
NexHotspot m8    = NexHotspot(0, 10, "key8");
NexHotspot m9    = NexHotspot(0, 11, "key9");
NexHotspot m10    = NexHotspot(0, 12, "keyB");
NexHotspot m11    = NexHotspot(0, 13, "keyS");

NexHotspot m12    = NexHotspot(2, 2, "St_We");
NexHotspot m13    = NexHotspot(3, 2, "Co_We");

int number = 50;
char buffer[10] = {0};
unsigned long entry;
bool keyPressed = true, enterKeyPressed=false;

/*
  Register object t0, buttonPlus, buttonMinus, to the touch event list.
*/
NexTouch *nex_listen_list[] =
{
  &m0,
  &m1,
  &m2,
  &m3,
  &m4,
  &m5,
  &m6,
  &m7,
  &m8,
  &m9,
  &m10,
  &m11,
  &m12,
  &m13,
  &t0,
  &t1,
  &t2,
  NULL
};
void EEPROM_writeDouble(int ee, float value)
{
    byte* p = (byte*)(void*)&value;
    for (int i = 0; i < sizeof(value); i++)
        EEPROM.write(ee++, *p++);
EEPROM.commit();
}
float EEPROM_readDouble(int ee)
{
    float value = 0.0;
    byte* p = (byte*)(void*)&value;
    for (int i = 0; i < sizeof(value); i++)
        *p++ = EEPROM.read(ee++);
    return value;
}
void unlock()
{
  /*
  digitalWrite(relayPIN,HIGH);
  delay(500);
  digitalWrite(relayPIN,LOW);
  */

   servo.write(180);
}

void lock(){
  delay(10000);
  servo.write(0);
}

void m0PushCallback(void *ptr)
{
  dbSerialPrintln("m1PushCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  //Set phone number on Screen
 ph_number+="0";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
 
}
void m1PushCallback(void *ptr)
{
 dbSerialPrintln("m1PushCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
 //Set phone number on Screen
 ph_number+="1";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);

}

void m2PushCallback(void *ptr)
{
 dbSerialPrintln("m2PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  
  //Set phone number on Screen
 ph_number+="2";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m3PushCallback(void *ptr)
{
 dbSerialPrintln("m3PushCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
//Set phone number on Screen
 ph_number+="3";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}

void m4PushCallback(void *ptr)
{
 dbSerialPrintln("m4PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  Serial.println("Button Pressed");

//Set phone number on Screen
 ph_number+="4";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m5PushCallback(void *ptr)
{
  dbSerialPrintln("m5PushCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  //Set phone number on Screen
 ph_number+="5";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m6PushCallback(void *ptr)
{
 dbSerialPrintln("m6PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  Serial.println("Button Pressed");
  //Set phone number on Screen
 ph_number+="6";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m7PushCallback(void *ptr)
{
 dbSerialPrintln("m7PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  Serial.println("Button Pressed");
  //Set phone number on Screen
 ph_number+="7";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m8PushCallback(void *ptr)
{
  dbSerialPrintln("m8PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  Serial.println("Button Pressed");
 //Set phone number on Screen
 ph_number+="8";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m9PushCallback(void *ptr)
{
  dbSerialPrintln("m6PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  Serial.println("Button Pressed");
  //Set phone number on Screen
 ph_number+="9";
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m10PushCallback(void *ptr)
{
  dbSerialPrintln("m6PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  
  keyPressed = true;
  Serial.println("BackSpace Pressed");
  //Set phone number on Screen
 ph_number=ph_number.substring(0,ph_number.length()-1);
 int len=ph_number.length()+1;
 char buf[len];
 ph_number.toCharArray(buf,len);
 t0.setText(buf);
}
void m11PushCallback(void *ptr)
{
 dbSerialPrintln("m6PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  keyPressed = true;
  Serial.println("Button Pressed");
   //Set phone number on Screen
 t0.setText("Submitted");
 unlock();
float instWeight=getWeight();
 //instWeight=120;
 cum_weight+=instWeight;
// cum_weight+=12;
 //sendData("phoneNo=" + getPhoneNo(ph_number)+"&InstaWeight="+String(instWeight)+"&CumulatWeight="+String(getCumWeight(cum_weight)));
 String ws="Weight= "+(String)instWeight;
 int len=ws.length()+1;
 char arr[len];
 ws.toCharArray(arr,len);
 t0.setText(arr);
 t0.setText("Enter Ph.No");
 Serial.println(cum_weight);
 EEPROM_writeDouble(0,cum_weight); 
 lock();
}
void m12PushCallback(void *ptr)
{
  delay(1000);
  t1.setText("1.5 Kg");
  delay(1000);
  t1.setText("1.5 Kg");
 dbSerialPrintln("m12PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  Serial.println("Button Pressed");
  Serial.println("Start Weight Process");
  instWeight=1.6;
  smoke=analogRead(MQ2_PIN);
}
void m13PushCallback(void *ptr)
{
  delay(1000);
  t2.setText("ED$ 125");
  delay(1000);
  t2.setText("ED$ 125");
  dbSerialPrintln("m13PopCallback");
  dbSerialPrint("ptr = ");
  dbSerialPrintln((uint32_t)ptr);
  Serial.println("Congratulations");
  Serial.println("Your Reward");
 // setupSIM868((String)temp,(String)hum,(String)instWeight,(String)cum_weight,(String)smoke, (String)ph_number,String(Lat),String(Long));
  ph_number="";
}
//----------------- S E T U P ----------------------------
void setup(void)
{
  EEPROM.begin(512);
  cum_weight=EEPROM_readDouble(0);
////////remove history from the EEPROM/
  EEPROM_writeDouble(0,0.000);
  pinMode(MQ2_PIN,INPUT);
  pinMode(relayPIN,OUTPUT);
  digitalWrite(relayPIN,LOW);
  nexInit(9600);      // default 115200
  m0.attachPush(m0PushCallback, &m0); 
  m1.attachPush(m1PushCallback, &m1);
  m2.attachPush(m2PushCallback, &m2);
  m3.attachPush(m3PushCallback, &m3);
  m4.attachPush(m4PushCallback, &m4);
  m5.attachPush(m5PushCallback, &m5);
  m6.attachPush(m6PushCallback, &m6);
  m7.attachPush(m7PushCallback, &m7);
  m8.attachPush(m8PushCallback, &m8);
  m9.attachPush(m9PushCallback, &m9);
  m10.attachPush(m10PushCallback, &m10);
  m11.attachPush(m11PushCallback, &m11);
  m12.attachPush(m12PushCallback, &m12);
  m13.attachPush(m13PushCallback, &m13);
  dbSerialPrintln("setup done");
  Serial.println("CUMULATIVE WEIGHT: "+(String)cum_weight);
///////////WIFI setup
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("Started");
  Serial.print("Connecting");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

servo.attach(33);
Serial.println("Ready to go");
Serial2.begin(9600,SERIAL_8N1,14,4);
//Serial2.begin(115200);

    setupLoadSensor();
    DHTsetup();
    getDHT();
    getWeight();
// void setupSIM868(String temp, String hum,String weight, String cumWeight, String Smoke, String ph_number, String Lat, String Long)
    servo.write(30);
}
//------------------- L O O P ---------------------------------------
void loop(void)
{ 
  /*
  currentMillis = millis();

   //Depois de um segundo, mostra-se o número de pulsos.
  if (currentMillis - previousMillis > intervalo) {
    previousMillis = currentMillis;
    getDHT();
    //getWeight();
  }*/
  nexLoop(nex_listen_list); 
  //getWeight();
}

