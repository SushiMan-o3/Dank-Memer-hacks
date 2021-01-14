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
        await ctx.send('\>>> Please send me something that you want me to start.')

    @donk.command()
    async def all(self, ctx):
        from config import prefix
        ok = {'beg': 785998769728389181, 'fish': 785998867556466728, 'search': 785998935642472539 , 'pm': 785998791668924496, 'hunt': 787721063504019466}
        for i in ok.keys():
            x = self.bot.get_channel(ok[i])
            await x.send(f'{prefix}donk {i}')

    @donk.command()
    async def fish(self, ctx):
        await ctx.send('\>>> Running Fish Command.')
        from config import logs, user_id
        logs = self.bot.get_channel(logs)
        while True:
            try:
                x = (await self.bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)).content.lower()
                if x == 'fish stop':
                    embed = discord.Embed(description = 'Fish Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                    await ctx.send('pls fish')
                    value = (await self.bot.wait_for('message', check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                    try:
                        if "Type" in value:
                            words = (value.split('`'))
                            async with ctx.channel.typing():
                                await asyncio.sleep(float(f"{random.randint(3, 7)}.{random.randint(0, 9)}"))
                                word = words[1].replace(u'\U0000feff', '')
                                await ctx.send(words[1])
                        else:
                            raise Exception("Fuck off dank memer")
                    except:
                        if 'lol you suck, you found nothing' in value or "You cast out your line and brought back" in value:
                            await ctx.send('Okay.')
                        else:
                            if "You don't have a fishing pole, you need to go buy one. You're not good enough to catch them with your hands." in value:
                                await ctx.send('pls buy fishingpole')
                                bruh = (await self.bot.wait_for('message', timeout = 5.0, check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                                if "Far out, you don't have enough money in your wallet or your bank to buy that much!!" in bruh:
                                    await ctx.send("\>>> Not enough for a fishing pole.")
                                    await logs.send('\>>> Not enough for a fishing pole')
                                    break
    
    @donk.command()
    async def hunt(self, ctx):
        await ctx.send('\>>> Running Hunt Command.')
        from config import logs, user_id
        logs = self.bot.get_channel(logs)
        while True:
            try:
                x = (await self.bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)).content.lower()
                if x == 'hunt stop':
                    embed = discord.Embed(description = 'Hunt Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                    await ctx.send('pls hunt')
                    value = (await self.bot.wait_for('message', check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                    try:
                        if "Type" in value:
                            words = (value.split('`'))
                            async with ctx.channel.typing():
                                await asyncio.sleep(float(f"{random.randint(3, 7)}.{random.randint(0, 9)}"))
                                word = words[1].replace(u'\U0000feff', '')
                                await ctx.send(word)

                        else:
                            raise Exception("Fuck off dank memer")
                    except:
                        if 'lmao you are terrible, you found nothing to hunt' in value or "You went hunting in the woods and brought back a" in value:
                            await ctx.send('Okay.')
                        else:
                            if "You don't have a hunting rifle, you need to go buy one. You're not good enough to shoot animals with your bare hands." in value:
                                await ctx.send('pls buy rifle')
                                bruh = (await self.bot.wait_for('message', timeout = 5.0, check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                                if "Far out, you don't have enough money in your wallet or your bank to buy that much!!" in bruh:
                                    await ctx.send("\>>> Not enough for a rifle.")
                                    await logs.send('\>>> Not enough for a rifle.')
                                    break

    @donk.command()
    async def beg(self, ctx):
        from config import user_id
        await ctx.send('\>>> Running Beg Command.')
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
        await ctx.send('\>>> Running Search Command.')
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
        await ctx.send('\>>> Running Postmeme Command.')
        while True:
            try:
                x = await self.bot.wait_for('message', timeout=60.0, check=lambda message: message.author.id == user_id and message.channel == ctx.channel)
                if x.content.lower() == 'pm stop' or x.content.lower() == 'post meme stop':
                    embed = discord.Embed(description = 'Posting Memes Stopped', color=0xbb0000)
                    await ctx.send(embed = embed)
                    break
            except asyncio.TimeoutError:
                await ctx.send('pls pm')
                word = (await self.bot.wait_for('message', check = lambda message: message.author.id == 270904126974590976 and message.channel == ctx.channel)).content
                if "oi you need to buy a laptop in the shop to post memes" in word:
                    break
                else:
                    opt = list('frick')
                    await asyncio.sleep(3)
                    await ctx.send(random.choice(opt))


def setup(bot):
    bot.add_cog(dank(bot))