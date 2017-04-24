import discord
import asyncio
import random
from lib import cmddict
from lib import threadpool
from game import dieroller

players = []
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    creg = cmddict.CmdDict()

    async def test(cmdargs):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    creg.regcmd('!test', test)

    async def sleep(cmdargs):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    creg.regcmd('!sleep', sleep)

    async def rolldie(cmdargs):
        num = 0
        tmp = None
        roller = dieroller.DieRoller()
        sides = 0
        try: 
            sides = int(cmdargs[0][1:])
        except ValueError:
            sides = 20
        num = roller.roll(sides)
        tmp = await client.send_message(message.channel, '`Rolling d{}`'.format(sides))
        await client.edit_message(tmp, '`You rolled a {}`'.format(num))
    creg.regcmd('!roll', rolldie)

    async def join(cmdargs):
        tmp = await client.send_message(message.channel, '`Thinking...`')
        print(message.author)
        if message.author in players:
            await client.edit_message(tmp, '`Found you, waking up character!`')
        else:
            players.append(message.author)
            await client.edit_message(tmp, '`Looks like you don\'t exist yet... let\'s create you!`')
            await client.send_message(message.channel, \
                """```Choose ye class, nerd !class:
                1: Wizardo
                2: Sneaky fuck
                3: Baldo
                4: GymRat
                5: Weeb```""")
    creg.regcmd('!join', join)

    async def getplayers(cmdargs):
        tmp = await client.send_message(message.channel, '`Hold on a sec...`')
        plyrs = ""
        for i in range(len(players)):
            plyrs = plyrs + str(players[i])
        await client.edit_message(tmp, '`{}`'.format(plyrs))
    creg.regcmd('!players', getplayers)

    # handle the command string passed in
    if message.content.startswith('!'):
        await creg.callcmdasync(message.content)

client.run('MzA1OTM2NjMwMzgyOTg1MjE3.C98edg.9bPTOe4-aB5Xk0PLeWtAhxCILFo')