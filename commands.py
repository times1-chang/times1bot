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
class CmdsClass(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        print('pinging')
        await ctx.send(f'{round(self.bot.latency*1000, 2)}ms')
    @commands.command()
    async def neko(self, ctx):
        random_nekopic = random.choice(setdata['nekopic'])
        await ctx.send(random_nekopic)

    @commands.command()
    async def vocaloid(self, ctx):
        random_vcldpic = random.choice(setdata['vcldpic'])
        await ctx.send(random_vcldpic)

    @commands.command()
    async def usefulpic(self, ctx):
        random_usflpic = random.choice(setdata['usflpic'])
        await ctx.send(random_usflpic)
    #@client.event
#async def on_reaction_add(reaction, user)
def setup(bot):
    bot.add_cog(CmdsClass(bot))
