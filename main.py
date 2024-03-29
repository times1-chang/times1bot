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
import urllib3
from github import Github


g = Github(os.getenv('GTOKEN'))
repo = g.get_repo('times1-chang/times1bot')


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents = intents, help_command = None)

@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)
    erochannel116 = bot.get_channel(setdata['erochannel116'])
    erochannel208 = bot.get_channel(setdata['erochannel208'])
    dutychannel = bot.get_channel(setdata['dutychannel'])
    testchannel = bot.get_channel(setdata['testchannel'])
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename != 'main.py' and filename != 'classes.py':
            bot.load_extension(filename[:-3])    
    while True:
        now = datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        print(hour)
        if hour=="12" and minute =="00" :
            arch = random.randint(1,4335)
            print("send!")
            mainhtml = requests.get(f"https://acg.lspimg.com/archives/{arch}.html")
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            results = mainsoup.find_all("a", class_="media-content", limit=10)
            image_links = list(result["href"] for result in results)
            for link in image_links:
                await erochannel116.send(link)
                await erochannel208.send(link)
                
        #if hour=="22" and minute =="00":
        while True:
            #dstfile = open('dutystudent.json', 'r+',encoding="utf8")
            dstjf = open('dutystudent.json', 'r+',encoding="utf8")
            dstfile = repo.get_contents("dutystudent.json", ref="test")
            dstdata = json.load(dstjf)
            worker = int(dstdata['dutystudent'])
            daynumber = int(dstdata['daynumber'])
            if daynumber >= 6:
                break
            await testchannel.send(f"今日值日生: {worker}、{worker+1}")
            worker +=2
            if worker >= 34:
                worker=1
            daynumber +=1
            if daynumber ==7:
                daynumber = 1
            newdstdata = json.dumps({"dutystudent" : f"{worker}", "daynumber" : f"{daynumber}"})
            
            #newdstdata = {"dutystudent" : f"{worker}"}
            repo.update_file(dstfile.path,"test",f"{newdstdata}", dstfile.sha, branch="test")
            dstjf.seek(0)
            dstjf.write(newdstdata)
            dstjf.close()
            print("working...")
        await asyncio.sleep(60)
bot.run(os.getenv('TOKEN'))

'''
        
        now = datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        print(hour)
        if hour=="11" and minute =="00" :
            print("send!")
            mainhtml = requests.get("https://gelbooru.com/index.php?page=post&s=list&tags=all")
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            newlink = list(mainsoup.find_all("article", class_="thumbnail-preview", limit = 10))
            for i in newlink:
                linktobig = i.find("a")
                html = requests.get(linktobig["href"])
                soup = BeautifulSoup(html.text, "html.parser")
                result = soup.find("img", class_="fit-width")
                await erochannel.send(result["src"])

    erochannel116 = bot.get_channel(setdata['erochannel116'])
    erochannel208 = bot.get_channel(setdata['erochannel208'])
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename != 'main.py' and filename != 'classes.py':
            bot.load_extension(filename[:-3])    
    while True:
        now = datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        print(hour)
        if hour=="11" and minute =="00" :
            print("send!")
            mainhtml = requests.get("https://acg.lspimg.com")
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            newlink = mainsoup.find("a", class_="item-link")
            html = requests.get(newlink["href"])
            soup = BeautifulSoup(html.text, "html.parser")
            results = soup.find_all("img", class_="post-item-img", limit=10)
            image_links = list(result["src"] for result in results)
            for link in image_links:
                await erochannel116.send(link)
                await erochannel208.send(link)
        await asyncio.sleep(60)

        now = datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        print(hour)
        if hour=="11" and minute =="00" :
            arch = random.randint(5,766)
            print("send!")
            mainhtml = requests.get(f"https://acg.lspimg.com/archives/{arch}/")
            mainsoup = BeautifulSoup(mainhtml.text, "html.parser")
            results = mainsoup.find_all("img", class_="post-item-img", limit=10)
            image_links = list(result["src"] for result in results)
            for link in image_links:
                await erochannel.send(link)

'''
