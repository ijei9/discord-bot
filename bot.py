import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

TOKEN = os.getenv("DISCORD_TOKEN")
client.run("MTUwNTA4MzA3NDI4NTc5NzQyNg.G5veE_.Q7PrIq17L1wIebJpD6D2CpM2lPI3wnZxcH-GAY")