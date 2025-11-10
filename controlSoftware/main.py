from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QSlider, QLabel,
                               QCheckBox, QComboBox, QButtonGroup, QMessageBox, QRadioButton)
from PySide6.QtGui import QIcon
from ui_connect_bt import Ui_connect_bt
from ui_interface import Ui_Interface
import sys
from bleak import BleakClient, BleakScanner
import asyncio
import time
import threading

client_instance = None
connection_status = False
COMMAND_CHAR_UUID = "0000DEAD-0000-1000-8000-00805f9b34fb"
NOTIFY_CHAR_UUID  = "0000FEF4-0000-1000-8000-00805f9b34fb"




class Interface(QMainWindow, Ui_Interface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Interface Miocinética - LabMicro")
        self.setWindowIcon(QIcon("logo_lab.png"))
        self.btn_connect2.clicked.connect(self.connect_btn)
        self.btn_iniciar.clicked.connect(self.start_btn)
        self.btn_padronizado.clicked.connect(self.padronizado_btn)
        self.btn_personalizado.clicked.connect(self.personalizado_btn)

        self.radios = []

        self.group = QButtonGroup()
        self.group.setExclusive(True)  # garante que apenas um pode ser selecionado

        for i in range(1, 9):
            radio = getattr(self, f"m_{i}")  # obtém o radio da UI
            self.radios.append(radio)
            self.group.addButton(radio)  # adiciona ao grupo
            radio.toggled.connect(self.selection)  # conecta o sinal


        self.mm_control = []

        for i in range(1, 9):
            slider_amp = getattr(self, f"amplitude_{i}")
            label_amp = getattr(self, f"amp_{i}")
            slider_freq = getattr(self, f"frequencia_{i}")
            label_freq = getattr(self, f"freq_{i}")
            combo_box = getattr(self, f"comboBox_{i}")
            checkbox = getattr(self, f"checkBox_{i}")

            marcador = MMcontrol(i, slider_amp, label_amp,slider_freq,label_freq,combo_box,checkbox)
            self.mm_control.append(marcador)

    def connect_btn(self):
        global connection_status
        connection_status = False
        self.window_running = Connect()
        self.close()
        self.window_running.show()

    def selection(self):
        selecionado = None
        for i, radio in enumerate(self.radios, start=1):
            if radio.isChecked():
                selecionado = i
                # Bolinha selecionada laranja + texto branco + fonte 14pt
                radio.setStyleSheet(u"""
                            QRadioButton {
                                color: rgb(255, 255, 255);
                                font: 14pt "MS Shell Dlg 2";
                            }
                            QRadioButton::indicator {
                                width: 16px;
                                height: 16px;
                                border-radius: 8px;   /* círculo */
                                background-color: orange;
                                border: 1px solid black;
                            }
                        """)
            else:
                # Demais rádios brancos + texto branco + fonte 14pt
                radio.setStyleSheet(u"""
                            QRadioButton {
                                color: rgb(255, 255, 255);
                                font: 14pt "MS Shell Dlg 2";
                            }
                            QRadioButton::indicator {
                                width: 16px;
                                height: 16px;
                                border-radius: 8px; 
                                background-color: white;
                                border: 1px solid black;
                            }
                        """)


        if selecionado:
            self.data_radio = [1, selecionado, 0, 0, 0, 0]
           # print(f"O radio selecionado é: m_{selecionado}")
        else:
            self.data_radio = [1, 0, 0, 0, 0, 0]
           # print("Nenhum radio selecionado")

        data_str = ",".join(map(str, self.data_radio))
        data_bytes = data_str.encode('utf-8')

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(client_instance.write_gatt_char(COMMAND_CHAR_UUID, data_bytes))
           # print("Enviado:", self.data_radio)
        except Exception as e:
           # print("Erro ao enviar BLE:", e)
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERRO")
            msg.setText("FALHA NA CONEXÃO!")
            msg.setStyleSheet("""
                                                      QMessageBox {
                                                          background-color: white;
                                                          border-radius: 10px;
                                                      }
                                                      QLabel {
                                                          color: black;
                                                          background-color: transparent;  /* remove fundo azul */
                                                          font-size: 11pt;
                                                      }
                                                      QPushButton {
                                                          background-color: #f0f0f0;
                                                          color: black;
                                                          border: 1px solid #bfbfbf;
                                                          border-radius: 5px;
                                                          padding: 5px 10px;
                                                      }
                                                      QPushButton:hover {
                                                          background-color: #dcdcdc;
                                                      }
                                                  """)



    def personalizado_btn(self):
        if self.btn_iniciar.text() == "INICIAR TESTE":
            self.stackedWidget.setCurrentWidget(self.pg_personalizado)
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Warming")
            msg.setText("Encerre o teste para trocar de página")
            msg.setStyleSheet("""
                   QMessageBox {
                       background-color: white;
                       border-radius: 10px;
                   }
                   QLabel {
                       color: black;
                       background-color: transparent;  /* remove fundo azul */
                       font-size: 11pt;
                   }
                   QPushButton {
                       background-color: #f0f0f0;
                       color: black;
                       border: 1px solid #bfbfbf;
                       border-radius: 5px;
                       padding: 5px 10px;
                   }
                   QPushButton:hover {
                       background-color: #dcdcdc;
                   }
               """)

            msg.exec_()


    def padronizado_btn(self):
        if self.btn_iniciar.text() == "INICIAR TESTE":
            self.stackedWidget.setCurrentWidget(self.pg_padronizado)
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Warming")
            msg.setText("Encerre o teste para trocar de página")
            msg.setStyleSheet("""
                   QMessageBox {
                       background-color: white;
                       border-radius: 10px;
                   }
                   QLabel {
                       color: black;
                       background-color: transparent;  /* remove fundo azul */
                       font-size: 11pt;
                   }
                   QPushButton {
                       background-color: #f0f0f0;
                       color: black;
                       border: 1px solid #bfbfbf;
                       border-radius: 5px;
                       padding: 5px 10px;
                   }
                   QPushButton:hover {
                       background-color: #dcdcdc;
                   }
               """)
            msg.exec_()


    def start_btn(self):
        global client_instance, connection_status
        if not client_instance or not client_instance.is_connected:
           # print("BLE não conectado!")
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERROR")
            msg.setText("FALHA NA CONEXÃO!")
            msg.setStyleSheet("""
                                                      QMessageBox {
                                                          background-color: white;
                                                          border-radius: 10px;
                                                      }
                                                      QLabel {
                                                          color: black;
                                                          background-color: transparent;  /* remove fundo azul */
                                                          font-size: 11pt;
                                                      }
                                                      QPushButton {
                                                          background-color: #f0f0f0;
                                                          color: black;
                                                          border: 1px solid #bfbfbf;
                                                          border-radius: 5px;
                                                          padding: 5px 10px;
                                                      }
                                                      QPushButton:hover {
                                                          background-color: #dcdcdc;
                                                      }
                                                  """)
            return

        if self.btn_iniciar.text() == "INICIAR TESTE":
            self.data_start = [2, 1, self.stackedWidget.currentIndex(), 0, 0, 0]
            self.btn_iniciar.setText("PARAR TESTE")
            self.btn_iniciar.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(200, 0, 0);
                        color: white;
                        font: 75 8pt "MS Shell Dlg 2";
                    }
                    QPushButton:hover {
                        background-color: rgb(255, 80, 80);
                        color: white;
                    }
                """)
        else:
            self.data_start = [2, 0, self.stackedWidget.currentIndex(), 0, 0, 0]
            self.btn_iniciar.setText("INICIAR TESTE")
            self.btn_iniciar.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(255, 255, 255);
                        color: rgb(0, 0, 0);
                        font: 75 8pt "MS Shell Dlg 2";
                    }
                    QPushButton:hover {
                        background-color: rgb(199, 199, 199);
                        color: rgb(255, 255, 255);
                    }
                """)

        data_str = ",".join(map(str, self.data_start))
        data_bytes = data_str.encode('utf-8')

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(client_instance.write_gatt_char(COMMAND_CHAR_UUID, data_bytes))
           # print("Enviado:", data_str)
        except Exception as e:
            print("Erro ao enviar BLE:", e)



