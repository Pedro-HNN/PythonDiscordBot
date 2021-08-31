
import os
import discord
from discord.ext import commands
import random
from functions import *

prefix = "&&"
client = commands.Bot(command_prefix= prefix, help_command=None)

#help command
@client.command(pass_context=True, aliases=['Help'])
async def help(context):
	embed = discord.Embed(title="Commands:", description="",color=0xFF1515)

	embed.add_field(name=f"{prefix}help", value="Prints this message",inline=False)
	embed.add_field(name=f"{prefix}dice <number>", value=f"Rolls a die with the chosen number of sides (you can also use {prefix}roll <number>)",inline=False)
	embed.add_field(name="Pin any message you want", value="You can pin any messages just by reacting to the message with this emoji 📌", inline=False)
	embed.add_field(name="Unpin any message you want", value="You can unpin any messages by removing the 📌 emoji from reactions", inline=False)
	embed.add_field(name=f"{prefix}color <HEXcode>", value=f"You can change your color role anytime you want using 6 digit HEX codes. You can also use {prefix}setColor <HEXcode>. \nCheck out: <https://www.google.com/search?q=color+picker>", inline=False)
	embed.add_field(name=f"{prefix}clear", value=f"You can clear your color role. You can also use {prefix}clearcolor", inline=False)
	await context.message.channel.send(content="", embed=embed)
#help command

#change color command
@client.command(pass_context=True, aliases=['Color','SetColor','setColor','Colour','colour','setColour','Setcolour','SetColour'])
async def color(context):
	color = context.message.content
	color = color.upper().split()[1]

	if(color.startswith("#")):
		color = color[1:]

	if(checkHex(f"#{color}")):#if color is real = pass
		for role in context.author.roles:			
			if(role.name.startswith("color")):#check if person has a color already
				await context.author.remove_roles(role)

		role = discord.utils.get(context.guild.roles, name=f"color{color}")

		if(role):#check if color already exists
			await context.author.add_roles(role)
		else:
			colorRole = int(f"{color}", 16)#converts hex to color
			newRole = await context.guild.create_role(name=f"color{color}", color= discord.Color(colorRole))#creates new role
			await context.author.add_roles(newRole)#gives role to user
		
		await context.message.channel.send('**Done!**')
	else:
		await context.message.channel.send('Please, use a real HEX code. You can see: <https://www.google.com/search?q=color+picker>!')
#change color command

#clear color command
@client.command(pass_context=True, aliases=['Clear','ClearColor','clearcolor','Clearcolor','clearColor', 'ClearColour','clearcolour','Clearcolour','clearColour'])
async def clear(context):

	for role in context.author.roles:
		if(role.name.startswith("color")):#check if person has a color already
				await context.author.remove_roles(role)
	await context.message.channel.send('User color cleared!')
	
#clear color command

#dice command
@client.command(aliases=['roll','Roll','Dice'])
async def dice(context, *, num):
	try:
		num = int(num)
		x = num
		num = num+1
		num = random.randrange(1,num)
		await context.send(f"*:game_die: D{x} Rolled* ***{num}***")
	except:
		await context.send("Please, use a positive Integer. Example: 20,30,40")
#dice command

#pin message event
@client.event
async def on_raw_reaction_add(payload):
	message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
	if (payload.emoji.name == "📌"):
		await discord.Message.pin(message)
#pin message event

#unpin message event
@client.event
async def on_raw_reaction_remove(payload): #:pushpin: == 📌
	message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
	if(message.pinned):
		if(not "📌" in [ payload.emoji.name for reaction in  message.reactions]):
			await discord.Message.unpin(message)
#unpin message event

#shutdown bot
@client.command()
@commands.is_owner()
async def shutdown(color):
    await color.bot.logout()
#shutdown bot

#delete all color roles
@client.command()
@commands.is_owner()
async def deleteAllColor(context):
    for role in context.guild.roles:
    	if(role.name.startswith("color")):
    		await role.delete()
    await context.send("Done! All color roles are deleted!")
#delete all color roles

#on ready terminal message
@client.event
async def on_ready():
	print("Logged as {0.user}".format(client))
#on ready terminal message

#change it later
if __name__ == '__main__':
	client.run(your token here)
#change it later
