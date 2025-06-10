import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Configura tu API key de Gemini
GEMINI_API_KEY = "AIzaSyCMjK6pJHetmGt1YwDkodiFfaplzE6qfZE"
genai.configure(api_key=GEMINI_API_KEY)

# Crea el modelo de Gemini
modelo = genai.GenerativeModel("gemini-2.0-flash")

def obtener_respuesta(mensaje):
    try:
        respuesta = modelo.generate_content(mensaje)
        return respuesta.text.strip()
    except Exception as e:
        print("Error al generar respuesta:", e)
        return "Lo siento, hubo un problema al procesar tu pregunta."
    
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    respuesta = obtener_respuesta(mensaje)
    await update.message.reply_text(respuesta)
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy un chatbot con inteligencia artificial. Pregúntame lo que quieras.")
    
if __name__ == "__main__":
    TOKEN = "7523434195:AAHTH5yc8lcnMkbCqzekZszYd9mzA7dLIuY"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot corriendo con Gemini...")
    app.run_polling()