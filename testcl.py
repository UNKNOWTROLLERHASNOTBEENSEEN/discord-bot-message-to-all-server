import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def send_to_all_servers(ctx, *, message):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send("this is my message sub to me https://www.youtube.com/@BANDIT50010")

bot.run('MTEwNjgxODI4NTYxOTY0MjM3OQ.GjIZCw.Xpu-YgBjGzZ_MwuTgMBksSuwev0cfnXLdbgGEQ')
