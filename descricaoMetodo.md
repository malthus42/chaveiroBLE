Inicialmente para testar o ESP32 foi feito um circuito simples com um Led e um Buzzer e o ESP recebendo energia via USB. 

O segundo passo foi substituir o Led pelo chaveiro e fazer o ESP funcionar com a bateria do chaveiro. Além disso, o ESP foi programado para acender o Led e o Buzzer quando recebesse um sinal pelo Bluetooth. Nessa parte foi usado o aplicativo nRF conect para mandar o sinal.

O próximo passo é desenvolver um aplicativo para mandar o sinal Bluetooth no lugar do nRF connect. (Parte que ainda vamos fazer) O aplicativo é simples, ele precisa apenas de uma interface que permita conectar ao ESP por Bluetooth e mandar uma mensagem.

Para finalizar, durante a elaboração do projeto foi criado a documentação seguindo o exemplo presente em https://github.com/FNakano/CFA2025-SampleProject