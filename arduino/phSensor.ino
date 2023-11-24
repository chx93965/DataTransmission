
#define SensorPin S0          //pH meter Analog output to Arduino Analog Input 0
#define Offset 0.00 		  //deviation compensate
#define LED 13
#define samplingInterval 20	  //ms
#define printInterval 800	  //ms
#define ArrayLenth 40 		  //number of collections
int pHArray[ArrayLenth];
int array_ind = 0;

void setup(){
	pinMode(LED, OUTPUT);  
	Serial.begin(9600);  		  //baud rate 9600 bps
	Serial.println("System ready");
}

double avergearray(int* arr, int length){
	int i;
	int max, min;
	double avg;
	long amount = 0;
	
	if(length <= 0){
		Serial.println("Invalid array length/n");
		return 0;
	}
	for(i = 0; i < length; i++){
		amount += arr[i];
	}
	avg = amount / length;
	return avg;
}

void loop(){
	static unsigned long samplingTime = millis();
	static unsigned long printTime = millis();
	static float pH, mV;
	
	if(millis() - samplingTime > samplingInterval){
		pHArray[array_ind++] = analogRead(SensorPin);
		if(array_ind == ArrayLenth) array_ind = 0;
		mV = avergearray(pHArray, ArrayLenth) * 5.0 / 1024; // convert analog to mV
		pH = 3.5 * mV + Offset; // convert mV to pH
		samplingTime = millis();
	}
	if(millis() - printTime > printInterval){
		//precision -> 2 decimal places
		Serial.print("\nmV: ");
		Serial.print(mV, 2);
		Serial.print("; pH: ");
		Serial.print(pH, 2);
		//toggle LED
		digitalWrite(LED, digitalRead(LED) ^ 1);
		printTime = millis();
	}
}



