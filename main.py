#!/usr/bin/python3

# Import-ant Libraries
import discord
import time
import data

boot_time = time.time()

# Setup
bot = discord.Bot(intents = data.intents, owner_id = data.owner_id)

@bot.listen()
async def on_connect():

    await bot.change_presence(
        activity = discord.Game(data.activity),
        status = discord.Status.online)

    print(f'{bot.user.name} woke up in {time.time() - boot_time} seconds.')
    return

bot.load_extensions('cogs')
bot.run(data.token)
