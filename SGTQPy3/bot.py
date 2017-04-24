import discord
import asyncio
import random

players = ["boolean", "NickBigDong", "Ibitsu", "RobDanHill"]
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!help'):
        hlp = "`this will eventually print a help message`"
        await client.send_message(message.channel, hlp)

    elif message.content.startswith('!roll'):
        num = 0
        tmp = None
        if ' d20' in message.content:
            num = random.randrange(1, 20)
            tmp = await client.send_message(message.channel, '`Rolling d20...`')            
            await client.edit_message(tmp, '`You rolled a {}`'.format(num))
        elif ' d2' in message.content:
            num = random.randrange(1, 2)
            tmp = await client.send_message(message.channel, '`Rolling d2...`')            
            await client.edit_message(tmp, '`You rolled a {}`'.format(num))
        elif ' d6' in message.content:
            num = random.randrange(1, 6)
            tmp = await client.send_message(message.channel, '`Rolling d6...`')            
            await client.edit_message(tmp, '`You rolled a {}`'.format(num))
        elif ' d10' in message.content:
            num = random.randrange(1, 10)
            tmp = await client.send_message(message.channel, '`Rolling d10...`')            
            await client.edit_message(tmp, '`You rolled a {}`'.format(num))

    elif message.content.startswith('!join'):
        tmp = await client.send_message(message.channel, '`Thinking...`')
        if message.author in players:
            await client.edit_message(tmp, '`Found you, waking up character!`')
        else:
            await client.edit_message(tmp, '`Looks like you don\'t exist yet... let\'s create you!`')
            await client.send_message(message.channel, \
                """```Choose ye class, nerd !class:
                1: Wizardo
                2: Sneaky fuck
                3: Baldo
                4: GymRat
                5: Weeb```""")

client.run('MzA1OTM2NjMwMzgyOTg1MjE3.C98edg.9bPTOe4-aB5Xk0PLeWtAhxCILFo')