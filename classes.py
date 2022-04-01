import discord
import asyncio
from discord.ext import commands
import os
import json
import random
setdata = ''
with open('setting.json','r', encoding="utf8") as setfile :
    setdata = json.load(setfile)
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

