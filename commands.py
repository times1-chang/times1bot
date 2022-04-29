import discord
import asyncio
from discord.ext import commands
import os
import json
import random
from classes import Cog_Extension
import datetime
setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)
class CmdsClass(Cog_Extension):
    @commands.command()
    async def helps(self, ctx):
        embed=discord.Embed(title="Help", description="about times1 bot", color=0x720ab8)
        embed.set_author(name="乘一", icon_url="https://64.media.tumblr.com/2061fee2529724d19321133f8b0e767d/e870751fd1d65c5f-c7/s400x600/d5020280b116871dbf935ac2837991ff3bdcd72d.jpg")
        embed.set_thumbnail(url="https://d3mww1g1pfq2pt.cloudfront.net/Image/ckjconmb94vs408761xsx2ywp/1625477488941.jpg")
        embed.add_field(name=">ping", value="check network latency", inline=False)
        embed.add_field(name=">roll value1 value2", value="return random number from value1~value2 (default is 1~30)", inline=False)
        embed.add_field(name=">meme", value="return random meme", inline=False)
        embed.add_field(name=">neko", value="return random catgirl picture", inline=False)
        embed.add_field(name=">vocaloid", value="return random vocaloid picture", inline=False)
        embed.add_field(name="randh", value="return random adult comic", inline=False)
        await ctx.send(embed=embed)
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
    async def meme(self, ctx):
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
