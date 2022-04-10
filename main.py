import diskord
from diskord.ext import commands
import os
from itertools import cycle
from asyncio import sleep
from dotenv import load_dotenv
import sys

client = commands.Bot(
    command_prefix="!",
    intents=diskord.Intents(guilds=True, messages=True),
    case_insensitive=True,
    help_command=None
)

async def change_status():
    statuses = cycle(
        [
            "!help",
            "!devs | Check our developers!",
            '!github | Check our organization!',
        ]
    )

    while not client.is_closed():
        await client.change_presence(activity=diskord.Game(name=next(statuses)))
        await sleep(10)

@client.event
async def on_ready():
    print(f"{client.user} is online")
    client.loop.create_task(change_status())

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        try:
            client.load_extension(f"cogs.{file[:-3]}")
        except Exception as e:
            print("Error loading " + file)
            print(e, file=sys.stderr)

load_dotenv()

client.run(os.getenv("TOKEN"))
