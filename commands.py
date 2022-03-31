import discord
import asyncio
from discord.ext import commands
import os
import json

setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)
#client 是我們與 Discord 連結的橋樑
#intents = discord.Intents.default()
#intents.members = True
bot = commands.Bot(command_prefix='>')#, intents = intents)

@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)


@bot.command()
async def ping(ctx):
    print('pinging')
    await ctx.send(f'{round(bot.latency*1000, 2)}ms')



#@client.event
#async def on_reaction_add(reaction, user):
#    if
bot.run(os.getenv('TOKEN'))
