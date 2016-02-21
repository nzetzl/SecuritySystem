void setup()
{
  pinMode(7, OUTPUT); // blue LED 
  pinMode(6, OUTPUT); // red LED
  pinMode(5, OUTPUT); // green LED
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(5, LOW); //green on
  digitalWrite(7, HIGH); //blue off
  digitalWrite(6, HIGH); // red off
  noTone(3);
  
  if (digitalRead(4) == LOW)
  {
    digitalWrite(6, LOW);  // red on
    digitalWrite(5, HIGH); //green off
    tone(3,355);
    delay(5000);
  }
}
