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
TOKEN = "ODM0NzkzNDU3NjQ1Mzg3Nzg2.YIGD_g.kGs82liJuuDCHoStD2wE_g0f9Yo"

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
    embed.add_field(name="invite", value="Invite the Bot to your Server!", inline=False)
    await message.channel.send(embed=embed)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]


# COMMAND
@Bot.command()  # BRACKETS
async def hi(ctx):
    await ctx.send("Hello")

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
async def avatar(ctx, avamember: discord.Member = None):
    if avamember == None:
        avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


# RUNNING THE BOT
Bot.run(TOKEN)
