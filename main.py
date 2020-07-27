import discord
import json
import scrollphathd as sphd
import time

bot = discord.Client()

with open("config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["token"]


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    #List servers the bot is connected to
    print('Servers:')
    for guild in bot.guilds:
        print(guild.name)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        member = message.author.name
        messageContent = message.content
        str = member + ": " + messageContent
        sphd.write_string(str)
        for i in str:
            sphd.show()
            sphd.scroll(1)
            time.sleep(0.05)

bot.run(TOKEN)
