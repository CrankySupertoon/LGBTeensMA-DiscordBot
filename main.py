import discord
import random
import os
import requests
import aiohttp
import box
import datetime
import time
import platform

from dadjokes import *
from discord.ext import commands
from datetime import datetime
from keep_alive import keep_alive

#Core Variables
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(description="LGBTeens Bot", command_prefix="!", intents=intents)
client.remove_command('help')

#Starting Bot
@client.event
async def on_ready():
    print("Logged in as:\n{}\n\n{}#{}\n----------".format(client.user.id, client.user.name, client.user.discriminator))
    print("#################\n# Bot is online #\n#################")
    launch_time = time.time()
    await client.change_presence(
        activity=discord.Game(name='around with different names'))

#Join Logs
@client.event
async def on_member_join(member):
  welcomechannel = client.get_channel(780936979067830272)
  staffwelcomechannel = client.get_channel(780939099283521557)
  jl = [
        f"We've got gays {member.mention}!",
        f"Isn't there a discord server for gays like {member.mention}?",
        f"I hope {member.mention} likes being gay?",
        f"Being Trans is a phase, or is it {member.mention}?",
        f"You like gays {member.mention}? Hopefully!",
        f"Once you comeout {member.mention}, you just keep coming out and out and out...!",
        f"Every {member.mention} is like a bird, they just fly in out of nowhere and poop on your head! Not really though!",
        f"Never going give {member.mention} up, never going let {member.mention} down",
        f"I see a message in the sky it says, “god belives in {member.mention}!",
        f":notes:I see trees of green, {member.mention}  too:notes: and i think to myself what a wonderful world we are living in!:notes:",
        f"{member.mention} came out, and got accepted!",
        f"A new player has came out, quick {member.mention}, show them what you can do!",
        f"It’s time to come out, come out. It's time to come come out. It's time to COMEEE OUTTTT {member.mention}!!!!",
        f"Obviously {member.mention} is not gay, am I right or am I right! :sunglasses:"
    ]
  jlrandom = random.choice(jl)
  await welcomechannel.send(f"{jlrandom}")
  await staffwelcomechannel.send(f"{member} Joined. Account created on {member.created_at}")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(780936979067830272)
    staff_channel = client.get_channel(780939099283521557)
    await channel.send(f"{member.mention} was outed by their parents")
    await staff_channel.send(f"{member.mention} left")


#Suggestions
#@client.event
#async def on_message(message):
#  if message.channel.id == 759913865848553513:
#    await message.add_reaction('👍')
#    await message.add_reaction('👎')
#  await client.process_commands(message)


#Help Command
@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.orange())
    embed.set_author(name="Commands:")

    #General Comamnds
    embed.add_field(
        name="General",
        value=
        "!help - Shows This Message\n\n!ping - Says Pong Back To You\n\n!server - Shows Server Info\n\n!stats - Show Bot Stats",
        inline=False)

    #Fun Comamnds
    embed.add_field(
        name="Fun",
        value=
        "!toss - Coin Flip\n\n!joke - Give a Dad Joke\n\n!dice - Roll 1-6\n\n!reverse - Reverses the given text\n\n!meme - Gives a random meme\n\n!r/lgbteens - shows a random post from the LGBTeens subreddit.",
        inline=False)
    await ctx.send(author, embed=embed)

@client.command("server")
async def s_info(ctx):
    server = ctx.guild
    icon = ("\uFEFF")
    embed = discord.Embed(
        title=f"Server info for {server.name}",
        description=None,
        colour=0x98FB98)
    embed.set_thumbnail(url=server.icon_url_as(size=256))
    # Basic info -- Name, Region, ID, Owner (USER+descrim, ID), Creation date, member count
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    #embed.add_field(name="Owner", value=f"{server.owner}", inline=True)
    embed.add_field(
        name="Creation Date", value=f"{server.created_at}", inline=True)
    #embed.add_field(name="Server Icon Url", value=server.icon_url, inline=False)
    embed.add_field(
        name="Member Count", value=server.member_count, inline=True)
    await ctx.send(content=None, embed=embed)






#Ping Command
@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')


#Roll Dice Command
@client.command(aliases=["roll"])
async def dice(ctx):
    """Rolls the dice"""
    cont = random.randint(1, 6)
    await ctx.send("You Rolled **{}**".format(cont))


#Co""in Flip Command
@client.command(aliases=["flip"])
async def toss(ctx):
    """Put the toss"""
    ch = ["Heads", "Tails"]
    rch = random.choice(ch)
    await ctx.send(f"You got **{rch}**")


