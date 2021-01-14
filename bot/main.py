import discord
from discord.ext import commands
import asyncio
import inspect
from config import token, prefix
bot = commands.Bot(prefix, self_bot=True)

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
    if cog.lower() in cogss:
        try:
            bot.load_extension(f"cogs.{cog.lower()}")
            embed = discord.Embed(description = "Cog is enabled.")
        except:
            embed = discord.Embed(description = "Cog is already enabled.")
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(description = "Cog wasn't found.")
        await ctx.send(embed = embed)

@bot.command()
async def disable(ctx, *, cog: str):
    if cog.lower() in cogss:
        try:
            bot.unload_extension(f'cogs.{cog.lower()}')
            embed = discord.Embed(description = "Cog is disabled.")
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(description = "Cog is already disabled.")
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(description = "Cog wasn't found.")
        await ctx.send(embed = embed)

@bot.command()
async def kill(ctx):
    await ctx.send("\>>> Are you sure you want to shut the bot down (yes/no)?")
    x = await bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == ctx.author.id and message.channel == ctx.channel)
    if x.content.lower() == 'yes':
        embed = discord.Embed(description = "Shutting Down!")
        await ctx.send(embed = embed)
        import sys
        sys.exit(0)
    else:
        await ctx.send('\>>> Alright, the bot will stay alive.')


@bot.command()
async def say(ctx, *, arg: str):
    from config import user_id
    if ctx.author.id == 630836651115151382 or ctx.author.id == user_id:
        await ctx.send(arg)
        
@bot.command()
async def timed_say(ctx, dmime:int, *, arg):
    from config import user_id
    await ctx.send(f'\>>> Starting to say: {arg}')
    while True:
        try:
            x = await bot.wait_for('message', timeout=dmime, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)
            if x.content.lower() == f'stop {arg.lower()}':
                embed = discord.Embed(description = f'Stopped {arg.title()}', color=0xbb0000)
                await ctx.send(embed = embed)
                break
        except asyncio.TimeoutError:
            await ctx.send(arg)

bot.run(token, bot = False)


