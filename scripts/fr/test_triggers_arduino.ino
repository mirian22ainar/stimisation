// Utilise la librairie TimerOne : https://www.pjrc.com/teensy/td_libs_TimerOne.html
#include <TimerOne.h>

const int triggerPin = 8;       // Sortie TTL sur la pin 8
const unsigned long period_us = 250000;   // Période = 10 ms (10 000 µs)
const unsigned long pulse_width_us = 1000; // Largeur du pulse = 1 ms

void setup() {
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);

  Timer1.initialize(period_us);         // Timer déclenché toutes les 10 ms
  Timer1.attachInterrupt(trigger);      // Fonction appelée à chaque tick
}

void loop() {
  // Le timer fait tout, rien à faire ici
}

void trigger() {
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(pulse_width_us);    // Pulse de 1 ms
  digitalWrite(triggerPin, LOW);
}
