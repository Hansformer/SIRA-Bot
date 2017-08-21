# required libs
import discord
import asyncio

# discord api config
'''
Create a local configuration file (config.py) with the following:
username = "String value"                                                   
password = "String value"
token = "String value"
debug = False
'''
from config import *

# var defs
client = discord.Client()
chan = None

# login routine
@client.event
@asyncio.coroutine
def on_ready():
	# print some console info
	print('Initializing SIRA Bot...')
	print('--------------')
	print(client.user.name)
	print(client.user.id)
	print('--------------')
	print('It lives.')
	# set channel and send a message
	chan = client.get_channel('348971376750886912')
	yield from client.send_message(chan,'SIRA Bot reporting for duty. o777')

# on message routine
@client.event
@asyncio.coroutine
def on_message(message):
	chan = message.channel

	# react to being mentioned
	if message.content.find('<@!319826689729232897>') != -1:
		yield from client.send_message(chan,'You noticed me, senpai. <:anime_smug:319973746825756683>')

	# sira-bot is patriotic
	if message.content.find('*bombs u*') != -1:
		yield from client.send_message(chan,'Space Ireland will be free! <:space_ireland:309204831548211201>')

	# kill the bot from discord
	if message.content.startswith('!botkill'):
		# make sure only Nitrous Oxide#1222 can do it ;)
		if message.author.id == '189890760873738240':
			# set the channel, send a message and kill the script
			chan = client.get_channel('348971376750886912')
			yield from client.send_message(chan,'SIRA Bot signing off. o777')
			yield from client.close()

	# if debug is enabled print a message log in the console
	if debug:
		print("New Message (%s) - %s: %s" % (message.channel, message.author, message.content))

	# adding space_ireland reactions
	x = message.content.lower()
	if (message.content.find('<:space_ireland:309204831548211201>') != -1 or 
		x.find('space ireland') != -1 or 
		x.find('s p a c e i r e l a n d') != -1):
		yield from client.add_reaction(message, ':space_ireland:309204831548211201')

# running the bot
client.login(username, password)
client.run(token)