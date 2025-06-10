import csv  # Para leer el archivo CSV
from telegram import Update  # Para manejar los mensajes de Telegram
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

respuestas = {}
with open("preguntas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        respuestas[fila["pregunta"].lower()] = fila["respuesta"]
        
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    return respuestas.get(mensaje, "Lo siento, no entiendo esa pregunta.")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    respuesta = obtener_respuesta(mensaje)
    await update.message.reply_text(respuesta)
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy un chatbot. Escribe tu pregunta.")
    
if __name__ == "__main__":
    TOKEN = "7523434195:AAHTH5yc8lcnMkbCqzekZszYd9mzA7dLIuY"  # 🔒 Pega tu token de @BotFather aquí

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot de Telegram corriendo...")
    app.run_polling()
    