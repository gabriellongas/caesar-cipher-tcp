# Comunicação Segura usando Diffie-Hellman e Cifra de César

## Visão Geral

Este projeto demonstra uma implementação simples de comunicação segura entre um cliente e um servidor, utilizando o protocolo de troca de chaves Diffie-Hellman e a Cifra de César para criptografia e descriptografia de mensagens. O projeto é composto por scripts Python para o cliente e o servidor, além de utilitários para geração de números primos e a técnica de criptografia da Cifra de César.

## Estrutura do Projeto

- **`tcpserver.py`**: Implementa a aplicação do lado do servidor, que gerencia conexões de clientes, troca chaves usando Diffie-Hellman e comunica mensagens criptografadas usando a Cifra de César.
- **`tcpclient.py`**: Implementa a aplicação do lado do cliente, que se conecta ao servidor, troca chaves usando Diffie-Hellman e comunica mensagens criptografadas usando a Cifra de César.
- **`diffie_hellman.py`**: Contém a implementação do protocolo de troca de chaves Diffie-Hellman.
- **`prime.py`**: Fornece funções para gerar números primos aleatórios e verificar a primalidade, utilizados na troca de chaves Diffie-Hellman.
- **`caesar_cipher.py`**: Implementa as funções de criptografia e descriptografia da Cifra de César.

## Como Funciona

1. **Troca de Chaves**: 
   - O servidor e o cliente geram suas chaves privadas e utilizam o protocolo Diffie-Hellman para trocar chaves públicas sobre um canal inseguro.
   - Tanto o servidor quanto o cliente calculam uma chave secreta compartilhada utilizando suas chaves privadas e a chave pública recebida da outra parte.

2. **Criptografia e Descriptografia de Mensagens**:
   - A chave secreta compartilhada é usada como valor de deslocamento para a Cifra de César.
   - Mensagens enviadas do cliente para o servidor (e vice-versa) são criptografadas usando essa chave compartilhada.
   - Ao receber uma mensagem, a parte receptora a descriptografa usando a mesma chave compartilhada.

## Configuração e Uso

### Pré-requisitos

- Python 3.x

### Executando o Projeto

1. Execute o servidor com o comando:
   ```bash
   python.exe tcpserver.py
   ```
2. Execute o client com o comando:
   ```bash
   python.exe tcpclient.py
