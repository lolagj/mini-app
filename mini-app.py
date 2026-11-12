import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # carga la clave y la dirección del servicio desde .env

client = OpenAI()  # lee OPENAI_API_KEY y OPENAI_BASE_URL del entorno
MODELO = os.getenv("MODELO", "fast")


mensaje = ""

if len(sys.argv) > 1:
    mensaje = sys.argv[1].strip()
elif not sys.stdin.isatty():
    mensaje = sys.stdin.read().strip()


if not mensaje:
    response = client.chat.completions.create(
        model=MODELO,
        max_completion_tokens=500,  # límite de la respuesta, en tokens
        messages=[
            {"role":"system", "content":"Devuelve las fechas clave del texto en formato DD/MM/AAAA. Describe de forma breve a qué se refiere esa fecha y qué importancia tiene."},
            {"role": "user", "content": "¿Qué hace este modelo?"}
        ],
    )
    eleccion = response.choices[0]
    print(eleccion.message.content or "(respuesta vacía)")
    print(f"\n[fin] {eleccion.finish_reason}")
    print(
    f"[tokens] entrada={response.usage.prompt_tokens} "
    f"salida={response.usage.completion_tokens}"
    )
    sys.exit(0)  

response = client.chat.completions.create(
    model=MODELO,
    max_completion_tokens=500,  # límite de la respuesta, en tokens
    messages=[
        {"role":"system", "content":"Devuelve las fechas clave del texto en formato DD/MM/AAAA. Describe de forma breve a qué se refiere esa fecha y qué importancia tiene. Indica al inicio de la respuesta qué hace el modelo"},
        {"role": "user", "content": mensaje}
    ],
)


eleccion = response.choices[0]
print(eleccion.message.content or "(respuesta vacía)")


print(f"\n[fin] {eleccion.finish_reason}")
print(
    f"[tokens] entrada={response.usage.prompt_tokens} "
    f"salida={response.usage.completion_tokens}"
)