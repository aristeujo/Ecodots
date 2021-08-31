#include "HX711.h"
// HX711 circuit wiring
#define DOUT 22
#define CLK 23


HX711 scale;

float calibration_factor = -6258;//54540; 
void setupLoadSensor(){
scale.begin(DOUT, CLK);
scale.set_scale();
scale.tare(); //Reset the scale to 0
long zero_factor = scale.read_average(); //Get a baseline reading
Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
Serial.println(zero_factor);

}

float getWeight() {
scale.set_scale(calibration_factor); //Adjust to this calibration factor
Serial.print("Reading: ");
float weight=scale.get_units(20)*0.453592;
if (weight < 0.0){
  weight = 0.0;
}
Serial.print(weight);
Serial.print(" kg"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
Serial.print(" calibration_factor: ");
Serial.print(calibration_factor);
Serial.println();

return weight;
}
