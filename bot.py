import os
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

activites = [
    discord.Game(name="World of Airports 3.0"),
    discord.Activity(type=discord.ActivityType.watching, name="SkyJet Alliance"),
    discord.Activity(type=discord.ActivityType.listening, name="Flight Requests")
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    change_status.start()


@tasks.loop(seconds=15)
async def change_status():
    current = activites.pop(0)
    await bot.change_presence(activity=current)
    activites.append(current)

bot.run(os.getenv("DISCORD_TOKEN"))
