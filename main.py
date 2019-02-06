from keep_alive import keep_alive
import discord
from discord.ext.commands import Bot
import os
import re
import unidecode
import json
activate = True

client = discord.Client()
prefix = ("a!")
client = Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("Online")
    print(client.user)

@client.command()
async def on():
  global activate
  activate = True
  await client.say("```The bot is now on```")

@client.command()
async def off():
  global activate
  activate = False
  await client.say("```The bot is now off```")
  
@client.command()
async def no():
  await client.say("**NO ANIME!**")


@client.event
async def on_message(message):
    discordmessage = str(message.content).replace(" ", "")
    discordmessage = unidecode.unidecode(discordmessage)
    discordmessage = re.sub(r'[.|?|/|\||(|)|+|<|>|,|;|:|{|}|*|-|=|#|^|&|~|!|`|_]', r'', discordmessage)
    global activate

    if (activate == True): 
      if (discordmessage.lower()).find('anime') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('loli') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('naruto') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!') 
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('sakura') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('hentai') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('baka') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('harem') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!') 
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('nani') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('otaku') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('tsundere') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('yaoi') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!') 
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('yuri') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('chibi') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('ecchi') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('sasuke') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('kakashi') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('sharingan') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!') 
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('<:sasuke:529529014541352961>') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('<:kakashi:529532755655131147>') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('<:sharingan:529528775923204097>') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('animu') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')     

      elif (discordmessage.lower()).find('japaneseanimation') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')  

      elif (discordmessage.lower()).find('japanesecartoon') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png')  

      elif (discordmessage.lower()).find('uwu') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png') 

      elif (discordmessage.lower()).find('owo') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME!')
        await client.send_file(message.channel, 'No Anime Violation.png') 

      elif (discordmessage.lower()).find('onepiece') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' NO ANIME! also ur anime is trash')
        await client.send_file(message.channel, 'No Anime Violation.png') 
      
      elif (discordmessage.lower()).find('jojo') > -1 and message.author != client.user:
        await client.send_message(message.channel, message.author.mention +' ZA WAURDO https://www.youtube.com/watch?v=7ePWNmLP0Z0')

    await client.process_commands(message)
       

keep_alive()
client.run(Token)
