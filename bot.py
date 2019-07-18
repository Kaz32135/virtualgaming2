import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix= '.')

@bot.event
async def on_ready():
    print ("VG Bot a mers")
    print ("Virtual-Gaming Bot#1")

@bot.event
async def on_member_join(member):
    print(f'(member) s-a inregistrat pe server.')

@bot.event
async def on_member_remove(member):
    print(f'(member) a parasit server-ul.')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Virtual-Gaming! {round(bot.latency * 1000)}ms')

bot.run('NjAxMjg5MzA5MDM0NjQzNDU3.XTAKQQ.jnw7t4ogGPOg4nUuVKFxyHFVLW8')

    