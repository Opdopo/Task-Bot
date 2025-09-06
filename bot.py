import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hey there!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

# Keep this at the bottom
token = os.environ.get("DISCORD_TOKEN")
if token is None:
    print("Error: DISCORD_TOKEN environment variable is not set!")
else:
    bot.run(MTQxMzc4MTQxOTQyNzEwMjczMA.GZ89hR.qrBK9lwnJiPyqTfjTwQihUwZz16SDGWAXpa_g4)
