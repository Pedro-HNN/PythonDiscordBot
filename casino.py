import discord
from discord.ext import commands
import random


class casino(commands.Cog):
    def __init__(self, client):
        self.client = client

    # dice command
    @commands.command(aliases=['roll', 'Roll', 'Dice'])
    async def dice(self, context, *,num=None):
        if num == None:
            num = 0
        try:
            num = int(num)
            x = num
            num = num + 1
            num = random.randrange(1, num)
            await context.send(f"*:game_die: D{x} Rolled* ***{num}***")
        except:
            await context.send("Please, use a positive Integer. Example: 20,30,40")

# setup cog
def setup(client):
    client.add_cog(casino(client))
