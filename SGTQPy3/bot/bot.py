import discord
import asyncio
import random
#import MapGen
from lib import cmddict
#from ..lib import threadpool
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
    @creg.regcmd('!newgame')
    async def creategame(cmdargs):
        isdm = False
        auth = message.author
        serv = auth.server
        sroles = serv.roles
        aroles = auth.roles
        sesschannel = None
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
                    if u not in serverunames: 
                        validusers = False
                if not validusers: 
                    await client.send_message(
                        message.channel, 
                        'At least one of those people is not a member of this server... Try again'
                        )
                    return
                await client.create_channel(serv, sessname) # create a text channel

                mentions = []
                for m in serv.members:
                    if m.name in players: mentions.append(m.mention)
                print(sesschannel)
                await client.send_message(
                    message.channel,
                    '{} game channel created, go play!'.format(sessname)
                    )
                # create the session and add the players to it.
                sess = gamesession.GameSession()
                for p in players:
                    sess.addplayer(player.Player(p))
                sessions[sessname] = sess
                await client.send_message(sesschannel, 'Well get to playing {}'.format(mentions))
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

    # handle the command string passed in
    if message.content.startswith('!'):
        await creg.callcmdasync(message.content)

def runbot(secret):
    client.run(secret)