#Reverse Text Command
@client.command()
async def reverse(ctx, *, text):
    """Reverse the given text"""
    await ctx.send("".join(list(reversed(str(text)))))


#Meme Command
@client.command()
async def meme(ctx):
    """Sends you random meme"""
    r = await aiohttp.ClientSession().get(
        "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100")
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)


#RFTB Command
@client.command(aliases=['r/lgbteens', 'r/lgbteen', "rlgbteens"])
async def rlgbteen(ctx):
    """Sends you a random post from r/feedthebeast"""
    r = await aiohttp.ClientSession().get(
        "https://www.reddit.com/r/lgbteens.json?sort=new&t=day&limit=100")
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)


#Reddit Wide Search Command
@client.command()
async def reddit(ctx, meme_term):
    url_comb = "https://www.reddit.com/search.json?sort=new&limit=100&q=" + meme_term
    r = await aiohttp.ClientSession().get(url_comb)
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)


#Dadjoke Command
@client.command(aliases=["dadjoke"])
async def joke(ctx):
    """Sends the dadjokes"""
    async with ctx.typing():
        await ctx.send(Dadjoke().joke)


#Stats Command
@client.command()
async def stats(ctx):

    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(
        title=f'{client.user.name} Stats',
        description='\uFEFF',
        colour=ctx.author.colour,
        timestamp=ctx.message.created_at)

    embed.add_field(
        name='Python Version:', value=f"{pythonVersion}", inline=False)
    embed.add_field(
        name='Discord.Py Version', value=f"{dpyVersion}", inline=False)
    embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
    embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
    embed.add_field(name='Bot Developers:', value="<@543576276108181506>")

    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)


#Poll Command
@client.command(pass_context=True)
async def poll(ctx, *args):
    mesg = ' '.join(args)
    await ctx.message.delete()
    embed = discord.Embed(
        title='A Poll has Started !',
        description='{0}'.format(mesg),
        color=0x00FF00)

    embed.set_footer(text='Poll created by: {0} • React to vote!'.format(
        ctx.message.author))

    embed_message = await ctx.send(embed=embed)

    await embed_message.add_reaction('👍')
    await embed_message.add_reaction('👎')
    await embed_message.add_reaction('🤷')


@client.command(pass_context=True)
async def ban(ctx, user: discord.Member, *, arg):
    author = ctx.message.author
    reason = arg
    server = ctx.guild.name
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    staff_log = client.get_channel(780939099283521557)
    embed = discord.Embed(
        name="MEMBER_BANNED",
        description="------------------------------------------------------",
        color=0x00ff00)
    embed.set_author(name="Member Banned:\nMember Banned Successfully")
    embed.add_field(
        name="Banned by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Banned: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(
        text="Requested by {} \a {}".format(author, data),
        icon_url=author.avatar_url)
    await ctx.send(embed=embed)
    embed = discord.Embed(
        name="MEMBER_BANNED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Banned:")
    embed.add_field(
        name="Banned by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Banned: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Banned at {}".format(data))
    await staff_log.send(embed=embed)
    embed = discord.Embed(
        name="BANNED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Banned:\nYou've been Banned")
    embed.add_field(
        name="Banned by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Banned in: ", value="{}".format(server), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Banned at {}".format(data))
    await user.send(user, embed=embed)
    await ctx.guild.ban(user, reason=reason)

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member, *, arg):
    author = ctx.message.author
    reason = arg
    server = ctx.guild.name
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    staff_log = client.get_channel(780939099283521557)
    embed = discord.Embed(
        name="MEMBER_KICKED",
        description="------------------------------------------------------",
        color=0x00ff00)
    embed.set_author(name="Member Kicked:\nMember Kicked Successfully")
    embed.add_field(
        name="Kicked by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Kicked: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Kicked: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(
        text="Requested by {} \a {}".format(author, data),
        icon_url=author.avatar_url)
    await ctx.send(embed=embed)
    embed = discord.Embed(
        name="MEMBER_KICKED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Kicked:")
    embed.add_field(
        name="Kicked by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Kicked: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Kicked at {}".format(data))
    await staff_log.send(embed=embed)
    embed = discord.Embed(
        name="KICKED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Kicked:\nYou've been Kicked")
    embed.add_field(
        name="Kicked by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Kicked in: ", value="{}".format(server), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Kicked at {}".format(data))
    await user.send(user, embed=embed)
    await ctx.guild.kick(user, reason=reason)

#Run Bot
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
