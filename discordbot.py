from discord.ext import commands
import os
import traceback

import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

WELCOME_MESSAGE = """
Welcome {0.mention} to {1.name}! 
Please wait here before someone give you a permission!
"""

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = WELCOME_MESSAGE.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = ''.format(member, guild)
        await guild.system_channel.send(to_send)

@bot.command()
async def roll(ctx):
    rnd = random.randrange(1, 100)
    await ctx.send(rnd)

bot.run(token)
