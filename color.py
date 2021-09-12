import discord
from discord.ext import commands
import re


class color(commands.Cog):
    def __init__(self, client):
        self.client = client

    # change color command
    @commands.command(pass_context=True,
                      aliases=['Color', 'SetColor', 'setColor', 'Colour', 'colour', 'setColour', 'Setcolour',
                               'SetColour'])
    async def color(self, context):
        color = context.message.content
        color = color.upper().split()[1]

        if (color.startswith("#")):
            color = color[1:]

        if (checkHex(f"#{color}")):  # if color is real = pass
            for role in context.author.roles:
                if (role.name.startswith("color")):  # check if person has a color already
                    await context.author.remove_roles(role)

            role = discord.utils.get(context.guild.roles, name=f"color{color}")

            if (role):  # check if color already exists
                await context.author.add_roles(role)
            else:
                colorRole = int(f"{color}", 16)  # converts hex to color
                newRole = await context.guild.create_role(name=f"color{color}",
                                                          color=discord.Color(colorRole))  # creates new role
                await context.author.add_roles(newRole)  # gives role to user

            await context.message.channel.send('**Done!**')
        else:
            await context.message.channel.send(
                'Please, use a real HEX code. You can see: <https://www.google.com/search?q=color+picker>!')

    # clear color command
    @commands.command(pass_context=True,
                      aliases=['Clear', 'ClearColor', 'clearcolor', 'Clearcolor', 'clearColor', 'ClearColour',
                               'clearcolour', 'Clearcolour', 'clearColour'])
    async def clear(self, context):
        for role in context.author.roles:
            if (role.name.startswith("color")):  # check if person has a color already
                await context.author.remove_roles(role)
        await context.message.channel.send('User color cleared!')

    # delete all color roles
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def deleteAllColor(self, context):
        for role in context.guild.roles:
            if (role.name.startswith("color")):
                await role.delete()
        await context.send("Done! All color roles are deleted!")


# check to see if the HEX code is real
def checkHex(hex):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)

    return match  # if True = it is a real HEX color

# setup cog
def setup(client):
    client.add_cog(color(client))

