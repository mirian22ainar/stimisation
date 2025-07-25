#include <TimerOne.h>

const int triggerPin = 8;
volatile bool should_send = false;

void setup() {
  Serial.begin(115200);
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);

  // Start the hardware timer to trigger every 500 ms
  Timer1.initialize(500000);  // 500,000 µs = 500 ms
  Timer1.attachInterrupt(periodic_routine);
}

void loop() {
  if (should_send) {
    should_send = false;

    // 1. Send the serial command
    Serial.println("SHOW");
    Serial.flush();  // ensure the message is fully sent before the TTL trigger

    // 2. Send a TTL pulse of 1 ms
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(triggerPin, LOW);
  }
}

// This function is called every 500 ms by the hardware timer
void periodic_routine() {
  should_send = true;
}
