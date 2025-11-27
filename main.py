import bluetooth
from machine import Pin, idle, freq
import time

freq(80_000_000)

led = Pin(8, Pin.OUT)
led.on()

buzzer = Pin(2, Pin.OUT, value=0)  
big_led = Pin(3, Pin.OUT, value=1)  

ble = bluetooth.BLE()
ble.active(True)

NUS_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
NUS_TX_UUID = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")  
NUS_RX_UUID = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")  

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

def muda_estagio_led():
    big_led.value(0)
    time.sleep(0.05)
    big_led.value(1)
    
def ble_irq(event, data):
    if event == 1:  
        print("Conectado")
    elif event == 2:  
        print("Desconectado")
        ble.gap_advertise(2_000_000, adv_payload)
    elif event == 3:  
        conn_handle, attr_handle = data
        if attr_handle == rx_handle:
            value = ble.gatts_read(rx_handle)
            try:
                cmd = value.decode('utf-8').strip()
                print("Recebido via BLE:", cmd)
                
                if cmd == "1":
                    buzzer.value(1)
                    for _ in range(4):
                        muda_estagio_led()
                        time.sleep(0.2)
                    buzzer.value(0)
                elif cmd == "0":
                    led.on()
            except Exception as e:
                print("Erro lendo comando:", e)

ble.irq(ble_irq)

def make_adv_payload(name=None):
    payload = bytearray(b'\x02\x01\x06')
    if name:
        payload += bytearray((len(name)+1, 0x09)) + name.encode()
    return payload

DEVICE_NAME = "ESP32-NUS"
adv_payload = make_adv_payload(DEVICE_NAME)

led.off()
ble.gap_advertise(100_000, adv_payload)
led.on()

while True:
    idle()

