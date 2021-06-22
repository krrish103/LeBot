import os
import discord
import pyshorteners
import smtplib
from PIL import Image
import png
import language
import json
import random
import pyqrcode
from pyqrcode import QRCode
from discord.ext import commands
import time
import nmap
import socket
import requests
import math

TOKEN = os.environ['TOKEN']

# DEFINING THE BOT
Bot = commands.Bot(command_prefix="-", intents = discord.Intents.all())
intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)
Bot.remove_command('help')



# WHEN BOT IS ONLINE
@Bot.event  # No brackets
async def on_ready():
    await Bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name='-help Made By AspireFlight#0946'))

    print("Bot is online")



@Bot.event
async def on_message_join(member):
    channel = Bot.get_channel(channel_id)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
    embed.set_thumbnail(url=member.avatar_url)

    await channel.send(embed=embed)

@Bot.event
async def on_message(message):
  await Bot.process_commands(message)
  if message.content == "-hello":
        await message.author.send("hello to you too")
  if message.content == "-hello":
      await message.author.send("hello to you too") 
  if message.content.startswith('-help'):
    embed = discord.Embed(
    color = discord.Colour.from_rgb(48, 37, 84)
   )
    embed.set_author(name="Help Command")
    embed.add_field(name="Command Prefix: ", value="-", inline=False)
    embed.add_field(name="avatar", value="Gets the Avatar of a User", inline=False)
    embed.add_field(name="id", value="Gets the ID of a User", inline=False)
    embed.add_field(name="shorten", value="Shortens the URL Provided", inline=False)
    embed.add_field(name="qrcode", value="Generate a QR Code  for the Text or LInk Provided", inline=False)
    embed.add_field(name="inspire", value="Sends An Inspirational Quote", inline=False)
    embed.add_field(name="help", value="Shows This Message", inline=False)
    embed.add_field(name="hi", value="Hello?", inline=False)
    embed.add_field(name="hello", value="DM's you back", inline=False)
    embed.add_field(name="dev", value="The Developer of the   Bot", inline=False)
    embed.add_field(name="calc", value="Can Add/Subtract/Multiply/Divide Numbers", inline=False)
    embed.add_field(name="invite", value="Invite the Bot to your Server!", inline=False)
    await message.channel.send(embed=embed)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

operations = ["add", "subtract", "multiply", "divide", "-", "+", "*", "/", "x"]

# COMMAND
@Bot.command()  # BRACKETS
async def hi(ctx):
    user = Bot.get_user("480341602796306432")
    await ctx.send("Hello")
    await user.send("Hello was used")

@Bot.command()
async def sqrt(ctx,*,message):
    num = float(message)
    sqrt = math.sqrt(num)
    print(sqrt)
    await ctx.send(sqrt)    

@Bot.command()  # BRACKETS
async def invite(ctx):
    embed = discord.Embed()
    embed.description = "<:invite:839052831536709694> ** [Click Here](http://bit.ly/Lebotinvite)** to Invite **LeBot** to your server!."
    await ctx.send(embed=embed)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@Bot.command()
async def servers(ctx):
    await ctx.channel.send("I'm in " + str(len(Bot.guilds)) + " servers!")

@Bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

@Bot.command()
async def poll(ctx,*,message):
    embed = discord.Embed(title="POLL", description=f"{message}")
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


@Bot.command()  # BRACKETS
async def dev(ctx):
    await ctx.send("<:aspireflight:840579032235769876> AspireFlight#0946")


@Bot.command()
async def ping(ctx):
    await ctx.send('My Ping is {0}'.format(round(Bot.latency, 1)))

@Bot.command()
async def qrcode(ctx, *, link):
    url = pyqrcode.create(link)
    url.png('QrCode.png', scale=6)
    await ctx.send(file=discord.File("QrCode.png"))



@Bot.command()
async def shorten(ctx, *, link):
    shortner = pyshorteners.Shortener()
    x = shortner.isgd.short(link)
    print(x)
    await ctx.send(x)


@Bot.command()  # BRACKETS
async def id(ctx, avamember: discord.Member = None):
    embed = discord.Embed(
        color=discord.Colour.red()
    )
    if avamember == None:
        avamember = ctx.author
    embed.set_author(name=f"User ID of {avamember}")
    embed.add_field(name=f"Requested by {ctx.author}", value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name=f"ID: ", value=f"{avamember.id}", inline=False)
    embed.set_thumbnail(url=avamember.avatar_url)
    await ctx.send(embed=embed)




@Bot.command()
async def avatar(ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        await ctx.send(embed=discord.Embed().set_image(url=member.avatar_url))

@Bot.command(aliases=["calc"])
async def calculate(ctx, function, n1, n2):
  try:
    cn1 = float(n1)
    cn2 = float(n2)
  except:
    await ctx.send("Syntax is -calculate <operation> <Number 1> <Number 2>")

  if function.lower() in operations:
    if function.lower() == "add" or function == "+":
      await ctx.send(f"Answer: {cn1+cn2}")
    if function.lower() == "subtract" or function == "-":
      await ctx.send(f"Answer: {cn1-cn2}")
    if function.lower() == "multiply" or function == "*" or function =="x":
      await ctx.send(f"Answer: {cn1*cn2}") 
    if function.lower() == "divide" or function == "/":
      await ctx.send(f"Answer: {cn1/cn2}")                 
  else:
    await ctx.send("Syntax is -calc <operation> <Number 1> <Number 2>")

@Bot.command(aliases=["remain"])
async def remainder(ctx, n1, n2):
  try:
    cn1 = float(n1)
    cn2 = float(n2)
    
  except:
    await ctx.send("Syntax is -remainder <Number 1> <Number 2>")

  answer = cn1 % cn2
  await ctx.send(answer)

@Bot.command(aliases=["hypot"])
async def hypotenuse(ctx, n1, n2):
  try:
    cn1 = float(n1)
    cn2 = float(n2)
    
  except:
    await ctx.send("Syntax is -hypot <Side A> <Side B>")

  answer = math.hypot(cn1, cn2)
  await ctx.send(answer)  
    
@Bot.command(aliases=["3root"])
async def cuberoot(ctx, n1):
  try:
    cn1 = float(n1)
        
  except:
    await ctx.send("`Syntax is -cuberoot <Number>`")

  answer = (cn1**(1/3))
  await ctx.send(answer)  
    
 
@Bot.command()
async def lcm(ctx, n1, n2):
  try:
    cn1 = int(n1)
    cn2 = int(n2)
  except:
      await ctx.send("Syntax is -lcm <Number 1> <Number 2>")
  if cn1 > cn2:
       greater = cn1
  else:
       greater = cn2

  if((greater % cn1 == 0) and (greater % cn2 == 0)):
    lcm = greater  
    greater += 1
  await ctx.send(lcm)

# RUNNING THE BOT
Bot.run(TOKEN)
