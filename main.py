
import requests
import discord 
from discord.ext import commands 
from price import btcbrl
from price import ethbrl

from time import sleep

client = commands.Bot(command_prefix = "<<", case_insensitive = True)

@client.event
async def on_ready():
  print('aaa')

@client.command()
async def ban(ctx):
  await ctx.send('Mizeravel o suficiente pra conseguir o fato de ser odiado por todos')

#Valor 


@client.command()
async def start(ctx):
  a = 1
  await ctx.send("**Canal setado**")
  while a == 1:
   
    btc = btcbrl()
    eth = ethbrl()

    await ctx.send("https://cdn.discordapp.com/emojis/841749229834731533.png?v=1&size=40")
    await ctx.send("R$" + btc)
    await ctx.send("https://media.discordapp.net/attachments/809092580703862794/841770470839418900/ethereum.png?width=40&height=40")
    await ctx.send("R$" + eth)

    sleep(1200)

  @client.command()
  async def stop(ctx):
    a = 0
    await ctx.send("Parando")
      

  

client.run('ODQxNzE4MzA3NDUxMzA2MDI0.YJq1Qg.U77apI2hekCE3_ZLAfg_uf5gaBw')

