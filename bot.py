import discord
from discord.ext import commands

from image_cog import image_cog
from music_cog import music_cog

Bot = commands.Bot(command_prefix='!')

Bot.add_cog(image_cog(Bot))
Bot.add_cog(music_cog(Bot))

token = ''
with open("token.txt") as file:
    token = file.read()
Bot.run(token)
