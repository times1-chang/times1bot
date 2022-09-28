import discord
import asyncio
from discord.ext import commands
import os
import json
import random
from classes import Cog_Extension
from datetime import datetime, timezone, timedelta
import requests
from bs4 import BeautifulSoup
import re

cookies = {'fringeBenefits': 'yup'}
setdata = ''
tododic = {}

tz = timezone(timedelta(hours=+8))
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)
class CmdsClass(Cog_Extension):
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help", description="about times1 bot", color=0x720ab8, timestamp=datetime.now().astimezone(tz))
        embed.set_author(name="乘一", icon_url="https://64.media.tumblr.com/2061fee2529724d19321133f8b0e767d/e870751fd1d65c5f-c7/s400x600/d5020280b116871dbf935ac2837991ff3bdcd72d.jpg")
        embed.set_thumbnail(url="https://d3mww1g1pfq2pt.cloudfront.net/Image/ckjconmb94vs408761xsx2ywp/1625477488941.jpg")
        embed.add_field(name=">ping", value="check network latency", inline=False)
        embed.add_field(name=">roll <value1> <value2>", value="return random number from value1~value2 (default is 1~30)", inline=False)
        embed.add_field(name=">meme", value="return random meme", inline=False)
        embed.add_field(name=">neko", value="return random catgirl picture", inline=False)
        embed.add_field(name=">vocaloid", value="return random vocaloid picture", inline=False)
        embed.add_field(name=">randh", value="return random adult comic", inline=False)
        embed.add_field(name=">hpic <tag>", value="return a pic of that tag", inline=False)
        embed.add_field(name=">hpic <r/rand/random>", value="return random adult pic", inline=False)
        embed.add_field(name=">hcomic <six-digit number>", value="return a adult comic", inline=False)
        embed.add_field(name=">hcomic <r/rand/random>", value="return random adult comic", inline=False)
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

    @commands.command()
    async def hpic(self, ctx, tag:str):
        if tag == "r" or tag=="random" or tag=="rand" :
            print("randomsend!")
            mainhtml = requests.get("https://gelbooru.com/index.php?page=post&s=random")
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            link = mainsoup.find("meta", property="og:image")
            await ctx.send(link["content"])
        else:
            mainhtml = requests.get(f"https://gelbooru.com/index.php?page=post&s=list&tags={tag}", cookies=cookies)
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            try:
                newlink = mainsoup.find("article", class_="thumbnail-preview")
            except:
                await ctx.send("No Result!")
            else:
                try:
                    linktobig = newlink.find("a")
                except:
                    await ctx.send("No Result!")
                else:
                    html = requests.get(linktobig["href"], cookies=cookies)
                    soup = BeautifulSoup(html.text, "html.parser")
                    try:
                        result = soup.find("img", class_="fit-width")
                    except:
                        await ctx.send("No Result!")
                    else:
                        await ctx.send(result["src"])
    @commands.command()
    async def hcomic(self, ctx, num: str):
        if len(num)==6 and num.isdigit():
            await ctx.send(f"https://nhentai.net/g/{num}")
        elif num=="rand" or num=="r" or num=="random":
            await ctx.send(f'https://nhentai.net/g/{random.randint(100000,400000)}')
        else:
            await ctx.send("I don't know what you are doing.\nUse ***>help*** command to see more information")
    @commands.command()
    async def vote(self,ctx):
        msgarr = ctx.message.content.split("/")
        msgcnt = len(msgarr)-1
        questionarr = msgarr[0].split(" ",1)
        question = questionarr[1]
        votestr = f"大家來投票啦!\n問題:{question}\n"
        if msgcnt == 0:
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("⭕")
            await votemsg.add_reaction("❌")
        if msgcnt == 10 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}\n:five:={msgarr[5]}\n:six:={msgarr[6]}\n:seven:={msgarr[7]}\n:eight:={msgarr[8]}\n:nine:={msgarr[9]}\n:keycap_ten:={msgarr[10]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
            await votemsg.add_reaction("5️⃣")
            await votemsg.add_reaction("6️⃣")
            await votemsg.add_reaction("7️⃣")
            await votemsg.add_reaction("8️⃣")
            await votemsg.add_reaction("9️⃣")
            await votemsg.add_reaction("🔟")
        if msgcnt == 9 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}\n:five:={msgarr[5]}\n:six:={msgarr[6]}\n:seven:={msgarr[7]}\n:eight:={msgarr[8]}\n:nine:={msgarr[9]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
            await votemsg.add_reaction("5️⃣")
            await votemsg.add_reaction("6️⃣")
            await votemsg.add_reaction("7️⃣")
            await votemsg.add_reaction("8️⃣")
            await votemsg.add_reaction("9️⃣")
        if msgcnt == 8 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}\n:five:={msgarr[5]}\n:six:={msgarr[6]}\n:seven:={msgarr[7]}\n:eight:={msgarr[8]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
            await votemsg.add_reaction("5️⃣")
            await votemsg.add_reaction("6️⃣")
            await votemsg.add_reaction("7️⃣")
            await votemsg.add_reaction("8️⃣")
        if msgcnt == 7 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}\n:five:={msgarr[5]}\n:six:={msgarr[6]}\n:seven:={msgarr[7]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
            await votemsg.add_reaction("5️⃣")
            await votemsg.add_reaction("6️⃣")
            await votemsg.add_reaction("7️⃣")
        if msgcnt == 6 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}\n:five:={msgarr[5]}\n:six:={msgarr[6]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
            await votemsg.add_reaction("5️⃣")
            await votemsg.add_reaction("6️⃣")
        if msgcnt == 5 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}\n:five:={msgarr[5]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
            await votemsg.add_reaction("5️⃣")
        if msgcnt == 4 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}\n:four:={msgarr[4]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
            await votemsg.add_reaction("4️⃣")
        if msgcnt == 3 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}\n:three:={msgarr[3]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
            await votemsg.add_reaction("3️⃣")
        if msgcnt == 2 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}\n:two:={msgarr[2]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await votemsg.add_reaction("2️⃣")
        if msgcnt == 1 :
            votestr = f"大家來投票啦!\n問題:{question}\n:one:={msgarr[1]}"
            votemsg = await ctx.send(votestr)
            await votemsg.add_reaction("1️⃣")
            await ctx.send("不可以獨裁:clown:")
    @commands.command()
    async def intodo(self,ctx):
        todomsg = ctx.message.content.split(" ", 1)
        datepattern = re.compile(r"\d{4}/\d{2}/\d{2}")
        if len(todomsg) == 1:
            await ctx.send("Please enter what you want to do.")
            return
        else:
            jobd = todomsg[1].split(":", 1)
            if len(jobd) == 1:
                await ctx.send("Please enter deadline.(yyyy/mm/dd)")
                return
            else:
                job = jobd[0]
                date = jobd[1]
                if not datepattern.match(date):
                    await ctx.send("Please enter correct pattern.(yyyy/mm/dd)")
                    return
                else:
                    if str(tododic.get(ctx.author.id))== "None":
                        todols = []
                        todols.append(f"{job} {date}")
                        tododic[ctx.author.id] = todols
                        print(tododic)
                    else:
                        tododic[ctx.author.id].append(f"{job} {date}")
                        print(tododic)
                    await ctx.send(f"{job} {date} write in.")
    @commands.command()
    async def todolist(self,ctx):
        await ctx.send("This is your todolist.")
        for i in tododic[ctx.author.id]:
            await ctx.send(i)



    #@client.event
#async def on_reaction_add(reaction, user)
def setup(bot):
    bot.add_cog(CmdsClass(bot))
