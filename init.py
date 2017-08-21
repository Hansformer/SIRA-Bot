import discord
import asyncio

'''
Create a local configuration file (config.py) with the following:
username="String value"                                                   
password="String value"
token="String value"
debug=False
'''
from config import *

client = discord.Client()
chan = None

@client.event
@asyncio.coroutine
def on_ready():
	print(client.user.name)
	print(client.user.id)
	print('--------------')
	print('I live')


@client.event
@asyncio.coroutine
def on_message(message):
	chan = message.channel
	
	if message.channel.name != 'fleetcom' or 'human-resources' or 'ayy-lmao-info-hub':
		if message.content.startswith('*bombs u*'):
			yield from client.send_message(chan,'Space Ireland will be free! <:space_ireland:309204831548211201>')

		elif message.content.startswith('<@!319826689729232897>'):
			yield from client.send_message(chan,'You noticed me, senpai. <:anime_smug:319973746825756683>')

	if message.content.startswith('!botkill'):
		if message.author.id == '189890760873738240':
			chan = client.get_channel('348971376750886912')
			yield from client.send_message(chan,'sira-bot signing off o777')
			yield from client.close()

	if message.content.find('<:space_ireland:309204831548211201>') != -1:
		yield from client.add_reaction(message, ':space_ireland:309204831548211201')
		
	x = message.content.lower()
	if x.find('space ireland') != -1:
		yield from client.add_reaction(message, ':space_ireland:309204831548211201')
	if x.find('s p a c e i r e l a n d') != -1:
		yield from client.add_reaction(message, ':space_ireland:309204831548211201')

	if debug:
		print("New message (%s) - %s: %s" % (message.channel, message.author, message.content))

client.login(username, password)
client.run(token)


