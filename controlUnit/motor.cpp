#include "Motor.h"

// Construtor
Motor::Motor(uint8_t pin, ledc_channel_t channel, uint8_t id, uint8_t amplitude, uint8_t frequency, uint8_t waveform, uint8_t checkbox, 
    uint8_t movimentType, int8_t direction, float position, float sine_position)
    : pin(pin), channel(channel), id(id), amplitude(amplitude), frequency(frequency), waveform(waveform), 
    checkbox(checkbox), movimentType(movimentType), direction(direction), position(position), sine_position(sine_position) {}

void Motor::setAmplitude(uint8_t amplitude) { this->amplitude = amplitude; }
void Motor::setFrequency(uint8_t frequency) { this->frequency = frequency; }
void Motor::setWaveform(uint8_t waveform) { this->waveform = waveform; }
void Motor::setCheckbox(uint8_t checkbox) { this->checkbox = checkbox; }
void Motor::setMovimentType(uint8_t movimentType) { this->movimentType = movimentType; }
void Motor::setDirection(int8_t direction) { this->direction = direction; }

// Getters
uint8_t Motor::getAmplitude() const { return amplitude; }
uint8_t Motor::getFrequency() const { return frequency; }
uint8_t Motor::getWaveform() const { return waveform; }
uint8_t Motor::getCheckbox() const { return checkbox; }
uint8_t Motor::getMovimentType() const { return movimentType; }
float Motor::getPosition() { return position; }



//pwm 
void Motor::pwmConfig() {

    ledc_timer_config_t timer_config = {
        .speed_mode       = LEDC_LOW_SPEED_MODE,
        .duty_resolution  = LEDC_TIMER_12_BIT,
        .timer_num        = LEDC_TIMER_0,
        .freq_hz          = 50,
        .clk_cfg          = LEDC_AUTO_CLK
    };
    ledc_timer_config(&timer_config);

    ledc_channel_config_t channel_config = {
        .gpio_num       = pin,
        .speed_mode     = LEDC_LOW_SPEED_MODE,
        .channel        = channel,
        .timer_sel      = LEDC_TIMER_0,     
        .duty           = 0,
        .hpoint         = 0
    };
    ledc_channel_config(&channel_config);

    printf("Motor PWM config -> GPIO %d | Channel %d", pin, channel );
}

// Movimentos
void Motor::sineMovement() {
    std::cout << "Sine movement: amplitude=" << (int)amplitude << ", frequency=" << (int)frequency << std::endl;
    const float min_us = 400.0f;
    const float max_us = 2600.0f;
    const float period_us = 20000.0f; // 50 Hz servo          
    float T = 1 / (float)frequency;               // período do sinal
    if(frequency == 0){
        T = 1 / 0.5;
    }
    
    if (T <= 0.0f) {
        std::cout << "Error: invalid period (frequency too low or zero)\n";
        return;
    }

    // calcula posição seguindo função cosseno
    float phase = fmod(sine_position, 2*T);       
    if (phase < T) {
        position = (amplitude / 2.0f) * (1 - cos(M_PI * phase / T));
    } else {
        float t_back = phase - T;
        position = (amplitude / 2.0f) * (1 - cos(M_PI * t_back / T));
        position = amplitude - position; // inverte para voltar
    }

    // converte posição para ângulo
    int angulo = converteDistAngulo(position);
    float pulse_us = min_us + (angulo / 180.0f) * (max_us - min_us);
    if(id > 4){
        pulse_us = max_us - (angulo / 180.0f) * (max_us - min_us);
    } 
    
    uint32_t duty = (pulse_us / period_us) * 4095.0f;

    ledc_set_duty(LEDC_LOW_SPEED_MODE, channel, duty);
    ledc_update_duty(LEDC_LOW_SPEED_MODE, channel);
    printf("Phase: %.3f, Position: %.3f mm, Angle: %d\n", phase, position, angulo);


    sine_position += SAMPLE_TIME_S; // incrementa tempo
    if(sine_position > 2*T) {
        sine_position= 0.0; 
    }
}


void Motor::rampMovement() {
    std::cout << "Ramp movement: amplitude=" << (int)amplitude
              << " mm, frequency=" << (int)frequency << " Hz\n";

    const float min_distance = 0.0f;
    const float min_us = 400.0f;
    const float max_us = 2600.0f;
    const float period_us = 20000.0f; // 50 Hz

    float incremento = amplitude * SAMPLE_TIME_S * (frequency); 

    printf("Incremento: %.2f mm\n", incremento);

    position += incremento * direction;

    
    if (position >= amplitude) {
        position = amplitude;
        direction = direction * (-1);
    } else if (position <= min_distance) {
        position = min_distance;
        direction = direction * (-1);
    }
  

    int angulo = converteDistAngulo(position);

    float pulse_us = min_us + (angulo / 180.0f) * (max_us - min_us);

    if(id > 4){
        pulse_us = max_us - (angulo / 180.0f) * (max_us - min_us);
    } 
    

    uint32_t duty = (pulse_us / period_us) * 4095.0f;

    ledc_set_duty(LEDC_LOW_SPEED_MODE, channel, duty);
    ledc_update_duty(LEDC_LOW_SPEED_MODE, channel);
}


void Motor::freeMovement() {
    if(checkbox == 1) {
        if(waveform == 0) {
            rampMovement();
        } else if(waveform == 1) {
            sineMovement();
        } else {
            std::cout << "No valid waveform selected." << std::endl;
        }
    }
    //std::cout << "Free movement." << std::endl;
}

void Motor::handOpening() {
    std::cout << "Hand opening movement." << std::endl;
    frequency = 0;
    amplitude = 10;
    if(position < amplitude) {
        sineMovement();
    }
}

void Motor::handClosing() {
    std::cout << "Hand closing movement." << std::endl;
    frequency = 0;
    amplitude = 10;
    if(position > 0.0f) {
        sineMovement();
    }
}



uint8_t Motor::converteDistAngulo(float distance) {
    float angulo = (distance * 180.0f) / (M_PI * RAIO);
    int anguloInt = static_cast<int>(std::round(angulo));
    if (anguloInt < 0) anguloInt = 0;
    else if (anguloInt > 180) anguloInt = 180;
    return anguloInt;
}