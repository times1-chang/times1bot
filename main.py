import discord
import asyncio
from discord.ext import commands
import os
import json
import random
from classes import Cog_Extension
from datetime import datetime, time, timedelta
import requests
from bs4 import BeautifulSoup


setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents = intents)

@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)
    
    erochannel = bot.get_channel(setdata['erochannel'])
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename != 'main.py' and filename != 'classes.py':
            bot.load_extension(filename[:-3])
    while True:
        now = datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        print(hour)
        if hour=="09" and minute =="00" :
            print("send!")
            mainhtml = requests.get("https://acg.lspimg.com")
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            newlink = mainsoup.find("a", class_="item-link")
            html = requests.get(newlink["href"])
            soup = BeautifulSoup(html.text, "html.parser")
            results = soup.find_all("img", class_="post-item-img", limit=5)
            image_links = list(result["src"] for result in results)
            for link in image_links:
                await erochannel.send(link)
        await asyncio.sleep(60)
bot.run(os.getenv('TOKEN'))
