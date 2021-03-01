import discord
from discord.ext import commands
import datetime
import discord.utils
import asyncio

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='./', description="Commands")



@bot.command()

async def ping(ctx):
  await ctx.send("pong")

bot.run('token')
