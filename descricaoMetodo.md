Inicialmente para testar o ESP32 foi feito um circuito simples com um Led e um Buzzer e o ESP recebendo energia via USB, em uma protoboard. 

O segundo passo foi integrar a placa com o circuito do chaveiro led e fazer o ESP funcionar com a bateria do chaveiro. Além disso, o ESP foi programado para acender o Led e o Buzzer quando recebesse um sinal pelo Bluetooth. Nessa parte foi usado o aplicativo nRF conect para mandar o sinal.

O próximo passo é desenvolver um aplicativo para mandar o sinal Bluetooth no lugar do nRF connect.O aplicativo é simples, ele possui apenas de uma interface que permite conectar ao ESP por Bluetooth e mandar um comando.

O passo seguinte da elaboração do projeto foi criar a documentação seguindo o exemplo presente em https://github.com/FNakano/CFA2025-SampleProject.

Depois, veio a fase de testes para transferir o dispositivo da protoboard para uma placa de perfurada de circuito impresso para acomodar todos os componentes. A seguir estão as fotos dessa primeira organização: 
![](/placaDeBaixo.png)
![](/placaDeCima.png)
