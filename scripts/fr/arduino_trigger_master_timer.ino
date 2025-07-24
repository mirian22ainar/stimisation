#include <TimerOne.h>

const int triggerPin = 8;
volatile bool doit_envoyer = false;

void setup() {
  Serial.begin(115200);
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);

  // Lancement du Timer toutes les 500 ms
  Timer1.initialize(500000);  // 500 000 µs = 500 ms
  Timer1.attachInterrupt(routine_periode);
}

void loop() {
  if (doit_envoyer) {
    doit_envoyer = false;

    // 1. Envoi de la commande série
    Serial.println("SHOW");
    Serial.flush();  // assure la transmission complète avant TTL

    // 2. Envoi du trigger TTL de 1 ms
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(triggerPin, LOW);
  }
}

// Fonction appelée toutes les 500 ms par le Timer hardware
void routine_periode() {
  doit_envoyer = true;
}
