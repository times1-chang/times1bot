import discord
import asyncio
from discord.ext import commands
import os
import json
import random
from classes import Cog_Extension

setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents = intents)

@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)

for filename in os.listdir('.'):
    if filename.endswith('.py') and filename != 'main.py' and filename != 'classes.py':
        bot.load_extension(filename[:-3])
bot.run(os.getenv('TOKEN'))
