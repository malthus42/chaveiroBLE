import React, { useState, useEffect } from 'react';
import { SafeAreaView, View, Button, Text, PermissionsAndroid, Platform, Alert } from 'react-native';
import { BleManager, Device } from 'react-native-ble-plx';
import { Buffer } from 'buffer';

const DEVICE_NAME = "ESP32-NUS";
const NUS_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E";
const NUS_RX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E";

export default function App() {
  const [bleManager] = useState(new BleManager());
  const [device, setDevice] = useState<Device | null>(null);
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    // Solicitar permissões no Android >= 6.0
    if (Platform.OS === "android" && Platform.Version >= 23) {
      PermissionsAndroid.requestMultiple([
        PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
        PermissionsAndroid.PERMISSIONS.BLUETOOTH_SCAN,
        PermissionsAndroid.PERMISSIONS.BLUETOOTH_CONNECT
      ]);
    }
  }, []);

  const scanAndConnect = () => {
    bleManager.startDeviceScan(null, null, (error, scannedDevice) => {
      if (error) {
        console.log("Scan error:", error);
        return;
      }

      if (scannedDevice && scannedDevice.name === DEVICE_NAME) {
        bleManager.stopDeviceScan();
        scannedDevice.connect()
          .then((d) => d.discoverAllServicesAndCharacteristics())
          .then((d) => {
            setDevice(d);
            setConnected(true);
            Alert.alert("Conectado", `Conectado ao ${DEVICE_NAME}`);
          })
          .catch((err) => console.log("Conexão falhou:", err));
      }
    });
  };

  const sendCommand = (cmd: string) => {
    if (!device) return;

    const base64Cmd = Buffer.from(cmd, 'utf8').toString('base64');

    device.writeCharacteristicWithResponseForService(
      NUS_SERVICE_UUID,
      NUS_RX_UUID,
      base64Cmd
    ).then(() => {
      Alert.alert("Comando enviado", cmd);
    }).catch((err) => console.log("Erro enviando comando:", err));
  };

  return (
    <SafeAreaView style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <View style={{ marginBottom: 20 }}>
        <Button title="Conectar" onPress={scanAndConnect} disabled={connected}/>
      </View>
      <View>
        <Button title="ON" onPress={() => sendCommand("1")} disabled={!connected}/>
      </View>
      <Text style={{ marginTop: 20 }}>
        {connected ? "Dispositivo conectado" : "Dispositivo desconectado"}
      </Text>
    </SafeAreaView>
  );
}
