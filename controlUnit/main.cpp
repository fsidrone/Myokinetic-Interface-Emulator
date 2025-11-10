#include <vector>
#include <iostream>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "driver/ledc.h"

#include "ble.h"
#include "motor.h"

#define MOTOR_1_PIN 32
#define MOTOR_2_PIN 33  
#define MOTOR_3_PIN 25
#define MOTOR_4_PIN 26
#define MOTOR_5_PIN 27
#define MOTOR_6_PIN 14
#define MOTOR_7_PIN 12
#define MOTOR_8_PIN 13

#define TRIGGER_PIN GPIO_NUM_4

SemaphoreHandle_t motoresMutex;

uint8_t control, page, id, frequency, amplitude, waveform, movimentType, start, active;
std::vector<Motor> motores;
std::vector<float> stop(8, 0.0f);


struct MotorTaskParam {
    uint8_t id_motor;
    uint8_t pin;
};



void parseReceivedData() {
    control = receivedData[0];
    if (control == 2) 
    {
        start = receivedData[1];
        page = receivedData[2];
    } 
    else if (control == 1) 
    {
        movimentType = receivedData[1];
    }
    else if (control == 0) 
    {
        active = receivedData[1];
        id = receivedData[2];
        waveform = receivedData[3];
        frequency = receivedData[4];
        amplitude = receivedData[5];
    }
}

ledc_channel_t getChannelFromId(int id_motor) {
    switch(id_motor) {
        case 1: return LEDC_CHANNEL_0;
        case 2: return LEDC_CHANNEL_1;
        case 3: return LEDC_CHANNEL_2;
        case 4: return LEDC_CHANNEL_3;
        case 5: return LEDC_CHANNEL_4;
        case 6: return LEDC_CHANNEL_5;
        case 7: return LEDC_CHANNEL_6;
        case 8: return LEDC_CHANNEL_7;
        default: return LEDC_CHANNEL_0; // retorna canal 0 se ID inválido
    }
}

void motor_control_task(void* param)
{
    uint64_t last_sample = esp_timer_get_time() / 1000;
    uint8_t counter = 0;
    bool trigger_control = true;

    while(true){
        
        uint64_t now = esp_timer_get_time() / 1000;
        if (now - last_sample >= SAMPLE_TIME_MS) {
            last_sample = now;
            

            for(uint8_t i = 0; i < motores.size(); i++) {

                float position = motores[i].getPosition();
                if(i==0 && start == 0 && position == 0.0f ){
                    counter = 0;
                }
                
                if(start == 1 || position != 0.0f) {
                    if(trigger_control){
                        counter++;
                        gpio_set_level(TRIGGER_PIN, 0);
                        trigger_control = false;
                        printf("Counter: %d\n", counter);
                    }

                    //trigger
                    if (page == 0) {
                        motores[i].freeMovement();
                    } else if (page == 1) {
                        vTaskDelay(pdMS_TO_TICKS(5));
                        if (movimentType == 1) {
                            motores[i].handOpening();
                            printf("Tamanho dos motores %d\n", motores.size());
                        } else if (movimentType == 2) {
                            motores[i].handClosing();
                        } else if (movimentType == 3) {
                            //Adicionar algum movimento padronizado

                        } else if (movimentType == 4) {
                            //Adicionar algum movimento padronizado
                        }
                    }
                }
                
            }
            trigger_control = true;
            gpio_set_level(TRIGGER_PIN, 1);
            
        }
        vTaskDelay(pdMS_TO_TICKS(10));
    }
}

void motor_params_task(void* param)
{
    MotorTaskParam* p = (MotorTaskParam*)param;
    uint8_t id_motor = p->id_motor;
    uint8_t pin = p->pin;
    ledc_channel_t channel = getChannelFromId(id_motor);

    xSemaphoreTake(motoresMutex, portMAX_DELAY);
    motores.emplace_back(pin, channel, id_motor);
    motores[id_motor - 1].pwmConfig();
    xSemaphoreGive(motoresMutex);
    
    

    while(true) {
        parseReceivedData();
        vTaskDelay(pdMS_TO_TICKS(10));

        if(id == id_motor) {
                    motores[id_motor - 1].setAmplitude((amplitude));
                    motores[id_motor - 1].setFrequency(frequency);
                    motores[id_motor - 1].setWaveform(waveform);
                    motores[id_motor - 1].setCheckbox(active);
        }


            //  printf("Received: ");
        //  for (int i = 0; i < 6; i++) {
        //      printf("%d ", receivedData[i]);
        //  }
        //  printf("\n");
     }
       
    
}

extern "C" void app_main(void)
{
    gpio_pad_select_gpio(TRIGGER_PIN);
    gpio_set_direction(TRIGGER_PIN, GPIO_MODE_OUTPUT);

    

    motoresMutex = xSemaphoreCreateMutex();
    static MotorTaskParam motor1Param = {1, MOTOR_1_PIN};
    xTaskCreate(motor_params_task, "motor1_task", 2048, &motor1Param, 5, NULL);
    esp_rom_delay_us(200000);

    static MotorTaskParam motor2Param = {2, MOTOR_2_PIN};
    xTaskCreate(motor_params_task, "motor2_task", 2048, &motor2Param, 5, NULL);
    esp_rom_delay_us(200000);


    static MotorTaskParam motor3Param = {3, MOTOR_3_PIN};
    xTaskCreate(motor_params_task, "motor3_task", 2048, &motor3Param, 5, NULL);
    esp_rom_delay_us(200000);


    static MotorTaskParam motor4Param = {4, MOTOR_4_PIN};
    xTaskCreate(motor_params_task, "motor4_task", 2048, &motor4Param, 5, NULL);
    esp_rom_delay_us(100000);


    static MotorTaskParam motor5Param = {5, MOTOR_5_PIN};
    xTaskCreate(motor_params_task, "motor5_task", 2048, &motor5Param, 5, NULL);
    esp_rom_delay_us(100000);


    static MotorTaskParam motor6Param = {6, MOTOR_6_PIN};
    xTaskCreate(motor_params_task, "motor6_task", 2048, &motor6Param, 5, NULL);
    esp_rom_delay_us(200000);


    static MotorTaskParam motor7Param = {7, MOTOR_7_PIN};
    xTaskCreate(motor_params_task, "motor7_task", 2048, &motor7Param, 5, NULL);
    esp_rom_delay_us(200000);


    static MotorTaskParam motor8Param = {8, MOTOR_8_PIN};
    xTaskCreate(motor_params_task, "motor8_task", 2048, &motor8Param, 5, NULL);
    esp_rom_delay_us(200000);

    ble_start();

    xTaskCreate(motor_control_task, "moviment_task", 2048, NULL, 5, NULL);


    
}

