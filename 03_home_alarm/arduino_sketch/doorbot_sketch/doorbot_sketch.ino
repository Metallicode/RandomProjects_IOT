int DOOR_STATE = 0;
int counter = 0;

void setup() { 
  pinMode(10, OUTPUT);
  pinMode(8, INPUT);
  Serial.begin(9600);
}

void loop() {
  counter = counter+1;
  DOOR_STATE = digitalRead(8);  
  if(DOOR_STATE==LOW){ 
    digitalWrite(10, HIGH);
    Serial.println("DOOR OPEN"); 
    }
  delay(5);
  if (counter%200==0){
	counter = 0; 
    digitalWrite(10, LOW);
    delay(100); 
  }
}
