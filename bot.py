import discord
from discord.ext import commands
import requests
import json
from requests.api import get
client=discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')   
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    data = json.loads(response.text)
    author = data[0]['a']
    return(quote,author)

k={'!thunder':"<@248742722221899778>",'!scout':"<@269369856229376000>",'!killer':"<@444583334539165697>",
'!rage':"<@337167925519712267>",'!taher':"<@713328216634425355>",'!serial':"<@250928149494235146>",'!tohan':"<@755245777915347055>",
  '!flames':"<@249520197919178763>"}
c= "abc"

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

    if message.content in k :
        c=k.get(message.content)
        for a in range(0,10):
            await message.channel.send(c)
            
    
    
        
    if message.content == "!watt":
        await message.channel.send ("Hiiiiiiiiiiiii")



client.run('NzM0MzQ4NTg5MTQwMTQ4MjQ0.XxQZaw.jLqNY7x84vhc-L4Agx0jFNWTEYU')