class MMcontrol:
    def __init__(self, id, amplitude_slider: QSlider, label_amp: QLabel,
                 frequencia_slider: QSlider, label_freq: QLabel,combo_box: QComboBox, check_box: QCheckBox):
        super().__init__()

        self.amplitude_slider = amplitude_slider
        self.label_amp = label_amp
        self.frequencia_slider = frequencia_slider
        self.label_freq = label_freq
        self.combo_box = combo_box
        self.check_box = check_box
        self.id = id

        # Conecta o sinal do slider
        self.amplitude_slider.valueChanged.connect(self.label_update)
        self.frequencia_slider.valueChanged.connect(self.label_update)
        self.combo_box.currentIndexChanged.connect(self.send_ble)
        self.check_box.stateChanged.connect(self.check_update)
        self.label_update()
        self.check_update()

    def label_update(self):
        self.label_amp.setText(str(self.amplitude_slider.value()))
        self.frequencia = (self.frequencia_slider.value())
        self.label_freq.setText(str(self.frequencia))
        self.send_ble()

    def check_update(self):
        self.send_ble()

        if self.check_box.isChecked():
            handle_color = "#ffaa7f"
            groove_color = "#ffdcc9"
            self.amplitude_slider.setEnabled(True)
            self.frequencia_slider.setEnabled(True)
        else:
            handle_color = "#3a75b0"
            groove_color = "#ffffff"  # barra desabilitada branca
            self.amplitude_slider.setEnabled(False)
            self.frequencia_slider.setEnabled(False)

        style = f"""
        QSlider::groove:horizontal {{
            border: 1px solid #999999;
            height: 10px;
            background: {groove_color};
            border-radius: 5px;
        }}

        QSlider::sub-page:horizontal {{
            background: {handle_color};
            border-radius: 5px;
        }}

        QSlider::handle:horizontal {{
            background-color: {handle_color};
            border: 2px solid #666666;
            width: 24px;
            height: 24px;
            margin: -7px 0;      /* centraliza verticalmente */
            border-radius: 12px; /* círculo perfeito */
        }}

        QSlider::handle:horizontal:hover {{
            border: 2px solid #ffffff;
        }}
        """

        self.amplitude_slider.setStyleSheet(style)
        self.frequencia_slider.setStyleSheet(style)

    def send_ble(self):
        if not client_instance or not client_instance.is_connected:
            print("BLE não conectado!")
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERRO")
            msg.setText("FALHA NA CONEXÃO!")
            msg.setStyleSheet("""
                                                      QMessageBox {
                                                          background-color: white;
                                                          border-radius: 10px;
                                                      }
                                                      QLabel {
                                                          color: black;
                                                          background-color: transparent;  /* remove fundo azul */
                                                          font-size: 11pt;
                                                      }
                                                      QPushButton {
                                                          background-color: #f0f0f0;
                                                          color: black;
                                                          border: 1px solid #bfbfbf;
                                                          border-radius: 5px;
                                                          padding: 5px 10px;
                                                      }
                                                      QPushButton:hover {
                                                          background-color: #dcdcdc;
                                                      }
                                                  """)
            return

        self.data = [
            0,  # Indica que estou alterando os dados por meio de um slider ou lista, não pelo botão
            int(self.check_box.isChecked()),  # 1 se marcado, 0 se não
            self.id,  # id do motor
            self.combo_box.currentIndex(),  # índice do combobox
            self.label_freq.text(),
            self.label_amp.text(),
        ]

        data_str = ",".join(map(str, self.data))
        data_bytes = data_str.encode('utf-8')

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(client_instance.write_gatt_char(COMMAND_CHAR_UUID, data_bytes))
            #print("Enviado:", data_str)
        except Exception as e:
            print("Erro ao enviar BLE:", e)





