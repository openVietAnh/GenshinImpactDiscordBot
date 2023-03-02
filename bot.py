import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from pytz import timezone, all_timezones

from datetime import datetime, timedelta

from artifact import Artifact
from domain import Domain

from bs4 import BeautifulSoup
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

USERS_TIMEZONE = {
    # 481458382662795264: 'Asia/Ho_Chi_Minh',
}

activity = discord.Game(name="Genshin Impact")
bot = commands.Bot(command_prefix='!', activity=activity, status=discord.Status.online,  intents=discord.Intents.all())

@bot.command(name='event', help='Information on current events')
async def get_events(ctx):
    url = "https://genshin-impact.fandom.com/wiki/Events"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    tables = soup.find_all('table')
    cells = tables[1].findChildren('td')
    times, event = cells[1::3], cells[0::3]
    result = ["Dear Travelver, here is the list of on-going events:"]
    for i in range(len(times)):
        result.append(event[i].text + " ends on " + " ".join(times[i].text.split(" ")[-3:-1]))
    response = "\n".join(result)
    await ctx.send(response)

@bot.command(name='introduce', help='Paimon introduces herself')
async def introduce(ctx):
    response = "I am The Traveler's Emergency Food and his best companion!"
    await ctx.send(response)

@bot.command(name='settime', help='Set your timezone to calculate resin full time')
async def calculate_resin(ctx, current_hour: int):
    if current_hour < 0 or current_hour > 23:
        response = "Traveler, your current hour must between 0AM and 23PM!"
        await ctx.send(response)
    else:
        result = []
        for zone in all_timezones:
            if datetime.now(timezone(zone)).hour == current_hour:
                result.append(zone)
        USERS_TIMEZONE[ctx.message.author.id] = result[0]
        response = "Traveler, your timezone has been set among these:\n"
        response += ", ".join(result) + "\n"
        response += "Please run the `!resin` command to check"
        await ctx.send(response)

async def introduce(ctx):
    response = "I am The Traveler's Emergency Food and his best companion!"
    await ctx.send(response)

@bot.command(name='resin', help="!resin [CURRENT RESIN]: Paimon calculates when the resin will be full.")
async def calculate_resin(ctx, current_resin: int):
    if current_resin < 160:
        try:
            full_resin = (160 - current_resin) * 8
            full_time = datetime.now(timezone(USERS_TIMEZONE[ctx.message.author.id])) + timedelta(minutes=full_resin)
            display_time = "{:02d}".format(full_time.hour) + ":" + "{:02d}".format(full_time.minute)
            response = "Traveler, in " + str(full_resin) + " minutes your resin will be full. At " + display_time + " don't forget to spend them!"
        except KeyError:
            response = "Traveler, your timezone is not set, I don't know which time resin will be full in your local timezone.\n"
            response += "In " + str(full_resin) + " minutes your resin will be full.\n"
            response += "Use the *!settime* command to set your timezone. Usage: `!settime [current hour in 24 hours format]`. Example: `!settime 13`"
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