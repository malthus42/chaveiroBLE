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

Nos testes realizados a bateria do chaveiro fornecia energia para o sistema por aproximadamente 2 horas.

### Manual de usuário 

Baixe o arquivo main.py e utilizando a IDE thonny carregue o arquivo para o ESP32. Baixe o apk e abra-o no celular. 
Certifique-se que o dispositivo está carregado e ligado, ao clicar no botão que aparece no aplicativo o led vai acender e o buzzer vai fazer um som.


### Manual de desenvolvedor

No código do esp foram usadas as bibliotecas: bluetooth, machine e time.

A biblioteca bluetooth foi usada para ativar o bluetooth do esp, se conectar ao aplicativo  e receber o comando para ativar o buzzer e o Led.

Da biblioteca machine foram usados a classe Pin e as funções idle e freq. A classe Pin é usado para controlar os pinos de entrada e saída do esp, as funções idle e freq são usadas para diminuir o consumo de energia do esp. Foi considerado usar deepsleep para diminuir o consumo de energia, contudo essa função não foi adequada para o projeto. 

A biblioteca time foi usada para controlar o tempo que o buzzer faz barulho e o Led pisca.

No arquivo [links](./links) tem o link de onde está cada biblioteca na documentação do micropython. 

## Conclusão e Comentários 

O projeto apresentou dois desafios, diminuir o tamanho do sistema para ter o tamanho de um chaveiro e diminuir o consumo de energia para que o sistema funcione com a bateria do chaveiro por mais tempo. 

Para diminuir o tamanho do sistema, a placa de circuito impresso foi substituída por soldar os componentes diretamente. Isso ajudou a formar um componente um pouco maior que o chaveiro original. 

Para diminuir o consumo de energia, foi testado o deepsleep, entretanto a dificuldade em controlar quando o modo deepsleep começa e termina e o fato de não ser possível usar o bluetooth nesse modo fizeram com que escolheremos outra abordagem para diminuir o consumo de energia. A nova abordagem foi diminuir a frequência do processador e usar uma função de baixo consumo (idle) no loop principal. Essa abordagem resultou em uma autonomia de 2 horas.

Para usar o deepsleep seria necessário adicionar um botão a placa para controlar quando esse modo seria ligado e desligado, contudo faltou tempo para adicionar o botão e os componentes já estava colado, o que dificulta a adição do botão. 

