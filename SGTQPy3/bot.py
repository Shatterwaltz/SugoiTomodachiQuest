import discord
import asyncio

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
        hlp = """!stats - show your stats
                 !survey - survey the current area
                 !inv - show inventory
                    |--> this should have sub commands
                 !use <item/thing> - use an item or environment item
                 !move <cardinal dir> - move your player
                 !equip <item> - equip an item
                 !throw - throw item in hand (make sure to equip thing you want to throw first
                 !speak <item> - speak to something, can talk to innanimate things too, just might look silly
                 !roll <die type> - roll a die, not used in game,
                     but can be used by players to determine who should get to do something."""
        await client.send_message(message.channel, hlp)

client.run('MzA1OTM2NjMwMzgyOTg1MjE3.C98edg.9bPTOe4-aB5Xk0PLeWtAhxCILFo')