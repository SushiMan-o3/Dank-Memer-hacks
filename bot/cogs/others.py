import discord
import random
from discord.ext import commands
import math
import datetime
import json
import asyncio
now = datetime.datetime.now()

def colour():
    colours = [0x921cff, 0x00ff7f, 0xff9b38, 0xff0000, 0x0900ff]
    return random.choice(colours)  


class other(commands.Cog, name='other'):
    def __init__(self, bot):
        self.bot = bot
        
    """
    Helping
    """
    @commands.command(aliases = ['math' , 'calc'])
    async def bmath(self, ctx, * , operations=None):
        if operations is None:
            embed=discord.Embed(description='Send the math question you want me to solve!')
            await ctx.send(embed=embed)
        else:
            if '^' in operations:
                operation = operations.replace("^", "**")
            else:
                operation = operations
            answer = eval(operation)
            embed=discord.Embed(title="Math Calculation", description=f'{operations} = {answer}', color=colour())
            await ctx.send(embed=embed)

    @commands.command(aliases = ['sqrt' , 'square root'])
    async def math_sqrt(self, ctx, kwarg):
        if kwarg is None:
            embed=discord.Embed(description='Send the number you want me to square root!')
            await ctx.send(embed=embed)
        else:
            try:
                question = int(kwarg)
                answer = math.sqrt(question)
                embed=discord.Embed(title='Square Roots', description=f"√{question} = {answer}", color=colour())
                await ctx.send(embed=embed)
            except:
                await ctx.send("\>>> Something went wrong!")
    
    @commands.command(description = "Shows you're away")
    async def afk(self, ctx):
        try:
            nickname = ctx.author.display_name 
            await ctx.author.edit(nick=f'[AFK] {nickname}')
            await ctx.channel.send(f'{ctx.author} has gone AFK')
            await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            await ctx.author.edit(nick=nickname)
            await ctx.channel.send(f'{ctx.author.mention} has been removed from AFK.')
        except:
            embed=discord.Embed(description="\>>> You don't have the permission to change your nickname.", color=colour())
            await ctx.send(embed=embed)
    
    """
    Tags
    """

    @commands.group(invoke_without_command=True)
    async def tag(self, ctx, *, tag: str = None):
        tag = tag.lower()
        with open('cogs/tags.json') as f:
            tags = json.load(f)
        if tag is None:
            await ctx.message.delete(delay=10.0)
            message = await ctx.send('\>>> You need to pass a tag.')
            return await message.delete(delay=10.0)
        else:
            if tag not in tags.keys():
                await ctx.message.delete(delay=10.0)
                message = await ctx.send('\>>> Could not find a tag with that name.')
                return await message.delete(delay=10.0)
            else:
                await ctx.send(tags[tag])

    @tag.command()
    async def create(self, ctx, * , name: str = None):
        if name is None:
            await ctx.send("\>>> The title of the tag you're trying to create is missing.")
        else:
            with open('cogs/tags.json') as f:
                tags = json.load(f)
            if name.lower() in tags.keys():
                await ctx.send("\>>> There's a tag with that name!")
            else:
                await ctx.send("\>>> Send the description of the tag.")
                await asyncio.sleep(1)
                description = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                tags[name.lower()] = description.content
                with open('cogs/tags.json', 'w') as f:
                    json.dump(tags, f, indent = 4)
                await ctx.send(f"\>>> Done! Your tag has been created.")

    @tag.command()
    async def edit(self, ctx, *, tag: str = None):
        if tag is None:
            await ctx.send('\>>> Please specify the tag you want to edit.')
        else:
            with open('cogs/tags.json') as f:
                tags = json.load(f)
            if tag.lower() not in tags.keys():
                await ctx.send("\>>> The tag you're trying to edit isn't found.")
            else:
                await ctx.send('\>>> What is the new description of this tag?')
                description = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                tags[tag.lower()] = description.content
                with open('cogs/tags.json', 'w') as f:
                    json.dump(tags, f, indent = 4)
                await ctx.send("\>>> Tag edited! Your tag has been edited.")
    
    @tag.command()
    async def delete(self, ctx, *, tag: str = None):
        if tag is None:
            await ctx.send('\>>> Please specify the tag you want to delete.')
        else:
            with open('cogs/tags.json') as f:
                tags = json.load(f)
            tag = tag.lower()
            if tag not in tags:
                await ctx.send("\>>> The tag that you're trying to delete wasn't found")
            else:
                tags.pop(tag)
                await ctx.send("\>>> Tag deleted! Your tag has been deleted.")
                with open('cogs/tags.json', 'w') as f:
                    json.dump(tags, f, indent = 4)

    
    """
    fun
    """
        
    @commands.command()
    async def emoji(self, ctx, *, text: str = None):
        if text is None:
            await ctx.send("\>>> Please add the text you want me to convert to emojis.")
        else:
            text = text.lower()
            emojis = {'a':'🇦 ', 'b': '🇧 ', 'c': '🇨 ', 'd': '🇩 ', 'e': '🇪 ', 'f': '🇫 ', 'g': '🇬 ', 'h': '🇭 ', 'i': '🇮 ', 'j': '🇯 ', 'k': '🇰 ', 'l': '🇱 ', 'm': '🇲 ', 'n': '🇳 ', 'o': '🇴 ', 'p': '🇵 ', 'q': '🇶 ', 'r': '🇷 ', 's': '🇸 ', 't': '🇹 ', 'u':'🇺 ', 'v': '🇻 ', 'w': '🇼 ', 'x':'🇽 ', 'y': '🇾 ', 'z': '🇿 ', ' ': '  ', '!': '❗'}
            for i in emojis.keys():
                text = text.replace(i, emojis[i])
            await ctx.send(text)

    @commands.group(invoke_without_command=True)
    async def morse(self, ctx, *, text: str = None):
        if text is None:
            await ctx.send("\>>> Please add the text you want me to convert to morse.")
        else:
            from cogs.morse import MorseCodeTranslator
            translator = MorseCodeTranslator()
            await ctx.send(translator.translate_text(text))

    @morse.command(alias = 'en')
    async def english(self, ctx, *, text: str = None):
        if text is None:
            await ctx.send("\>>> Please add the morse text you want me to convert to english.")
        else:
            from cogs.morse import MorseCodeTranslator
            translator = MorseCodeTranslator()
            await ctx.send(translator.translate_morse(text))

    


def setup(bot):
    bot.add_cog(other(bot))
