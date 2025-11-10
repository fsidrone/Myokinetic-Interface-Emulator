#ifndef BLE_H
#define BLE_H

#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "esp_event.h"
#include "nvs_flash.h"
#include "esp_log.h"
#include "esp_nimble_hci.h"
#include "nimble/nimble_port.h"
#include "nimble/nimble_port_freertos.h"
#include "host/ble_hs.h"
#include "services/gap/ble_svc_gap.h"
#include "services/gatt/ble_svc_gatt.h"
#include "sdkconfig.h"

#ifdef __cplusplus
extern "C" {
#endif

extern uint8_t receivedData[6];

void ble_app_advertise(void);

// Função chamada quando a aplicação BLE está sincronizada
void ble_app_on_sync(void);

// Tarefa principal do host BLE
void host_task(void *param);

// Função principal da aplicação
void ble_start();

#ifdef __cplusplus
}
#endif


#endif





