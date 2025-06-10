import requests

def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        clima = {
            "ciudad": datos["name"],
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"],
            "humedad": datos["main"]["humidity"],
            "viento": datos["wind"]["speed"]
        }
        return clima
    else:
        return {"error": "No se pudo obtener el clima."}

if __name__ == "__main__":
    ciudad = input("Ingrese el nombre de la ciudad: ")
    api_key = "f9248ad6b9352ca10eeae4ddec4b1ff2"
    clima = obtener_clima(ciudad, api_key)
if "error" in clima:
    print(clima["error"])
else:
    print(f"Clima en {clima['ciudad']}:")
    print(f"Temperatura: {clima['temperatura']}°C")
    print(f"Descripción: {clima['descripcion']}")
    print(f"Humedad: {clima['humedad']}%")
    print(f"Viento: {clima['viento']} m/s")

               

