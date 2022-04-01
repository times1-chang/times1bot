import discord
import asyncio
from discord.ext import commands
import os
import json
import random
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
@bot.command()
async def neko(ctx):
    random_nekopic = random.choice(setdata['nekopic'])
    await ctx.send(random_nekopic)

@bot.command()
async def vocaloid(ctx):
    random_vcldpic = random.choice(setdata['vcldpic'])
    await ctx.send(random_vcldpic)

@bot.command()
async def usefulpic(ctx):
    random_usflpic = random.choice(setdata['usflpic'])
    await ctx.send(random_usflpic)
#@client.event
#async def on_reaction_add(reaction, user):
#    if
bot.run(os.getenv('TOKEN'))
