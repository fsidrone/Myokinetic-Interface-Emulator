#ifndef MOTOR_H
#define MOTOR_H

#include <cstdint>
#include <iostream>
#include <cmath>
#include <algorithm>
#include "esp_timer.h"
#include "driver/ledc.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_task_wdt.h"


#define RAIO 10 // Raio da polia em mm
#define SAMPLE_TIME_MS 50 // Tempo de amostragem em ms
#define SAMPLE_TIME_S 0.05 // Tempo de amostragem em ms


class Motor {
private:
    uint8_t pin;
    ledc_channel_t channel;
    uint8_t id;
    uint8_t amplitude;
    uint8_t frequency;
    uint8_t waveform;
    uint8_t checkbox;
    uint8_t movimentType;
    int8_t direction;
    float position;
    float sine_position;

  

    uint8_t converteDistAngulo(float distance);

public:
    // Construtor
    Motor(uint8_t pin, ledc_channel_t channel, uint8_t id,  uint8_t amplitude=0, uint8_t frequency=0, uint8_t waveform=0, uint8_t checkbox=0, 
        uint8_t movimentType=0, int8_t direction = 1, float position=0.0f, float sine_position=0.0f);

    // Setters
    void setAmplitude(uint8_t amplitude);
    void setFrequency(uint8_t frequency);
    void setWaveform(uint8_t waveform);
    void setCheckbox(uint8_t checkbox);
    void setMovimentType(uint8_t movimentType);
    void setDirection(int8_t direction);
    void pwmConfig();

    // Getters
    uint8_t getAmplitude() const;
    uint8_t getFrequency() const;
    uint8_t getWaveform() const;
    uint8_t getCheckbox() const;
    uint8_t getMovimentType() const;
    float getPosition();


    // Movimentos
    void freeMovement();
    void sineMovement();
    void rampMovement();
    void handOpening();
    void handClosing();
};

#endif
