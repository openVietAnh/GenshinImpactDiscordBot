import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from datetime import datetime, timedelta

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='introduce')
async def introduce(ctx):
    response = "Mình là thức ăn dự trữ và bạn đồng hành tốt nhất của nhà lữ hành!"
    await ctx.send(response)

@bot.command(name='resin')
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

@bot.command(name='botngu')
async def calculate_resin(ctx):
    id = '<@' + str(ctx.message.author.id) + '>'
    print(id)
    response = "Thôi đi!" + id +" ngu thì có!"
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)