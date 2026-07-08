from main import *
import discord
from discord.ext import commands
import dotenv
import os
import requests

dotenv.load_dotenv()


TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    
@bot.command()
async def chat(ctx, *, prompt):
    try:
        response = ai.generate_ai_response(prompt)
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")
        
@bot.command()
async def clima(ctx, city: str = "Madrid"):
    urlclimate = f"https://api.open-meteo.com/v1/forecast?city={city}&current_weather=true"
    try:
        response = requests.get(urlclimate)
        data = response.json()
        current_weather = data.get("current_weather", {})
        temperature = current_weather.get("temperature")
        windspeed = current_weather.get("windspeed")
        weather_message = f"El clima actual en {city} es:\nTemperatura: {temperature}°C\nVelocidad del viento: {windspeed} km/h"
        await ctx.send(weather_message)
    except Exception as e:
        await ctx.send(f"Error al obtener el clima: {str(e)}")
     
@bot.command()
async def consejo(ctx):
    try:
        response = ai.get_consejo()
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")
           
bot.run(TOKEN)