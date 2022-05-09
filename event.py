import discord
import asyncio
from discord.ext import commands
import os
import json
import random
from classes import Cog_Extension
from datetime import datetime, time, timedelta

setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)

class EventClass(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member}join!')
        joinchannel = self.bot.get_channel(setdata['joinchannel'])
        await joinchannel.send(member.mention+' 歡迎加入!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member}leave~')
        leavechannel = self.bot.get_channel(setdata['leavechannel'])
        await leavechannel.send(member.mention+' 含笑而去~~~\n讓我們祝他一路好走!')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.author.id)
        if message.author == self.bot.user:
            return
        if message.author.id =="563290210813739010" :
            await message.channel.send("這是777")
            await asyncio.sleep(10)
        if message.author.id == "888749633466171413":
            await message.channel.send("這是旺仔")
            await asyncio.sleep(10)
        if message.content==f"<@!{self.bot.user.id}>" or message.content==f"<@{self.bot.user.id}>":
            delmsg = await message.channel.send(message.author.mention+"tag尛")
            await asyncio.sleep(3)
            await delmsg.delete()
            await message.channel.send("對不起我不該這麼兇\n"+message.author.name+"找我有什麼事?")
        elif self.bot.user.mentioned_in(message):
            delmsg = await message.channel.send(message.author.mention+"tag尛")
            await asyncio.sleep(3)
            await delmsg.delete()
            await message.channel.send("對不起我不該這麼兇\n"+message.author.name+"你剛剛說什麼?")
        if message.content == 'ping':
            await message.channel.send('pong')
        if "沒用" in message.content:
            await message.channel.send("屁啦!")
        if message.content.startswith('說'):
            #分割訊息成兩份
            tmp = message.content.split(" ",1)
            #如果分割後串列長度只有1
            if len(tmp) == 1:
                await message.channel.send("你要我說什麼啦？")
            else:
                await message.delete()
                await message.channel.send(tmp[1])
        if "否" in message.content:
            await message.channel.send("明明就是")
        if "我超弱" in message.content:
            tmpmsg = await message.channel.send(str(message.author.name)+"不要瞎掰好嗎")
            await asyncio.sleep(3)
            await tmpmsg.delete()
        #await self.bot.process_commands(message)



def setup(bot):
    bot.add_cog(EventClass(bot))

