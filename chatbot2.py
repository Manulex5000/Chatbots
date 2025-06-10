import csv
respuestas ={}
#leer un cvs con encabezados
with open("preguntas.csv", "r") as archivo: 
    lector = csv.DictReader(archivo)
    for fila in lector:
        respuestas[fila["pregunta"]]=fila["respuesta"]    # Accede a columnas específicas       

def agregar_pregunta(mensaje):
    print("metodo agregar")
    with open("salida.csv")
    mensaje = mensaje.lower()
    if mensaje in respuestas:
        return respuestas[mensaje]

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
        return "Lo siento, no entiendo esa pregunta."
#Se muestra un mensaje de bienvenida e instrucción para salir del programa escribiendo "salir".
print("¡Hola! Soy un chatbot. Escribe 'salir' para terminar la conversación.")
#Este bucle permite que el usuario interactúe continuamente con el chatbot hasta escribir "salir".
while True:
    usuario = input("Tú: ")
    if usuario.lower() == "salir":
        print("Chatbot: ¡Adiós!")
        break
    respuesta = obtener_respuesta(usuario)
    print("Chatbot:", respuesta)