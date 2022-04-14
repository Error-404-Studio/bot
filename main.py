from discord import Intents, Game
from discord.ext.commands import *
from os import *
from dotenv import *

bot = Bot(
    command_prefix="!",
    intents=Intents(guilds=True, members=True, messages=True, message_content=True),
    activity=Game(name="!help")
)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"{bot.user} is online.")

for file in listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

load_dotenv()

bot.run(getenv("TOKEN"))
