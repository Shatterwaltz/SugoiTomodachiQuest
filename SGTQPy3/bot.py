import discord
import asyncio
import random

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
        hlp = """```
                 !stats - show your stats
                 !survey - survey the current area
                 !inv - show inventory
                    |--> this should have sub commands
                 !use <item/thing> - use an item or environment item
                 !move <cardinal dir> - move your player
                 !equip <item> - equip an item
                 !throw - throw item in hand (make sure to equip thing you want to throw first
                 !speak <item> - speak to something, can talk to innanimate things too, just might look silly
                 !roll <die type> - roll a die, not used in game,
                     but can be used by players to determine who should get to do something.
                  ```"""
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

client.run('MzA1OTM2NjMwMzgyOTg1MjE3.C98edg.9bPTOe4-aB5Xk0PLeWtAhxCILFo')