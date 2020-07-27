import discord
import json

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(TOKEN)
