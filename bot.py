import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from datetime import datetime, timedelta

from event import Event

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='event', help='Information on current events')
async def get_events(ctx):
    event = Event()
    event_names, event_links, event_times = event.get_events()
    messages = ["Danh sách các event đang diễn ra:"]
    for i in range(len(event_names)):
        messages.append(event_names[i] + " còn " + event_times[i])
        messages.append("https://genshin-impact.fandom.com" + event_links[i])
    response = "\n".join(messages)
    await ctx.send(response)

@bot.command(name='introduce', help='Paimon introduces herself')
async def introduce(ctx):
    response = "Mình là thức ăn dự trữ và bạn đồng hành tốt nhất của nhà lữ hành!"
    await ctx.send(response)

@bot.command(name='resin', help="!resin [CURRENT RESIN]: Paimon calculates when the resin will be full.")
async def calculate_resin(ctx, current_resin: int):
    if current_resin < 160:
        full_resin = (160 - current_resin) * 8
        full_time = datetime.now() + timedelta(minutes=full_resin)
        hour = full_time.hour
        minute = full_time.minute
        response = "Nhà lữ hành, trong vòng " + str(full_resin) + " phút nữa nhựa sẽ đầy nha. Vào " + str(hour) + "h" + str(minute) + "p đừng quên xả nhựa đó!"
        await ctx.send(response)
    else:
        response = "Xả nhựa thôi nào nhà lữ hành! Để đầy lâu sẽ gây lãng phí đó!"
        await ctx.send(response)

@bot.command(name='botngu', help='Mock the emergency food.')
async def bully(ctx):
    id = '<@' + str(ctx.message.author.id) + '>'
    print(id)
    response = "Thôi đi!" + id +" ngu thì có!"
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)