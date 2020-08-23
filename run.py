from typing import List, Any, Dict

import discord
from discord.ext import commands
import datetime

app = commands.Bot(command_prefix='/')
app.remove_command("help")

tokn = 'NzA0OTc4MDI2MTA2MDYwODIy.XqlA2w.vTJy-y_mRWpOEGrKRKkfwRN7M4I'

@app.event
async def on_ready():
    print("==========")

@app.event
async def on_member_join(member):
    channel = app.get_channel(id=704978414188232815) # id= 후에 채널 아이디을 넣으면 거기로 가짐
    await channel.send("<@{}>님 SW project서버에 오신것을 환영합니다!\n자동으로 유저권한이 지급되었습니다!".format(member.id))
    author = member.guild.get_member(int(member.id))
    role = discord.utils.get(member.guild.roles, name="USER")
    await author.add_roles(role)

@app.event
async def on_member_remove(member):
    channel = app.get_channel(id=704978414188232815) # id= 후에 채널 아이디을 넣으면 거기로 가짐
    await channel.send("{}님이 나가셨어요.. 다음에 다시봐요!".format(member))

app.run(tokn)
