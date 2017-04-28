import discord
import asyncio
import random
import MapGen
from lib import cmddict
from lib import threadpool
from game import dieroller
from game import gamesession
from game import character
from game import player

sessions = {}
gsess = gamesession.GameSession()
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

    '''
    Here is where we handle setup of a game session.
    We first check to see if the user requesting the session is a DM.
    If the are then we parse the rest of the command and generate a session 
    object and spawn a sessions channel. If the bot goes down sessions can be
    persisted by serializing game sessions.
    '''
    async def creategame(cmdargs):
        isdm = False
        auth = message.author
        serv = auth.server
        sroles = serv.roles
        aroles = auth.roles
        sess = None
        dmrole = None
        for r in aroles: 
            if r.name == 'DM': isdm = True; dmrole = r
        if isdm:
            # we can parse the rest of the command and create a session etc.
            sessname = cmdargs[0]
            players = cmdargs[1:]
            # http://discordpy.readthedocs.io/en/latest/api.html?highlight=member#discord.Client.wait_for_message
            # create a channel
            await client.send_message(
                message.channel, 
                'One super duper game session coming right up!'
                )
            try:
                # should check to make sure that user names given are 
                # actual users on the server.
                validusers = True
                serverunames = [m.name for m in serv.members]
                print(serverunames)
                for u in players:
                    if u not in serverunames: validusers = False
                if not validusers: 
                    await client.send_message(
                        message.channel, 
                        'At least one of those people is not a member of this server... Try again'
                        )
                    return
                await client.create_channel(serv, sessname) # create a text channel
                await client.send_message(
                    message.channel,
                    '{} game channel created, go play!'.format(sessname)
                    )
                # create the session and add the players to it.
                sess = gamesession.GameSession()
                for p in players:
                    sess.addplayer(player.Player(p))
                sessions[sessname] = sess
                await client.send_message(sessname, 'Well get to playing {}'.format(players))
            except discord.Forbidden:
                await client.send_message(
                    message.channel,
                    'I don\'t have permission to do that!'
                    )
        else:
            for r in sroles: 
                if r.name == 'DM': mentionstr = r.mention
            await client.send_message(
                message.channel, 
                'You can\'t do that! Only the DM can do that.'
                )
            await client.send_message(message.channel, 
                '{} create a game for this dork.'.format(mentionstr)
                )
    creg.regcmd('!newgame', creategame)

    async def test(cmdargs):
        counter = 0
        tmp = await client.send_message(
            message.channel, 
            'Calculating messages...'
            )
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
        print(cmdargs)
        if 'd(' in cmdargs[0] and ')' in cmdargs[-1]:
            print(' '.join(cmdargs))
            expr = ' '.join(cmdargs)[2:-1]
            print(expr)
            sides = roller.reversepolish(expr)
        else:
            try: 
                sides = int(cmdargs[0][1:])
            except ValueError:
                sides = 20
        num = roller.roll(sides)
        tmp = await client.send_message(message.channel, '`Rolling d{}`'.format(sides))
        await client.edit_message(tmp, '`You rolled a {}`'.format(num))
    creg.regcmd('!roll', rolldie)

    # async def join(cmdargs):
    #     tmp = await client.send_message(message.channel, 'Thinking...')
    #     print(message.author)
    #     if message.author in gsess.players:
    #         await client.edit_message(tmp, 'Found you, waking up character!')
    #     elif message.author not in gsess.players or cmdargs[0] == 'classes':
    #         await client.edit_message(tmp, '`Looks like you don\'t exist yet... let\'s create you!`')
    #         await client.send_message(message.channel, \
    #             'Here are the classes you may start with, nerd:\n\n' \
    #             + '1. Sneaky Fuk\n'\
    #             + '2. Stronk Bro\n'\
    #             + '3. Gigantic Braino\n'\
    #             + '4. Weeabo NEET\n'\
    #             + '5. Rom Com Anime Side Character\n'\
    #             + 'send `!join new <class num here>` to start creating a character!\n')
    #     # handle character creation.
    #     print(cmdargs)
    #     if len(cmdargs) != 0 and cmdargs[0] == 'new':
    #         try:
    #             classnum = int(cmdargs[1])
    #         except ValueError:
    #             await client.send_message(message.channel, 'That isn\'t a class you donkass!')
    #             return
    #         await client.send_message(message.channel, 'You chose class {}'.format(classnum))
    #         gsess.players[message.author] = player.Player(message.author) 
    #         gsess.players[message.author].pcharacter = character.Character(
    #             'desc here', 
    #             str(classnum),
    #             message.author
    #             )
    #         char = gsess.players[message.author]
    #         await client.send_message(message.channel, 
    #             'your character is:\n' \
    #             + char.name + '\n' \
    #             + char.desc + '\n' \
    #             + char.did + '\n'
    #             )
    # creg.regcmd('!join', join)

    # async def getplayers(cmdargs):
    #     tmp = await client.send_message(message.channel, '`Hold on a sec...`')
    #     plyrs = ""
    #     for i in range(len(players)):
    #         plyrs = plyrs + str(players[i])
    #     await client.edit_message(tmp, '`{}`\n'.format(plyrs))
    # creg.regcmd('!players', getplayers)

    # handle the command string passed in
    if message.content.startswith('!'):
        await creg.callcmdasync(message.content)

client.run('MzA1OTM2NjMwMzgyOTg1MjE3.C98edg.9bPTOe4-aB5Xk0PLeWtAhxCILFo')
