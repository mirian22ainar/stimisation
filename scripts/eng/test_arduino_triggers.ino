// Uses the TimerOne library: https://www.pjrc.com/teensy/td_libs_TimerOne.html
#include <TimerOne.h>

const int triggerPin = 8;               // TTL output on pin 8
const unsigned long period_us = 250000; // Period = 250 ms (250,000 µs)
const unsigned long pulse_width_us = 1000; // Pulse width = 1 ms

void setup() {
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);

  Timer1.initialize(period_us);    // Trigger timer every 250 ms
  Timer1.attachInterrupt(trigger); // Function called on each tick
}

void loop() {
  // Nothing to do here — the timer handles everything
}

void trigger() {
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(pulse_width_us); // 1 ms TTL pulse
  digitalWrite(triggerPin, LOW);
}
