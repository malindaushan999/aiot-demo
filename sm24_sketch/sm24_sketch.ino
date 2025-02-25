const int geophonePin = A0; // Analog pin connected to the geophone

void setup() {
    Serial.begin(115200); // Start serial communication at 115200 baud
}

void loop() {
    int sensorValue = analogRead(geophonePin); // Read the analog value from the geophone
    Serial.println(sensorValue); // Print the value to Serial Plotter
    delay(10); // Small delay to stabilize readings
}

