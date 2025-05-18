# README

## Projeto: Pipeline de Recolha e Armazenamento de Dados do Bitcoin

Este projeto implementa um pipeline ETL (Extração, Transformação e Carregamento) para recolher, processar e armazenar dados sobre o preço do Bitcoin numa base de dados PostgreSQL. Utiliza a API da Coinbase para obter os preços em tempo real, transforma os dados para um formato adequado e insere-os numa tabela da base de dados.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Requests**: Biblioteca para efetuar chamadas HTTP.
- **psycopg2**: Biblioteca para interagir com a base de dados PostgreSQL.
- **dotenv**: Biblioteca para gerir variáveis de ambiente.
- **PostgreSQL**: Base de dados utilizada para armazenar os dados recolhidos.
- **Coinbase API**: Fonte dos dados sobre o preço do Bitcoin.

## Configuração do Ambiente
Antes de executar o projeto, certificar que o ambiente está devidamente configurado:

1. **Instale as dependências necessárias:**
  
     ``` pip install requests psycopg2 python-dotenv   ```
 

2. **Configure as variáveis de ambiente:**
   Crie um ficheiro '.env' na raiz do projeto e adicione as seguintes variáveis:
      ```
   DB_NAME=nome_da_base
   DB_USER=utilizador
   DB_PASSWORD=senha
   DB_HOST=host_da_base
   DB_PORT=porta
   ```

3. **Base de Dados:**
   Certifique-se de que a base de dados PostgreSQL está configurada e acessível.

## Estrutura do Código

### Funções Principais
- **extract_bitcoin_data()**: Obtém os dados do preço do Bitcoin através da API da Coinbase.
- **transform_bitcoin_data(data)**: Transforma os dados recebidos num formato adequado para a base de dados, incluindo a conversão de tipos e adição de um timestamp.
- **load_bitcoin_postgres(data)**: Insere os dados transformados na tabela da base de dados PostgreSQL.
- **create_table()**: Cria a tabela `bitcoin_data` na base de dados, caso ainda não exista.

## Execução

### Criação da Tabela
Ao iniciar, o código verifica se a tabela existe na base de dados e cria-a caso necessário.

### Loop Principal
O programa executa continuamente o processo ETL (Extração, Transformação e Carregamento) a cada 12 segundos. Pode ser interrompido manualmente pressionando `Ctrl+C`.

### Uso
1. **Iniciar o programa:**
   `python script.py`
   

2. **Monitorizar a execução:**
   O script irá exibir logs informando sobre:
   - Criação/verificação da tabela.
   - Sucesso no carregamento de dados.
   - Erros em caso de falhas.

3. **Interromper a execução:**
   Para encerrar, pressione `Ctrl+C`.

## Estrutura da Tabela
A tabela na base de dados PostgreSQL tem a seguinte estrutura:

| Coluna       | Tipo         | Descrição                      |
|-------------|------------|---------------------------------|
| id          | SERIAL     | Identificador único            |
| valor       | NUMERIC    | Preço do Bitcoin               |
| criptomoeda | VARCHAR(10)| Código da criptomoeda         |
| moeda       | VARCHAR(10)| Moeda de referência           |
| timestamp   | TIMESTAMP  | Data e hora da recolha         |

## Observações
- Certifique-se de que a API da Coinbase está acessível.
- Pode ajustar o intervalo de tempo (`time.sleep`) conforme necessário.
- Garanta que as variáveis de ambiente estão corretamente configuradas.

## Contribuição
Contribuições são bem-vindas! Para sugerir melhorias ou corrigir problemas, crie uma *issue* ou envie um *pull request*.

## Licença
Este projeto está disponível sob a Licença MIT. Consulte o ficheiro `LICENSE` para mais detalhes.

# Pipeline_API_bitcoin
