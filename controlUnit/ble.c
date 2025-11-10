#include "ble.h"

uint8_t ble_addr_type;
uint8_t receivedData[6] = {0}; 

// Função de escrita de dados no servidor ESP32 via BLE
static int device_read(uint16_t conn_handle, uint16_t attr_handle,
                       struct ble_gatt_access_ctxt *ctxt, void *arg)
{

    // Copia os dados recebidos para uma string local
    char data[64];
    memcpy(data, ctxt->om->om_data, ctxt->om->om_len);
    data[ctxt->om->om_len] = '\0';


    // Divide os valores por vírgula e converte para float
    int i = 0;
    char *token = strtok(data, ",");
    while (token != NULL && i < 6)
    {
        receivedData[i] = atoi(token);
        i++;
        token = strtok(NULL, ",");
    }

    return 0;
}

// Função de leitura de dados do servidor ESP32 via BLE
static int device_write(uint16_t con_handle, uint16_t attr_handle, struct ble_gatt_access_ctxt *ctxt, void *arg)
{
    // Envia uma string de dados de volta ao cliente
    os_mbuf_append(ctxt->om, "Data from the server", strlen("Data from the server"));
    return 0;
}

// Definição das características GATT do serviço BLE
static const struct ble_gatt_svc_def gatt_svcs[] = {
    {.type = BLE_GATT_SVC_TYPE_PRIMARY,
     .uuid = BLE_UUID16_DECLARE(0x180),                 // Define o UUID do serviço
     .characteristics = (struct ble_gatt_chr_def[]){
         {.uuid = BLE_UUID16_DECLARE(0xFEF4),           // Define o UUID para leitura
          .flags = BLE_GATT_CHR_F_READ,
          .access_cb = device_write},
         {.uuid = BLE_UUID16_DECLARE(0xDEAD),           // Define o UUID para escrita
          .flags = BLE_GATT_CHR_F_WRITE,
          .access_cb = device_read},
         {0}}},
    {0}};

// Função para lidar com eventos GAP (Generic Access Profile)
static int ble_gap_event(struct ble_gap_event *event, void *arg)
{
    switch (event->type)
    {
    case BLE_GAP_EVENT_CONNECT:
        ESP_LOGI("GAP", "BLE GAP EVENT CONNECT %s", event->connect.status == 0 ? "OK!" : "FAILED!");
        if (event->connect.status != 0)
        {
            ble_app_advertise();  // Recomeça a anunciar se a conexão falhar
        }
        break;
    case BLE_GAP_EVENT_DISCONNECT:
        ESP_LOGI("GAP", "BLE GAP EVENT DISCONNECTED");
        ble_app_advertise();
        break;
    case BLE_GAP_EVENT_ADV_COMPLETE:
        ESP_LOGI("GAP", "BLE GAP EVENT");
        ble_app_advertise();  // Recomeça a anunciar após o término de um anúncio
        break;
    default:
        break;
    }
    return 0;
}

// Função para configurar e iniciar o anúncio BLE
void ble_app_advertise(void)
{
    // Definição do nome do dispositivo GAP
    struct ble_hs_adv_fields fields;
    const char *device_name;
    memset(&fields, 0, sizeof(fields));
    device_name = ble_svc_gap_device_name();  // Obtém o nome do dispositivo BLE
    fields.name = (uint8_t *)device_name;
    fields.name_len = strlen(device_name);
    fields.name_is_complete = 1;
    ble_gap_adv_set_fields(&fields);

    // Configuração dos parâmetros de conectividade GAP
    struct ble_gap_adv_params adv_params;
    memset(&adv_params, 0, sizeof(adv_params));
    adv_params.conn_mode = BLE_GAP_CONN_MODE_UND;  // Modo de conexão (conectável ou não)
    adv_params.disc_mode = BLE_GAP_DISC_MODE_GEN;  // Modo de descoberta (descoberta geral ou limitada)
    ble_gap_adv_start(ble_addr_type, NULL, BLE_HS_FOREVER, &adv_params, ble_gap_event, NULL);
}

// Função chamada quando a aplicação BLE está sincronizada
void ble_app_on_sync(void)
{
    ble_hs_id_infer_auto(0, &ble_addr_type);  // Determina automaticamente o melhor tipo de endereço
    ble_app_advertise();  // Inicia o anúncio BLE
}

// Tarefa principal do host BLE
void host_task(void *param)
{
    nimble_port_run();  // Função que só retorna quando nimble_port_stop() é executado
}

// Função principal da aplicação
void ble_start()
{
    nvs_flash_init();                          // 1 - Inicializa o NVS flash
    esp_nimble_hci_and_controller_init();      // 2 - Inicializa o controlador ESP 
    nimble_port_init();                        // 3 - Inicializa a pilha do host
    ble_svc_gap_device_name_set("MYKI");       // 4 - Define o nome do servidor BLE
    ble_svc_gap_init();                        // 4 - Inicializa o serviço GAP
    ble_svc_gatt_init();                       // 4 - Inicializa o serviço GATT
    ble_gatts_count_cfg(gatt_svcs);            // 4 - Conta as configurações dos serviços GATT
    ble_gatts_add_svcs(gatt_svcs);             // 4 - Adiciona os serviços GATT à fila
    ble_hs_cfg.sync_cb = ble_app_on_sync;      // 5 - Define a função de sincronização da aplicação
    nimble_port_freertos_init(host_task);      // 6 - Inicia a tarefa FreeRTOS
}
