#導入 Discord.py
import discord
import asyncio
from discord.ext import commands
#client 是我們與 Discord 連結的橋樑
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix= '>', intents = intents)
#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)
@bot.event
async def on_member_join(member):
    print(f'{member}join!')
    joinchannel = bot.get_channel(956529975375302666)
    await joinchannel.send(member.mention+' 歡迎加入!')
@bot.event
async def on_member_remove(member):
    print(f'{member}leave~')
    leavechannel = bot.get_channel(956938642641801287)
    leavemsg = await leavechannel.send(member.mention+' 含笑而去~~~\n讓我們祝他一路好走!')
@bot.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    if message.content==f"<@!{bot.user.id}>" or message.content==f"<@{bot.user.id}>":
        delmsg = await message.channel.send(message.author.mention+"tag尛")
        await asyncio.sleep(3)
        await delmsg.delete()
        await message.channel.send("對不起我不該這麼兇\n"+message.author.name+"找我有什麼事?")
    elif bot.user.mentioned_in(message):
        delmsg = await message.channel.send(message.author.mention+"tag尛")
        await asyncio.sleep(3)
        await delmsg.delete()
        await message.channel.send("對不起我不該這麼兇\n"+message.author.name+"你剛剛說什麼?")
    if 'ping' in message.content:
        await message.channel.send('pong')
    if "沒用" in message.content:
        await message.channel.send("屁啦!")
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])
    if "否" in message.content:
        await message.channel.send("明明就是")
    if "我超弱" in message.content:
        tmpmsg = await message.channel.send(str(message.author.name)+"不要瞎掰好嗎")
        await asyncio.sleep(3)
        await tmpmsg.delete()
#@client.event
#async def on_reaction_add(reaction, user):
#    if 
bot.run('OTU2NTM0NzAwNjU3MjIxNjU0.YjxoXA.BlDOvU0XQoRfAla9M_XJbQ5iXC4')
