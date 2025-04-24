# Projeto de Metadatas (Metadados)

Muitas empresas de telecom precisam transferir ou receber dados importantes para controle de operação, montagem de relatórios dentre outros pontos.
Um arquivo de metadados contém diversos tipos de dados sobre determinado arquivo.
Ao ter um áudio de nome "213213213.mp3", você não consegue saber quem era o cliente, o dia da ligação, o documento deste cliente etc só pelo nome do áudio.
Logo, arquivos de metadados ajudam as empresas a ter um controle melhor do atendimento, podendo filtrar diferentes tipos de áudios para trabalhos diversos.

O projeto contempla a simulação da criação de arquivos metadados CSV com os dados de atendimentos a partir dos áudios encontrados em determinada pasta.
O fluxo de processo é de:
    1. O script busca uma pasta com áudios gravados
    2. A partir do nome dos áudios, o script recupera o id do atendimento
    3. Pelo id de atendimento, o script busca no BD (neste projeto, será Postgres) os metadados de cada atendimento.
    4. O script gera um CSV final com os dados recuperados.

## Objetivo de estudos
Por este projeto, visa-se estudar:

- O conceito de metadatas
- Uso autoescalavél de Queue e Threads
- Arquitetura em camadas
- Confiabilidade em casos de erro 
- Conexão com Postgres no Python
- Testes unitários 

## Padrão de nomenclatura de áudios
atendimento_{id}.mp3 ou atendimento_{id}.wav

## exemplo de .env
AUDIO_PATH='audios/'

DATASOURCE_HOST='localhost'
DATASOURCE_PORT='5432'
DATASOURCE_DB='SRC'
DATASOURCE_USER='seu_usuario'
DATASOURCE_PASSWORD='sua_senha'
