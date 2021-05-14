#Imports
import discord
import logging
import sys
import traceback
from discord.ext import commands
from typing import Optional
from discord import activity
from discord.enums import Status

#Defining bot
bot = commands.Bot(command_prefix='nt!')

#Debugging Log
logging.basicConfig(level=logging.INFO)

#Setting the status
activity = discord.Activity(name="First 100% made by Guff Discord bot!", type=discord.ActivityType.watching)

#Setting the client
client = discord.Client(activity=activity)

#Message de connection
@client.event
async def on_ready():
    print("Connecté en tant que {0.user}".format(client))

#####################Start of Bot############################

#Commande (nt!test) répond (Let's gooooo!)
@client.event
async def on_message(message):

    if message.content.startswith("nt!test"):
        await message.channel.send("Let's gooooo!")
        print("La commande nt!test a été évoqué.")

#Commande (nt!test2) delete la commande et répond avec un embed
@client.event
async def on_message(message):

    if message.content.startswith("nt!test2"):
        await message.delete()
        embed=discord.Embed(title="Guff Glitches", description="User Embed!!!", color=0x00ff00)
        embed.set_author(name="Guffy Boi", icon_url="https://i.ibb.co/CJPFXTC/guff-300x300-full-body.png")
        embed.add_field(name="I can send an embed! Isn't that cool?", value="Yes, it is", inline=True)
        embed.set_footer(text="I like ya cut g!")
        await message.channel.send(embed=embed)
        print("La commande nt!test2 a été évoqué.")


######################End of bot#############################



#Running the bot with the token (A besoin d'être la dernière ligne)
client.run("Real account Token, not a bot Token", bot=False)