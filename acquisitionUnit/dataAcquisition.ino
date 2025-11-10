#include <SPI.h>

const int csPins[] = {33, 25, 26, 27, 2, 15, 13, 4, 16, 17, 21, 5}; 
const int numSensors = sizeof(csPins) / sizeof(csPins[0]); 

#define SCLK 18
#define SDI_SDO 19
#define BOTAO_PIN 34
#define OFF 12

#define WHO_AM_I  0x8F
#define CTRL_REG1 0x20
#define CTRL_REG2 0x21
#define CTRL_REG3 0x22 
#define CTRL_REG4 0x23
#define CTRL_REG5 0x24
#define OUT_X_L   0xE8 
#define OUT_X_H   0x29
#define OUT_Y_L   0x2A
#define OUT_Y_H   0x2B
#define OUT_Z_L   0x2C
#define OUT_Z_H   0x2D
#define READ_dummy 0X00

uint8_t sendData[2];
uint8_t dummy[2];
uint8_t readData[7];
const long interval = 50; 
const int dados_CS = 22; 
int count = 0;

int16_t offsetsX[numSensors] = {0};
int16_t offsetsY[numSensors] = {0};
int16_t offsetsZ[numSensors] = {0};

SPIClass LIS3MDL1(HSPI);
SPISettings settings(1000000, MSBFIRST, SPI_MODE0);

// variável para sinalizar interrupção
volatile bool startRead = false;

// debounce simples
volatile unsigned long lastInterrupt = 0;
const unsigned long debounceTime = 40;

void IRAM_ATTR buttonISR() {
    startRead = true;
}

void setup() {
  Serial.begin(115200);  
  digitalWrite(OFF, HIGH);
  pinMode(BOTAO_PIN, INPUT_PULLUP);
  pinMode(dados_CS, OUTPUT);
  digitalWrite(dados_CS, HIGH); 
  
  for (int i = 0; i < numSensors; i++) {
    pinMode(csPins[i], OUTPUT);
    digitalWrite(csPins[i], HIGH);
  }

  pinMode(SCLK, OUTPUT);
  pinMode(SDI_SDO, INPUT); 

  LIS3MDL1.begin(SCLK, SDI_SDO, SDI_SDO); 

  sendData[0] = CTRL_REG3; sendData[1] = 0b00000100;
  for (int i = 0; i < numSensors; i++) send_command(csPins[i], sendData, dummy);

  sendData[0] = CTRL_REG2; sendData[1] = 0b01100000;
  for (int i = 0; i < numSensors; i++) send_command(csPins[i], sendData, dummy);

  sendData[0] = CTRL_REG5; sendData[1] = 0b01000000;
  for (int i = 0; i < numSensors; i++) send_command(csPins[i], sendData, dummy);

  sendData[0] = WHO_AM_I; sendData[1] = READ_dummy;
  for (int i = 0; i < numSensors; i++) {
    send_command(csPins[i], sendData, dummy);
    Serial.print("GPIO: "); Serial.print(csPins[i]);
    Serial.print(" WHO_AM_I: "); Serial.println(dummy[1]);
  }

  calibrateSensors();

  // Configura interrupção no botão
  attachInterrupt(digitalPinToInterrupt(BOTAO_PIN), buttonISR, FALLING);
}

void loop() {
  if (startRead) {
    startRead = false;  // reseta flag
    count++;
    unsigned long previousMillis = millis();  

    uint8_t buffer[72]; 
    int idx = 0;

    for (int i = 0; i < numSensors; i++) {
      sendData[0] = OUT_X_L;
      sendData[1] = READ_dummy;
      read_data(csPins[i], sendData, readData);

      int16_t rawX = (int16_t)(readData[2] << 8 | readData[1]) - offsetsX[i];
      int16_t rawY = (int16_t)(readData[4] << 8 | readData[3]) - offsetsY[i];
      int16_t rawZ = (int16_t)(readData[6] << 8 | readData[5]) - offsetsZ[i];


      buffer[idx++] = (rawX >> 8) & 0xFF;
      buffer[idx++] = rawX & 0xFF;
      
      buffer[idx++] = (rawY >> 8) & 0xFF;
      buffer[idx++] = rawY & 0xFF;

      buffer[idx++] = (rawZ >> 8) & 0xFF;
      buffer[idx++] = rawZ & 0xFF;
    }

    LIS3MDL1.beginTransaction(settings);
    digitalWrite(dados_CS, LOW);           
    LIS3MDL1.transfer(buffer, 72);         
    digitalWrite(dados_CS, HIGH);          
    LIS3MDL1.endTransaction();

  
  }
}

void calibrateSensors() {
  for (int i = 0; i < numSensors; i++) {
    sendData[0] = OUT_X_L;
    sendData[1] = READ_dummy;
    read_data(csPins[i], sendData, readData);

    offsetsX[i] = (int16_t)(readData[2] << 8) | readData[1];
    offsetsY[i] = (int16_t)(readData[4] << 8) | readData[3];
    offsetsZ[i] = (int16_t)(readData[6] << 8) | readData[5];

    Serial.print("Calibração Sensor ");
    Serial.print(i + 1);
    Serial.print(": X="); 
    Serial.print(offsetsX[i]);
    Serial.print(" Y="); 
    Serial.print(offsetsY[i]);
    Serial.print(" Z="); 
    Serial.println(offsetsZ[i]);
  }
}

void send_command(int Chip_select, uint8_t data_sent[2], uint8_t data_back[2]) {
  LIS3MDL1.beginTransaction(settings);
  digitalWrite(Chip_select, LOW);
  LIS3MDL1.transferBytes(data_sent, data_back, 2);
  digitalWrite(Chip_select, HIGH);
  LIS3MDL1.endTransaction();
}

void read_data(int Chip_select, uint8_t data_sent[2], uint8_t data_back[7]) {
  LIS3MDL1.beginTransaction(settings);
  digitalWrite(Chip_select, LOW);
  LIS3MDL1.transferBytes(data_sent, data_back, 7);
  digitalWrite(Chip_select, HIGH);
  LIS3MDL1.endTransaction();
}
