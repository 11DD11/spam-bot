import discord, asyncio
from discord.ext import commands

async def Ping(Pin):
    while True:
        try:
           chn = await Pin.fetch_channel(847829646065401876)
           guild = Pin.get_guild(847826510538473493)
           for member in guild.members:
              await chn.send(f"{member.mention}, @everyone")
        except: pass

intents = discord.Intents().all()

PingBot = commands.Bot(command_prefix='PingBot!', description = 'PingHub Official Bot!', case_insensitive=False, intents=intents)
PingBot2 = commands.Bot(command_prefix='PingBot!', description = 'PingHub Official Bot!', case_insensitive=False, intents=intents)
PingBot3 = commands.Bot(command_prefix='PingBot!', description = 'PingHub Official Bot!', case_insensitive=False, intents=intents)
PingBot4 = commands.Bot(command_prefix='PingBot!', description = 'PingHub Official Bot!', case_insensitive=False, intents=intents)
PingBot5 = commands.Bot(command_prefix='PingBot!', description = 'PingHub Official Bot!', case_insensitive=False, intents=intents)


@PingBot.event
async def on_ready():
    print("PingBot Bot Ready!")
    PingBot.loop.create_task(Ping(PingBot))

@PingBot2.event
async def on_ready():
    print("PingBot2 Bot Ready!")
    PingBot2.loop.create_task(Ping(PingBot2))

@PingBot3.event
async def on_ready():
    print("PingBot3 Bot Ready!")
    PingBot3.loop.create_task(Ping(PingBot3))

@PingBot4.event
async def on_ready():
    print("PingBot4 Bot Ready!")
    PingBot4.loop.create_task(Ping(PingBot4))

@PingBot5.event
async def on_ready():
    print("PingBot5 Bot Ready!")
    PingBot5.loop.create_task(Ping(PingBot5))

tokens = ["", "", "", "", ""]


loop = asyncio.get_event_loop()
loop.create_task(PingBot.start(tokens[0], bot=True, reconnect=True))
loop.create_task(PingBot2.start(tokens[1], bot=True, reconnect=True))
loop.create_task(PingBot3.start(tokens[2], bot=True, reconnect=True))
loop.create_task(PingBot4.start(tokens[3], bot=True, reconnect=True))
loop.create_task(PingBot5.start(tokens[4], bot=True, reconnect=True))
loop.run_forever()