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
    if message.channel.name == 'sira-bot-playground':
        chan = message.channel
        if message.content.startswith('*bombs u*'):
            yield from client.send_message(chan,
                                           'Space IRA will be free!')
        if message.content.startswith('<@319826689729232897>'):
            yield from client.send_message(chan,
                                           'You mentioned me')
    if debug:
        print("New message in: %s: %s" % (message.channel.name, message.content))

client.login(username, password)
client.run(token)
