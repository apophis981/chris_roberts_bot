import discord
import time
from markov_chain import markov

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@404085796883267594" in message.content:
        #msg = 'Hello {0.author.mention}'.format(message)
        new_message = markov.message
        time.sleep(5)
        await client.send_message(message.channel, new_message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

with open('../chris_token.txt', 'r') as myfile:
    token=myfile.read().replace('\n', '')
client.run(token)