class Connect(QWidget, Ui_connect_bt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Interface Miocinética - LabMicro")
        self.setWindowIcon(QIcon("logo_lab.png"))
        self.btn_connect.clicked.connect(self.connect)
        self.id_bt.returnPressed.connect(self.connect)

        self.interface_window = None

    def connect(self):
        thread_connect_bt = threading.Thread(target=self.connect_bt_thread_wrapper)
        thread_connect_bt.start()
        start_time = time.time()
        while not connection_status and (time.time() - start_time < 18):
            time.sleep(0.1)
        if connection_status:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("CONECTADO")
            msg.setText("CONEXÃO ESTABELECIDA COM SUCESSO!")
            msg.setStyleSheet("""
                                          QMessageBox {
                                              background-color: white;
                                              border-radius: 10px;
                                          }
                                          QLabel {
                                              color: black;
                                              background-color: transparent;  /* remove fundo azul */
                                              font-size: 11pt;
                                          }
                                          QPushButton {
                                              background-color: #f0f0f0;
                                              color: black;
                                              border: 1px solid #bfbfbf;
                                              border-radius: 5px;
                                              padding: 5px 10px;
                                          }
                                          QPushButton:hover {
                                              background-color: #dcdcdc;
                                          }
                                      """)
            msg.exec_()
            self.interface_window = Interface()
            self.interface_window.stackedWidget.setCurrentIndex(0)
            self.interface_window.show()
            self.close()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("")
            msg.setText("FALHA NA CONEXÃO!")
            msg.setStyleSheet("""
                                          QMessageBox {
                                              background-color: white;
                                              border-radius: 10px;
                                          }
                                          QLabel {
                                              color: black;
                                              background-color: transparent;  /* remove fundo azul */
                                              font-size: 11pt;
                                          }
                                          QPushButton {
                                              background-color: #f0f0f0;
                                              color: black;
                                              border: 1px solid #bfbfbf;
                                              border-radius: 5px;
                                              padding: 5px 10px;
                                          }
                                          QPushButton:hover {
                                              background-color: #dcdcdc;
                                          }
                                      """)
            msg.exec_()
    def connect_bt_thread_wrapper(self):
        device_name = self.id_bt.text()
        asyncio.run(self.connect_bt_async(device_name))



    async def connect_bt_async(self, device_name):
        global client_instance, connection_status
       # print(f"Procurando {device_name}...")

        if client_instance is not None:
            try:
                await client_instance.disconnect()
                print("Cliente anterior desconectado com sucesso.")
                await asyncio.sleep(1)
            except Exception as e:
                print("Falha ao desconectar cliente anterior:", e)


        devices = await BleakScanner.discover(timeout=5)
        target = next((d for d in devices if d.name == device_name), None)


        if not target:
            #print("Dispositivo não encontrado.")
            connection_status = False
            return

        #print("Encontrado:", target.name, target.address)

        client_instance = BleakClient(target.address)
        await client_instance.connect()

        if client_instance.is_connected:
            connection_status = True
           # print("Conectado com sucesso!")
            return

        else:
            connection_status = False
            #print("Falha na conexão.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Connect()
    window.show()
    app.exec()
