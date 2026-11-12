# Extractor de Fechas con IA

Este script de Python utiliza la API de OpenAI (o compatibles) para analizar un texto, extraer las fechas clave en formato `DD/MM/AAAA` y explicar brevemente a qué se refieren y su importancia.

## Requisitos previos

Asegúrate de tener instalado Python en tu sistema. Luego, instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install openai python-dotenv
```

## Configuración (.env)

El script utiliza la librería `dotenv` para cargar las credenciales y configuraciones de forma segura. Debes crear un archivo llamado `.env` en la misma carpeta donde esté el script y añadir las siguientes variables:

```env
# Obligatorio: Tu clave de API
OPENAI_API_KEY=tu_clave_api_aqui

# Opcional: Si usas un proveedor alternativo a OpenAI (ej. LM Studio, vLLM, etc.)
# OPENAI_BASE_URL=http://localhost:1234/v1

# Opcional: El nombre del modelo que quieres usar (por defecto usa "fast")
MODELO=gpt-4o-mini
```

## Cómo ejecutar el script

El script es muy flexible y acepta el texto de entrada de tres formas distintas:

**1. Ejecución por defecto (sin parámetros)**
Si lo ejecutas sin enviarle ningún texto, el script hará una prueba automática preguntando al modelo "¿Qué hace este modelo?".
```bash
python script.py
```

**2. Pasando el texto como argumento**
Puedes pasar el texto directamente entre comillas al ejecutar el comando:
```bash
python script.py "El Apolo 11 despegó el 16 de julio de 1969 y llegó a la Luna días después."
```

**3. Leyendo desde la entrada estándar (stdin / tuberías)**
Ideal si quieres procesar el contenido de un archivo de texto o la salida de otro comando:
```bash
python script.py < mi_texto.txt
```

## Salida esperada
El script imprimirá la respuesta generada por la IA, seguida de la razón de finalización y un conteo del consumo de tokens (entrada y salida).