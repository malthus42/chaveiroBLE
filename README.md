Projeto da disciplina ACH2157 - Computação Física e Aplicações (2025)

# chaveiroIOT

## Objetivo(s)

Adaptar um chaveiro Led para usá-lo como um dispositivo de localização de objetos por meio de sinais sonoros e luminosos.
Para isso:
* Adicionar um buzzer para fazer som
* Conectar um esp32 ao chaveiro para ligar o dispositivo 
* Criar um aplicativo para conectar e controlar o esp32 pelo celular

## Introdução 

Para lidar com o problema de encontrar objetos próximos em um ambiente, propõe-se adaptar um chaveiro Led Para transformá-lo em um dispositivo de localização. 

Este dispositivo deve emitir um sinal sonoro e um sinal luminoso e ser controlado pelo celular. 

Do ponto de vista construtivo é um sistema de informação composto por circuito físico, interfaces de uso e de comunicação Bluetooth.

## Método (de execução do projeto)

Usou-se o método descrito em ... O tipo de projeto é forma de documentação foram escolhidos com base nas diretrizes da disciplina https://github.com/FNakano/CFA/blob/master/diretrizes.md .

A aplicação executada no dispositivo tem vários arquivos. (Que foram copiados para esse repositório...)

## Resultados 

### Como reproduzir este dispositivo 

#### Lista de Materiais

| Nome | Quantidade | link para foto do componente, de fato, utilizado |
| ... | ... | ... |
| Placa de desenvolvimento Ai-Thinker ESP32-C3 | 1 | Figura x, ... |
| Protoboard | 1 | Na figura x, ... |
| Buzzer | 1 | Na figura x, ... |
| chaveiro led | 1 | Na figura y, ... |

#### Montagem

##### Lista de conexões 

Tabela de conexões: 
| Placa da lanterna | Pino da placa  de desenvolvimento | Pino no Buzzer |
| ... | ... | ... |
| GND | GND | GND |
| VCC | V3 | ---|
| Pino de controle do Led | 3 | --- |
| --- | 4 | Positivo |

#### Carga do programa em um novo dispositivo 

1. Copie somente a pasta `src` e seu conteúdo;
2. Entre na pasta `src`;
3. Transfira para o dispositivo usando `rshell` com o comando `cp -r * /pyboard/`;
4 Feche Russell com o comando `exit`;
5. Abra o Thonny; 
6. Na janela de comando do Thonny dê o comando `import startsystem`;

#### Teste de uso

...

### Manual de usuário 

...


### Manual de desenvolvedor

...

## Conclusão e Comentários 

...

