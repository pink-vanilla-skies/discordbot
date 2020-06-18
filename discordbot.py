# id 721988431013478481
# token NzIxOTg4NDMxMDEzNDc4NDgx.XuciUg.RkqF_OdLfCsFgZr1bVJYcq6WW2k
# permission 2147483639
# https://discordapp.com/oauth2/authorize?client_id=721988431013478481&scope=bot&permissions=2147483639


import discord
import asyncio
import time


client = discord.Client()

@client.event
async def on_ready():
    print(f"You've logged in as {client.user}")



@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "hi" in message.content.lower():
        await message.channel.send("Hi there!")
    elif "sentdebot.community_report()" == message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in sentdex_guild.members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")
    elif "vera.logout" in message.content.lower():
        await client.close()
        sys.exit()




client.run("NzIxOTg4NDMxMDEzNDc4NDgx.XuciUg.RkqF_OdLfCsFgZr1bVJYcq6WW2k")
