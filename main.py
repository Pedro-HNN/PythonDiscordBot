import discord
from discord.ext import commands
import music
import color
import casino

prefix = "&&"
client = commands.Bot(command_prefix= prefix, help_command=None)

#setup cogs
cogs = [music,color,casino]
for i in range(len(cogs)):
	cogs[i].setup(client)

# help command
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

# shutdown bot command
@client.command()
@commands.is_owner()
async def shutdown(context):
	await context.send("Goodbye!")
	await context.bot.logout()

# pin message event
@client.event
async def on_raw_reaction_add(payload):
	message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
	if (payload.emoji.name == "📌"):
		await discord.Message.pin(message)

# unpin message event
@client.event
async def on_raw_reaction_remove(payload): #:pushpin: == 📌
	message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
	if(message.pinned):
		if(not "📌" in [ payload.emoji.name for reaction in  message.reactions]):
			await discord.Message.unpin(message)


# on ready terminal message event
@client.event
async def on_ready():
	print("Logged as {0.user}".format(client))

# run bot
if __name__ == '__main__':
	client.run('your token here')
