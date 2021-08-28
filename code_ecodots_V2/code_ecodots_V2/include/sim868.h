#include<Arduino.h>
    #define PIN_TX                  27
    #define PIN_RX                  26
    #define UART_BAUD               115200
    #define PWR_PIN                 4
    #define LED_PIN                 12
    #define POWER_PIN               25
    #define IND_PIN                 36

 
#define SIM800L_RX     27
#define SIM800L_TX     26
#define SIM800L_PWRKEY 4
#define SIM800L_RST    5
#define SIM800L_POWER  23



String apn = "APN";                    //APN
String apn_u = "";                     //APN-Username
String apn_p = "";                     //APN-Password
String url = "https://myiotevent.azure-devices.net/devices/esp8266/messages/events?api-version=2020-03-13";  //URL of Server

void gsm_config_gprs();
void gsm_http_post( String postdata);


void gsm_send_serial(String command) {
  Serial.println("Send ->: " + command);
  Serial1.println(command);
  long wtimer = millis();
  while (wtimer + 3000 > millis()) {
    while (Serial1.available()) {
      Serial.write(Serial1.read());
    }
  }
  Serial.println();
}
void setupSIM868(String temp, String hum,String weight, String cum_weight, String Smoke, String ph_number, String Lat, String Long)
{

      // Onboard LED light, it can be used freely
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    // POWER_PIN : This pin controls the power supply of the Modem
    pinMode(POWER_PIN, OUTPUT);
    digitalWrite(POWER_PIN, HIGH);

    // PWR_PIN ： This Pin is the PWR-KEY of the Modem
    // The time of active low level impulse of PWRKEY pin to power on module , type 500 ms
    pinMode(PWR_PIN, OUTPUT);
    digitalWrite(PWR_PIN, HIGH);
    delay(500);
    digitalWrite(PWR_PIN, LOW);
    // delay(500);
  pinMode(SIM800L_POWER, OUTPUT);
  digitalWrite(SIM800L_POWER, HIGH);

  Serial.begin(115200);
  Serial.println("ESP32+SIM800L AT CMD Test");
  Serial1.begin(115200, SERIAL_8N1, SIM800L_TX, SIM800L_RX);
   delay(10000);
  while (Serial1.available()) {
    Serial.write(Serial1.read());
  }
  delay(2000);
  gsm_config_gprs();
 
    gsm_http_post("{ \"DeviceId\":\"esp8266\",\"Temperature\":"+temp+  ","+"\"Humidity\":"+hum+ ","+"\"Latitude\":"+"33.981792"+","+"\"Longitude\":"+"73.777557"+","+"\"Methane\":"+(String)random(100,500)+ ","+"\"Smoke\":"+Smoke+","+"\"CO2\":"+(String)random(20,50)+","+"\"PhoneNumber\":"+ph_number+","+"\"Weight\":"+weight+","+ "\"CumulativeWeight\":"+cum_weight+        "}\r\n");

    //gsm_http_post("{ \"DeviceId\":\"esp8266\",\"Temperature\":150.00,\"Humidity\":110.00}\r\n");
}


void ATloop() {

if (Serial1.available()) {
      Serial.write(Serial1.read());
    }

    if (Serial.available()) {
      Serial1.write(Serial.read());
    }
}

void gsm_http_post( String postdata) {
  Serial.println(" --- Start GPRS & HTTP --- ");
  gsm_send_serial("AT+SAPBR=1,1");
  gsm_send_serial("AT+SAPBR=2,1");
  gsm_send_serial("AT+HTTPINIT");
    gsm_send_serial("AT+HTTPSSL=1");
  gsm_send_serial("AT+HTTPPARA=CID,1");
  gsm_send_serial("AT+HTTPPARA=URL," + url);
  gsm_send_serial("AT+HTTPPARA=\"USERDATA\",\"Authorization:SharedAccessSignature sr=myiotevent.azure-devices.net%2Fdevices%2Fesp8266&sig=2OZdLSLMeRgJkHb1rR9XAVh9VLV21TNewaWm8LHvxAE%3D&se=1623334110\"");

  gsm_send_serial("AT+HTTPPARA=\"CONTENT\",\"application/json\"");

gsm_send_serial("AT+HTTPDATA=700,5000");
  delay(500);
  gsm_send_serial(postdata);

  delay(10000);

  gsm_send_serial("AT+HTTPACTION=1");

delay(7000);


boolean status=false;
while (status==false)
{String buf;
    if(Serial1.available())
    {
buf=Serial1.readString();
Serial.println(buf);
if (buf.indexOf("HTTPACTION")>-1)
{
   status=true;

}

delay(20);
    }
}

  gsm_send_serial("AT+HTTPREAD");
  gsm_send_serial("AT+HTTPTERM");
  gsm_send_serial("AT+SAPBR=0,1");

}

void gsm_config_gprs() {
  Serial.println(" --- CONFIG GPRS --- ");
  gsm_send_serial("AT+SAPBR=3,1,Contype,GPRS");
  gsm_send_serial("AT+SAPBR=3,1,APN," + apn);
  if (apn_u != "") {
    gsm_send_serial("AT+SAPBR=3,1,USER," + apn_u);
  }
  if (apn_p != "") {
    gsm_send_serial("AT+SAPBR=3,1,PWD," + apn_p);
  }
}
