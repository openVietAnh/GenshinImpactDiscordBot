import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from pytz import timezone

from datetime import datetime, timedelta

from event import Event
from artifact import Artifact
from domain import Domain

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

USERS_TIMEZONE = {
    481458382662795264: 'Asia/Ho_Chi_Minh'
}

bot = commands.Bot(command_prefix='!')

@bot.command(name='event', help='Information on current events')
async def get_events(ctx):
    # event = Event()
    # event_names, event_links, event_times = event.get_events()
    # messages = ["List of on-going events:"]
    # for i in range(len(event_names)):
    #     messages.append(event_names[i] + " còn " + event_times[i])
    #     messages.append("https://genshin-impact.fandom.com" + event_links[i])
    response = "The event command is under maintaince, sorry for the inconvenience, Traveler"
    await ctx.send(response)

@bot.command(name='introduce', help='Paimon introduces herself')
async def introduce(ctx):
    print(ctx.message.author)
    response = "I am The Traveler's Emergency Food and his best companion!"
    await ctx.send(response)

@bot.command(name='resin', help="!resin [CURRENT RESIN]: Paimon calculates when the resin will be full.")
async def calculate_resin(ctx, current_resin: int):
    if current_resin < 160:
        full_resin = (160 - current_resin) * 8
        full_time = datetime.now(timezone(USERS_TIMEZONE[ctx.message.author.id])) + timedelta(minutes=full_resin)
        display_time = "{:02d}".format(full_time.hour) + ":" + "{:02d}".format(full_time.minute)
        response = "Traveler, in " + str(full_resin) + " minutes your resin will be full. At " + display_time + " don't forget to spend them!"
        await ctx.send(response)
    else:
        response = "Let's spend your resin Traveler! It would be wasteful if you let them full for a long time!"
        await ctx.send(response)

@bot.command(name='ehe', help='What do you mean EHE?!?')
async def ehe(ctx):
    ehe_gif = "https://c.tenor.com/cZHoFqQEgwkAAAAM/paimon.gif"
    response = "EHE TE NANDAYO?!?"
    await ctx.send(response)
    await ctx.send(ehe_gif)

@bot.command(name='stupid', help='Mock the emergency food.')
async def bully(ctx):
    id = '<@' + str(ctx.message.author.id) + '>'
    gif = "https://c.tenor.com/vteeAE47mHgAAAAd/mihoyo-genshin.gif"
    response = "Stop!" + id +" is stupid!"
    await ctx.send(response)
    await ctx.send(gif)

@bot.command(name='artifact', help="Generate a random 5 stars artifact")
async def get_artifact(ctx, *args):
    if len(args) != 2:
        await ctx.send("Traveler, please provide artifact type (flower/plume/sands/goblet/circlet) and its level (0 - 20)")
        return
    type, level = args
    if type.lower() not in ["flower", "plume", "sands", "goblet", "circlet"] or int(level) not in range(0, 21):
        await ctx.send("Traveler, are you dumb? We don't have this kind of artifact?!")
        return
    artifact = Artifact(type, level)
    await ctx.send("\n".join(artifact.get_info()))

@bot.command(name='today', help='Check what domain resource you can farm today')
async def get_resource(ctx, type="all"):
    if type not in ["talent", "weapon", "all", "book"]:
        message = "Traveler, there is no kind of resource that called " + type + ", only 'talent'/'book', 'weapon' & 'all'!"
        await ctx.send(message)
    else:
        domain = Domain()
        messages = domain.get_output(type)
        await ctx.send('\n'.join(messages))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)