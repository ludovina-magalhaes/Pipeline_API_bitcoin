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
📊 Proyecto: Pipeline ETL de Datos de Bitcoin
Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) para recolectar, procesar y almacenar datos del precio del Bitcoin en tiempo real. Los datos se extraen desde la API de Coinbase, se transforman a un formato adecuado y se almacenan en una base de datos PostgreSQL alojada en la nube. La visualización de los datos se realiza a través de un dashboard interactivo con Streamlit.

⚙️ Tecnologías Utilizadas
Python – Lenguaje principal del proyecto

Requests – Para hacer solicitudes HTTP a la API

psycopg2 / SQLAlchemy – Para interactuar con PostgreSQL

dotenv – Para gestionar variables de entorno

PostgreSQL – Base de datos relacional

Coinbase API – Fuente de datos del precio del Bitcoin

Streamlit – Para construir el dashboard web

🏗️ Estructura del Pipeline
Extracción (Extract)

Los datos se obtienen desde la API de Coinbase utilizando la biblioteca requests.

También se incluye un ejemplo de extracción desde la API de la NASA.

Transformación (Transform)

Los datos JSON se procesan directamente con Python.

Se renombran los campos:
amount → valor, base → criptomoneda, currency → moneda

Se agrega un campo timestamp con la fecha y hora de extracción.

Carga (Load)

Inicialmente se usó la base TinyDB (NoSQL local) como prueba de concepto.

Posteriormente, los datos se migraron a una base PostgreSQL en la nube mediante Render.

La carga se realiza con SQLAlchemy, que gestiona la creación de tablas y la inserción de datos.

Automatización

El pipeline se ejecuta en un bucle continuo, con una pausa de 12 segundos entre ciclos (time.sleep()).

Aunque simple, esta automatización permite simular orquestadores como Airflow.

Dashboard

Los datos almacenados se visualizan con Streamlit directamente desde PostgreSQL.

El dashboard muestra el precio actual y la evolución histórica del Bitcoin.

🧪 Configuración del Entorno
Instalar dependencias:

bash
Copiar
Editar
pip install requests psycopg2-binary python-dotenv SQLAlchemy streamlit
Crear el archivo .env:

env
Copiar
Editar
DB_NAME=nombre_de_la_base
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=host
DB_PORT=puerto
Configurar la base de datos PostgreSQL:

Asegúrese de que la base esté activa y accesible.

Recomendación: usar Render para alojamiento gratuito.

🧩 Estructura del Código
Función	Descripción
extract_bitcoin_data()	Solicita datos desde la API de Coinbase
transform_bitcoin_data(data)	Formatea los datos y agrega timestamp
load_bitcoin_postgres(data)	Inserta los datos en PostgreSQL
create_table()	Crea la tabla bitcoin_data si no existe

🏃‍♂️ Ejecución
Iniciar el script:

bash
Copiar
Editar
python script.py
Monitorear la ejecución:

El script muestra logs sobre extracción, transformación y carga.

Interrumpir manualmente:

Presionar Ctrl+C.

🗃️ Estructura de la Tabla
Columna	Tipo	Descripción
id	SERIAL	Identificador único
valor	NUMERIC	Precio del Bitcoin
criptomoneda	VARCHAR(10)	Código de la criptomoneda
moneda	VARCHAR(10)	Moneda de referencia
timestamp	TIMESTAMP	Fecha y hora de recolección

📝 Notas
Verifique que la API de Coinbase esté accesible.

El intervalo entre ejecuciones (time.sleep) puede ser ajustado.

Asegúrese de configurar correctamente las variables de entorno en el archivo .env.

🤝 Contribuciones
¡Las contribuciones son bienvenidas!
Puede abrir un issue con sugerencias o enviar un pull request con mejoras.

📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT.
Consulte el archivo LICENSE para más información.
