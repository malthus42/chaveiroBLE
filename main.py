import bluetooth
from machine import Pin, I2C
import sh1106
import time


led = Pin(8, Pin.OUT)
led.off()

i2c = I2C(0, scl=Pin(6), sda=Pin(5))
oled = sh1106.SH1106_I2C(128, 64, i2c)
oled.fill(0)
oled.show()
buzzer = Pin(4, Pin.OUT)  

# === Configuração BLE ===
ble = bluetooth.BLE()
ble.active(True)

NUS_UUID       = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
NUS_TX_UUID    = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")  # notify (ESP -> cliente)
NUS_RX_UUID    = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")  # write  (cliente -> ESP)

NUS_TX_FLAG = bluetooth.FLAG_NOTIFY
NUS_RX_FLAG = bluetooth.FLAG_WRITE

NUS_SERVICE = (
    NUS_UUID,
    (
        (NUS_TX_UUID, NUS_TX_FLAG),
        (NUS_RX_UUID, NUS_RX_FLAG),
    ),
)

services = (NUS_SERVICE,)
((tx_handle, rx_handle),) = ble.gatts_register_services(services)

# === Callback BLE ===
def ble_irq(event, data):
    if event == 1:  # Conectado
        print("Conectado")
    elif event == 2:  # Desconectado
        print("Desconectado")
        ble.gap_advertise(100, adv_payload)
    elif event == 3:  # Recebeu dados
        conn_handle, attr_handle = data
        if attr_handle == rx_handle:
            value = ble.gatts_read(rx_handle)
            try:
                cmd = value.decode('utf-8').strip()
                print("Recebido via BLE:", cmd)

                # Controle do LED
                if cmd.lower() == "on":
                    buzzer.value(1)
                    led.off()
                elif cmd.lower() == "off":
                    led.on()
                    buzzer.value(0)                   

                oled.fill(0)
                oled.text(cmd, 28, 22, 1)
                oled.show()

            except Exception as e:
                print("Erro lendo comando:", e)

ble.irq(ble_irq)

# === Função para gerar payload de anúncio ===
def make_adv_payload(name=None):
    payload = bytearray(b'\x02\x01\x06')
    if name:
        payload += bytearray((len(name)+1, 0x09)) + name.encode()
    return payload

DEVICE_NAME = "ESP32-NUS"
adv_payload = make_adv_payload(DEVICE_NAME)

# === Começa a anunciar ===
ble.gap_advertise(100, adv_payload)
print("Anunciando como:", DEVICE_NAME)

while True:
    time.sleep(1)