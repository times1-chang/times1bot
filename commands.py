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
    '''
    @commands.command()
    async def roll(self, ctx, arg1, arg2):
        if (arg1 and arg2) and int(arg1)<=int(arg2):
            await ctx.send(random.randint(int(arg1),int(arg2)))
        elif (arg1 and arg2):
            await ctx.send("Error")
        elif not(arg1 and arg2):
            await ctx.send(random.randint(1,30))
        else:
            await ctx.send(random.randint(1,30))
    '''

    @commands.command()
    async def roll(self, ctx):
        msg = ctx.message.content.split(" ",2)
        if len(msg)==1:
            await ctx.send(random.randint(1, 30))
        elif len(msg)==3 and msg[1]<=msg[2]:
            await ctx.send(random.randint(int(msg[1]), int(msg[2])))
        else:
            await ctx.send("Error")

    @commands.command()
    async def randh(self, ctx):
        await ctx.send(random.randint(100000, 400000))
    #@client.event
#async def on_reaction_add(reaction, user)
def setup(bot):
    bot.add_cog(CmdsClass(bot))
