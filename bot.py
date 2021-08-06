import discord
from discord.ext import commands
import requests
import json
from requests.api import get
import random
client=discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')   
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    data = json.loads(response.text)
    author = data[0]['a']
    return(quote,author)

f= "abc"
p="ok"

@client.event
async def on_ready():
    print("Bot is online as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.content == "!quote":
        quote,author = get_quote()
        
        embedVar = discord.Embed(title="QUOTE", color=random.randint(0, 0xffffff))
        embedVar.add_field(name=(quote), value= (author) , inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith("!tag"):
        d=message.content
        n=d.find(" ",5,50)
        if d[5:n].startswith("<"):
            if d[-1] !=">":
                g=d[n+1:]
                g=int(g)  
                if g>250:
                    await message.channel.send("huge no.")
                else:          
                    f=d[5:n]
                    for a in range(0,g):
                        await message.channel.send(f)
            else:
                g=10
                p=d[5:]
                for a in range(0,g):
                    await message.channel.send(p)       

    
        
    if message.content == "!watt":
        await message.channel.send ("Hiiiiiiiiiiiii")



client.run('NzM0MzQ4NTg5MTQwMTQ4MjQ0.XxQZaw.jLqNY7x84vhc-L4Agx0jFNWTEYU')
