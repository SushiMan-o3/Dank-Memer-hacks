import discord
from discord.ext import commands
import asyncio
import json
import random
import inspect
from config import token, prefix
import os

bot = commands.Bot(prefix, self_bot=True)

logs = bot.get_channel(785248219285553192)

@bot.event
async def on_ready():
    everything = f'Logged in as {bot.user.name}#{bot.user.discriminator}'
    print(f'{(len(everything) + 4) * "_"} \n\n| {everything} | \n{(len(everything) + 4) * "_"} ')
    

@bot.event
async def on_command_error(ctx, error):
    from config import logs
    error_logs = bot.get_channel(logs)
    await error_logs.send(f"```py\n{error}\n```")


cogss = [
    'dank',
    'information',
    'others'
]

for cog in cogss:
    bot.load_extension(f'cogs.{cog}')

@bot.command(name='eval', pass_context=True)
async def eval_(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await ctx.send(await res)
    else:
        await ctx.send(res)


@bot.command()
async def enable(ctx, *, cog: str):
    if cog.lower() in cogss.lower():
        bot.load_extension(cog)
        embed = discord.Embed(description = "Cog is enabled.")
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(description = "Cog wasn't found.")
        await ctx.send(embed = embed)

@bot.command()
async def disable(ctx, *, cog: str):
    if cog in cogss:
        bot.unload_extension(cog)
        embed = discord.Embed(description = "Cog is disabled.")
        await ctx.send(embed = embed)
        
    else:
        embed = discord.Embed(description = "Cog wasn't found.")
        await ctx.send(embed = embed)

@bot.command()
async def kill(ctx):
    embed = discord.Embed(description = "Shutting Down")
    await ctx.send(embed = embed)
    #import sys, sys.___()

@bot.command()
async def say(ctx, *, arg: str):
    await ctx.send(arg)
        
@bot.command()
async def timed_say(ctx, time:int, *, arg):
    while True:
        await asyncio.sleep(time)
        await ctx.send(arg)


bot.run(token, bot = False)


