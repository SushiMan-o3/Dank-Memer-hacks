import discord
import random

def colour():
    colours = [0x921cff, 0x00ff7f, 0xff9b38, 0xff0000, 0x0900ff]
    return random.choice(colours)  

class logging(commands.Cog, name='logging'):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(logging(bot))