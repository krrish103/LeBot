import os
import discord
import pyshorteners
import smtplib
from PIL import Image
import png
import pyqrcode
from pyqrcode import QRCode
from discord.ext import commands

TOKEN = 'ODM0NzkzNDU3NjQ1Mzg3Nzg2.YIGD_g.kGs82liJuuDCHoStD2wE_g0f9Yo'

# DEFINING THE BOT
Bot = commands.Bot(command_prefix="-")
client = discord.Client()


# WHEN BOT IS ONLINE
@Bot.event  # No brackets
async def on_ready():
    await Bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name='-help Made By AspireFlight#0946'))

    print("Bot is online")


@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    if message.content == "-hello":
        await message.author.send("hello to you too")


# COMMAND
@Bot.command()  # BRACKETS
async def hi(ctx):
    await ctx.send("Hello")


@Bot.command()  # BRACKETS
async def dev(ctx):
    await ctx.send("AspireFlight#0946")


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