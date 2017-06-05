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

@client.event
@asyncio.coroutine
def on_ready():
    print(client.user.name)
    print(client.user.id)
    print(client.servers)


@client.event
@asyncio.coroutine
def on_message(message):
    channel = message.channel
    if message.content.startswith('*bombs u*'):
        yield from client.send_message(message.channel,
                                            'Space IRA will be free!')
    if message.content.contains('<@319826689729232897>'):
        yield from client.send_message(message.channel,
                                        'You mentioned me')
    if debug:
        print("New message in: %s: %s" % (message.channel, message.content))
        print(channel)
        yield from client.send_message(channel, 'fucking kill me already')

client.login(username, password)
client.run(token)
