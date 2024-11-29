# Comparação entre protocolos TCP e UDP

Redes de Computadores II  
Universidade Federal do Paraná  
Departamento de Informática  
Bacharelado em Ciência da Computação  

Eduardo Gabriel Kenzo Tanaka - GRR20211791  
Vinícius Yuji Hara - GRR20211763

### Descrição

Este trabalho tem como objetivo comparar o desempenho dos protocolos TCP e UDP. Para isso, foram consideradas as metricas de tempo, vazão e perda de dados na transferencia de arquivos e transferencia em memória principal entre servidor e cliente.  
Os programas de teste foram implementados em python utilizando as bibliotecas:  
**socket** para comunicação entre as máquinas;  
**time** para contagem de tempo;   
**matplotlib** para plotagem de gráficos a partir dos dados coletados.

### Projeto

#### 19/11: Defiição de métricas e casos de comparação
Serão consideradas as métricas tempo, vazão e quantidade de pacotes perdidos, para os seguintes casos de envio de dados: com/sem fragmentação e com/sem checksum.

#### Executando o trabalho
Para executar o trabalho utilizando conexão TCP é utilzado os arquivos cliente_tcp.py e server_tcp.py e para a conexão UDP é utilizado os arquivos cliente_udp.py e server_udp.py.

Para executar o server tem como exemplo abaixo:
```
python3 server_udp.py host
```
Em que o 'host' é o nome da máquina do server

Para executar o server tem como exemplo abaixo:

```
python3 cliente_udp.py metrica tam_pacote nome_arquivo host num_bytes
```
Em que a 'métrica' pode ser "arquivo" para transferência de arquivo ou "memoria" para transferir em memória principal.
'tam_pacote' é o tamanho em bytes que o server vai mandar em cada pacote.
'nome_arquivo' é o arquivo que o cliente deseja obter do server ou escrever em seu diretório
'host' é o nome da máquina do server
'num_bytes' é o tamanho de bytes a ser transferido em memória, para arquivos usa-se 0.

Exemplo para o server:
```
python3 server_udp.py i29
```

Exemplos para o cliente:
```
python3 cliente_udp.py arquivo 1024 exemplo.txt i29 0
```
```
python3 cliente_udp.py memoria 1024 exemplo.txt i29 100000
```
### Conclusões
