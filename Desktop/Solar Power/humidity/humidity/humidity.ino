#include "DHT.h"
#define DHTPIN 2 // Тот самый номер пина, о котором упоминалось выше
DHT dht(DHTPIN, DHT11);
;
void setup() {
  Serial.begin(9600);
  dht.begin();
}
void loop() {
  delay(2000); // 2 секунды задержки
  float h = dht.readHumidity(); //Измеряем влажность
  float t = dht.readTemperature(); //Измеряем температуру
  if (isnan(h) || isnan(t)) {  // Проверка. Если не удается считать показания, выводится «Ошибка считывания», и программа завершает работу
    Serial.println("Ошибка считывания");
    return;
  }
  //Serial.print("Влажность: ");
  Serial.print(h);
  Serial.print("\t");
  Serial.print(t);
  Serial.print("\n");
  //Serial.print("Температура: ");
  //Serial.print(t);
  //Serial.println(" *C "); //Вывод показателей на экран
}
