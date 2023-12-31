# Import-ant Libraries
import discord
import time
from data import BotData as data
from dotenv import load_dotenv
import os

# Setup
boot_time = time.time()
bot = discord.Bot(intents = data.intents, owner_id = data.owner_id)

@bot.listen()
async def on_connect():

    await bot.change_presence(
        activity = discord.Game(data.activity),
        status = discord.Status.online)

    print(f'{bot.user.name} woke up in {time.time() - boot_time} seconds.')
    return


# Run
bot.load_extensions('cogs')
load_dotenv()
bot.run(os.environ.get("TOKEN"))
