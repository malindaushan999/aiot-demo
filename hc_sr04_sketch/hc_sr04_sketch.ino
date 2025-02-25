const int trigPin = 9;  // Trigger pin of HC-SR04
const int echoPin = 10; // Echo pin of HC-SR04

void setup() {
    Serial.begin(9600); // Start the serial communication
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    long duration;
    float distance;
    
    // Send a 10-microsecond pulse to trigger pin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // Read the echo pin, and calculate distance
    duration = pulseIn(echoPin, HIGH);
    distance = duration * 0.034 / 2; // Convert to cm
    
    // Print distance to Serial Plotter
    Serial.println(distance);
    
    delay(100); // Delay to avoid excessive readings
}