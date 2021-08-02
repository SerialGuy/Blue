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

k={'thunder':"<@248742722221899778>",'scout':"<@269369856229376000>",'killer':"<@444583334539165697>",
'rage':"<@337167925519712267>",'taher':"<@713328216634425355>",'serial':"<@250928149494235146>",'tohan':"<@755245777915347055>",
  'flames':"<@249520197919178763>",'assassin':"<@671290157818839071>",'adib':"<@840566992443277402>",'abesh':"<@748602930931957763>"}
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
        n=d.find(" ",5,20)
        if d[5:n] in k:
            g=d[n+1:]
            g=int(g) 
            if g>251:
                await message.channel.send("No. Cannot be larger than 250")
            else:
                f=k.get(d[5:n])
                for a in range(0,g):
                    await message.channel.send(f)
        else:
            g=10
            p=k.get(d[5:])
            for a in range(0,g):
                await message.channel.send(p)
    
        
    if message.content == "!watt":
        await message.channel.send ("Hiiiiiiiiiiiii")



client.run('NzM0MzQ4NTg5MTQwMTQ4MjQ0.XxQZaw.jLqNY7x84vhc-L4Agx0jFNWTEYU')
