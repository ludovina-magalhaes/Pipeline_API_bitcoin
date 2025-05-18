#  Proyecto: Pipeline ETL de Datos de Bitcoin

Este proyecto implementa un **pipeline ETL (Extracción, Transformación y Carga)** para recolectar, procesar y almacenar datos del precio del **Bitcoin** en tiempo real. Los datos se extraen desde la **API de Coinbase**, se transforman a un formato adecuado y se almacenan en una base de datos **PostgreSQL** alojada en la nube. La visualización de los datos se realiza a través de un **dashboard interactivo con Streamlit**.

---

##  Tecnologías Utilizadas

- **Python** – Lenguaje principal del proyecto  
- **Requests** – Para hacer solicitudes HTTP a la API  
- **psycopg2 / SQLAlchemy** – Para interactuar con PostgreSQL  
- **dotenv** – Para gestionar variables de entorno  
- **PostgreSQL** – Base de datos relacional  
- **Coinbase API** – Fuente de datos del precio del Bitcoin  
- **Streamlit** – Para construir el dashboard web

---

##  Estructura del Pipeline

1. **Extracción (Extract)**  
   - Los datos se obtienen desde la **API de Coinbase** utilizando la biblioteca `requests`.  

2. **Transformación (Transform)**  
   - Los datos JSON se procesan directamente con Python.  
   - Se renombran los campos:  
     `amount` → `valor`, `base` → `criptomoneda`, `currency` → `moneda`  
   - Se agrega un campo **timestamp** con la fecha y hora de extracción.

3. **Carga (Load)**  
   - Inicialmente se usó la base **TinyDB** (NoSQL local) como prueba de concepto.  
   - Posteriormente, los datos se migraron a una base **PostgreSQL** en la nube mediante **Render**.  
   - La carga se realiza con `SQLAlchemy`, que gestiona la creación de tablas y la inserción de datos.

4. **Automatización**  
   - El pipeline se ejecuta en un **bucle continuo**, con una pausa de 12 segundos entre ciclos (`time.sleep()`).  
   - Aunque simple, esta automatización permite simular orquestadores como Airflow.

5. **Dashboard**  
   - Los datos almacenados se visualizan con **Streamlit** directamente desde PostgreSQL.  
   - El dashboard muestra el **precio actual** y la **evolución histórica** del Bitcoin.

---

##  Configuración del Entorno

1. **Instalar dependencias:**

```bash
pip install requests psycopg2-binary python-dotenv SQLAlchemy streamlit
```

2. **Crear el archivo `.env`:**

```env
DB_NAME=nombre_de_la_base
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=host
DB_PORT=puerto
```

3. **Configurar la base de datos PostgreSQL:**  
   - Asegúrese de que la base esté activa y accesible.  
   - Recomendación: usar [Render](https://render.com/) para alojamiento gratuito.

---

##  Estructura del Código

| Función                     | Descripción |
|----------------------------|-------------|
| `extract_bitcoin_data()`   | Solicita datos desde la API de Coinbase |
| `transform_bitcoin_data(data)` | Formatea los datos y agrega timestamp |
| `load_bitcoin_postgres(data)` | Inserta los datos en PostgreSQL |
| `create_table()`           | Crea la tabla `bitcoin_data` si no existe |

---

##  Ejecución

1. **Iniciar el script:**

```bash
python script.py
```

2. **Monitorear la ejecución:**  
   - El script muestra logs sobre extracción, transformación y carga.

3. **Interrumpir manualmente:**  
   - Presionar `Ctrl+C`.

---

##  Estructura de la Tabla

| Columna       | Tipo         | Descripción                    |
|---------------|--------------|--------------------------------|
| id            | SERIAL       | Identificador único            |
| valor         | NUMERIC      | Precio del Bitcoin             |
| criptomoneda  | VARCHAR(10)  | Código de la criptomoneda      |
| moneda        | VARCHAR(10)  | Moneda de referencia           |
| timestamp     | TIMESTAMP    | Fecha y hora de recolección    |

---

##  Notas

- Verifique que la **API de Coinbase** esté accesible.  
- El intervalo entre ejecuciones (`time.sleep`) puede ser ajustado.  
- Asegúrese de configurar correctamente las variables de entorno en el archivo `.env`.

---

##  Contribuciones

¡Las contribuciones son bienvenidas!  
Puede abrir un *issue* con sugerencias o enviar un *pull request* con mejoras.

---

##  Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.  
Consulte el archivo `LICENSE` para más información.
