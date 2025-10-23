Projeto da disciplina ACH2157 - Computação Física e Aplicações (2025)

# chaveiroIOT

## Objetivo(s)

Adaptar um chaveiro Led para usá-lo como um dispositivo de localização de objetos por meio de sinais sonoros e luminosos.
Para isso:
* Adicionar um buzzer para fazer som
* Conectar um esp32 ao chaveiro para ligar o dispositivo 
* Criar um aplicativo para conectar e controlar o esp32 pelo celular

## Introdução 

Para lidar com o problema de encontrar objetos próximos em um ambiente, propõe-se adaptar um chaveiro Led para transformá-lo em um dispositivo de localização. 

Este dispositivo deve emitir um sinal sonoro e um sinal luminoso e ser controlado pelo celular. 

Do ponto de vista construtivo é um sistema de informação composto por circuito físico, interfaces de uso e de comunicação Bluetooth.

## Método (de execução do projeto)

Usou-se o método descrito em [Método](./descricaoMetodo.md) . O tipo de projeto é forma de documentação foram escolhidos com base nas diretrizes da disciplina https://github.com/FNakano/CFA/blob/master/diretrizes.md .

A aplicação executada no dispositivo tem vários arquivos. (Que foram copiados para esse repositório...)

## Resultados 

### Como reproduzir este dispositivo 

#### Lista de Materiais

| Nome | Quantidade | link para foto do componente, de fato, utilizado |
| --- | --- | --- |
| Placa de desenvolvimento Ai-Thinker ESP32-C3 | 1 | Figura x, ... |
| Protoboard | 1 | Na figura x, ... |
| Buzzer | 1 | Na figura x, ... |
| chaveiro led | 1 | Na figura y, ... |

#### Montagem

##### Lista de conexões 

Tabela de conexões: 
| Placa da lanterna | Pino da placa  de desenvolvimento | Pino no Buzzer |
| --- | --- | --- |
| GND | GND | GND |
| VCC | V3 | ---|
| Pino de controle do Led | 3 | --- |
| --- | 4 | Positivo |

#### Carga do programa em um novo dispositivo 

Baixe o arquivo main.py e utilizando a IDE thonny carregue o arquivo para o ESP32.


#### Teste de uso

...

### Manual de usuário 

Baixe o arquivo main.py e utilizando a IDE thonny carregue o arquivo para o ESP32. Baixe o apk e abra-o no celular. 
Certifique-se que o dispositivo está carregado e ligado, ao clicar no botão que aparece no aplicativo o led vai acender e o buzzer vai fazer um som.


### Manual de desenvolvedor

...

## Conclusão e Comentários 

...

