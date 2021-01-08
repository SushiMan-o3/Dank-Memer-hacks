import discord
import random
import asyncio
from discord.ext import commands

def colour():
    colours = [0x921cff, 0x00ff7f, 0xff9b38, 0xff0000, 0x0900ff]
    return random.choice(colours)  

class dank(commands.Cog, name='dank'):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        from config import logs
        logs = self.bot.get_channel(logs)
        await logs.send('pls settings DM Notifications true')
        await logs.send('pls settings tips false')

    @commands.group(invoke_without_command=True, aliases = ['start'])
    async def donk(self, ctx):
        await ctx.send('Please send me something that you want me to start.')

    @donk.command()
    async def all(self, ctx):
        ok = {'beg': 785998769728389181, 'fish': 785998867556466728, 'search': 785998935642472539 , 'pm': 785998791668924496, 'hunt': 787721063504019466}
        for i in ok.keys():
            x = self.bot.get_channel(ok[i])
            await x.send(f'╞donk {i}')

    @donk.command()
    async def fish(self, ctx):
        from config import logs, user_id
        await ctx.send('pls fish')
        while True:
            try:
                x = (await self.bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)).content.lower()
                if x == 'fish stop':
                    embed = discord.Embed(description = 'Fish Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                await ctx.send('pls fish')
                try:
                    value = (await self.bot.wait_for('message', timeout = 60.0, check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                    if value == "You don't have a fishing pole, you need to go buy one. You're not good enough to catch them with your hands.":
                        await ctx.send('pls buy fishingpole')
                        bruh = (await self.bot.wait_for('message', timeout = 5.0, check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                        if bruh.find("Far out, you don't have enough money in your wallet or your bank to buy that much!!"):
                            embed = discord.Embed(description = 'Fishing rod lost.', color=0xbb0000)
                            await logs.send('@everyone')
                            await logs.send(embed = embed)
                            break
                    else:
                        if value.find("lol you suck, you found nothing") or value.find("You cast out your line and brought back"):
                            pass
                        else:
                            if 'type' in value:
                                words = value.split('type')
                                words = words[2].replace('`', '')
                                async with ctx.typing():
                                    await asyncio.sleep(5)
                                await ctx.send(words)
                            else:
                                await ctx.send('type not found')
                except:
                    ...
    
    @donk.command()
    async def hunt(self, ctx):
        from config import logs, user_id
        await ctx.send('pls hunt')
        while True:
            try:
                x = (await self.bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)).content.lower()
                if x == 'hunt stop':
                    embed = discord.Embed(description = 'Hunt Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                await ctx.send('pls hunt')
                try:
                    value = (await self.bot.wait_for('message', timeout = 60.0, check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                    if value.find("You don't have a hunting rifle, you need to go buy one. You're not good enough to shoot animals with your bare hands."):
                        await ctx.send('pls buy rifle')
                        bruh = (await self.bot.wait_for('message', timeout = 5.0, check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                        if bruh.find("Far out, you don't have enough money in your wallet or your bank to buy that much!!"):
                            embed = discord.Embed(description = 'Rifle lost.', color=0xbb0000)
                            logs = self.bot.get_channel(logs)
                            await logs.send(embed = embed)
                            break
                        else:
                            ...
                    else:
                        if value.find("lmao you are terrible, you found nothing to hunt") or value.find("You went hunting in the woods and brought back a"):
                            pass
                        else:
                            if 'type' in value:
                                words = value.split('type')
                                words = words[2].replace('`', '')
                                async with ctx.typing():
                                    await asyncio.sleep(5)
                                await ctx.send(words)
                            else:
                                await ctx.send('type not found')
                except:
                    ...

    @donk.command()
    async def beg(self, ctx):
        from config import user_id
        await ctx.send('pls beg')
        while True:
            try:
                x = (await self.bot.wait_for('message', timeout=46.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)).content.lower()
                if x == 'begging stop':
                    embed = discord.Embed(description = 'Beggin Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                await ctx.send('pls beg')

    @donk.command()
    async def search(self, ctx):
        from config import user_id
        while True:
            try:
                x = (await self.bot.wait_for('message', timeout=30.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)).content.lower()
                if x == 'search stop':
                    embed = discord.Embed(description = 'Searching Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                await ctx.send('pls search')
                try:
                    word = (await self.bot.wait_for('message', check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                    notneeded, listss = word.split('chat.', 2)
                    listss = (listss.replace('`', '')).split(',')
                    await ctx.send(random.choice(listss))
                except asyncio.TimeoutError:
                    ...  
    
    @donk.command(aliases = ['postmeme'])
    async def pm(self, ctx):
        from config import user_id
        while True:
            try:
                x = await self.bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)
                if x.content.lower() == 'pm stop' or x.content.lower() == 'post meme stop':
                    embed = discord.Embed(description = 'Posting Memes Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                await ctx.send('pls pm')
                opt = list('frick')
                await asyncio.sleep(3)
                await ctx.send(random.choice(opt))

    @donk.group(invoke_without_command=True)
    async def reactions(self, ctx):
        await ctx.send('Please send me something that you want me to start.')
    
def setup(bot):
    bot.add_cog(dank(bot))