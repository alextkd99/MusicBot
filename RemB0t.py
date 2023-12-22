import discord
from discord.ext import commands
import youtube_dl
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message content intent
intents.guilds = True
intents.voice_states = True

# Bot setup with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Basic command to check if the bot is responsive
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Play command
@bot.command(name='play')
async def play(ctx, *, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.message.author.voice.channel
    if not ctx.voice_client:
        await channel.connect()

    voice_client = ctx.voice_client

    with YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(FFmpegPCMAudio(URL))

    await ctx.send(f"Now playing: {info['title']}")

# Command to leave the voice channel
@bot.command(name='leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Run the bot with your token
bot.run('MTExOTAyNTkyODE2MTQ3NjY0OA.GJBn3f.AdAsjSedjt1Zuk7rrSgN3vx4YsHGVmCRgh2Arc')
