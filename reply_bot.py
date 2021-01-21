import discord
import asyncio
import aiohttp

# under auth proxy
proxy = aiohttp.ProxyConnector(proxy='http://USER:PASSWORD@SERVER:PORT')
#client = discord.Client( connector = proxy )
client = discord.Client( )

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
    if message.content.startswith("チャンネルリスト"):
        if client.user != message.author:
            m = client.text_channels
            await client.send_message(message.channel, m)

client.run("TOKEN")
