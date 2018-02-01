import discord
import time
import math
from markov_chain import markov

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # If someone tags the bot, or direct messages the bot: reply on same channel
    if(
    "@404085796883267594" in message.content or
    type(message.channel) == discord.channel.PrivateChannel):
        #Generate message from markov model of chris roberts text
        new_message = markov.text_model.make_short_sentence(240)
        #Time of simulated typing
        t = math.floor(len(new_message) / 12)
        print("sending message '", new_message, "' to:", message.channel, "wait", t)
        #Initial break before bot begins to imitate typing
        time.sleep(5)
        #Make it look like it is typing
        await client.send_typing(message.channel)
        #type for as long as the message is
        time.sleep(t)
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
