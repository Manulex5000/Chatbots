import csv
import google.generativeai as genai

genai.configure(api_key="AIzaSyCMjK6pJHetmGt1YwDkodiFfaplzE6qfZE")
respuestas = {}
with open("preguntas.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        respuestas[fila["pregunta"].lower()] = fila["respuesta"]

modelo = genai.GenerativeModel('gemini-2.0-flash')

def agregar_pregunta(mensaje,respuesta_gemini):
    with open("preguntas.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([mensaje, respuesta_gemini.text.strip()])

def agregar_respuesta(mensaje,respuesta_gemini):
    with open("preguntas.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([mensaje, ""])

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
        respuesta_gemini = modelo.generate_content(mensaje)
        agregar_pregunta(mensaje,respuesta_gemini)
        agregar_respuesta(mensaje,respuesta_gemini)
        return respuesta_gemini.text.strip()
    
while True:
    usuario = input("Tú: ")
    if usuario.lower() == "salir":
        break
    respuesta = obtener_respuesta(usuario)
    print("Chatbot:", respuesta)
        