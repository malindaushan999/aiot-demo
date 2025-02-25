#include <SoftwareSerial.h>
#include <TinyGPS++.h>

// Define RX and TX pins for SoftwareSerial
#define RXPin 4
#define TXPin 3
#define GPSBaud 9600

// Create SoftwareSerial and TinyGPS++ instances
SoftwareSerial gpsSerial(RXPin, TXPin);
TinyGPSPlus gps;

void setup() {
    Serial.begin(115200);  // Start serial for debugging
    gpsSerial.begin(GPSBaud);  // Start GPS module serial

    Serial.println("Connecting to NEO-6M GPS...");
}

void loop() {
    while (gpsSerial.available()) {  // Check for GPS data
        gps.encode(gpsSerial.read());  // Parse incoming data
    }

    if (gps.location.isUpdated()) {  // If new data is available
        Serial.print("Latitude: ");
        Serial.print(gps.location.lat(), 6);  // Print latitude
        Serial.print(" | Longitude: ");
        Serial.println(gps.location.lng(), 6);  // Print longitude
    }

    if (gps.date.isValid()) {
        Serial.print("Date: ");
        Serial.print(gps.date.day());
        Serial.print("/");
        Serial.print(gps.date.month());
        Serial.print("/");
        Serial.println(gps.date.year());
    }

    if (gps.time.isValid()) {
        Serial.print("Time: ");
        Serial.print(gps.time.hour());
        Serial.print(":");
        Serial.print(gps.time.minute());
        Serial.print(":");
        Serial.println(gps.time.second());
    }

    Serial.println("-------------------------");
    delay(2000);  // Wait before next read
}
