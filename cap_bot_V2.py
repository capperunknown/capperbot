import discord
from discord.ext.commands import Bot
from discord.utils import get

TOKEN = 'ADD TOKEN HERE'
bot = Bot(command_prefix='$')
#test from vscode

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('CAPPER BOT IS NOW ACTIVE')
    # Setting `Playing ` status
    #await bot.change_presence(activity=discord.Game(name="a game"))

    # Setting `Streaming ` status
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

    # Setting `Listening ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$commands"))

    # Setting `Watching ` status
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('<:angry:835398771491733515>'):
        await message.channel.send('<:angry:835398771491733515>')
        
    author=message.author
    if('fortnite' in message.content or 'Fortnite' in message.content):
        await message.channel.send("<@{}> is playing fortnite :LOL:".format(author.id))
    await bot.process_commands(message)

@bot.command()
async def callOut(ctx, user: discord.Member):
    ident = user.id
    if(ident==591065765185191983):     
        await ctx.send("<@{}> WARNING".format(ctx.message.author.id))
    else:
        await ctx.send("<@{}> WARNING".format(ident))


@bot.command(pass_context=True)
async def timeout(ctx, user: discord.Member):
    member = ctx.message.author
    ident = user.id

    role = discord.utils.find(lambda r: r.name == 'Student', user.guild.roles)#ctx.message.author.guild.roles)
    
    DNC = discord.utils.find(lambda r: r.name == 'Does Not Cap', ctx.message.author.guild.roles)
    admins = discord.utils.find(lambda r: r.name == 'Admins', ctx.message.author.guild.roles)
    decent = discord.utils.find(lambda r: r.name == 'Decent', ctx.message.author.guild.roles)

    if(DNC in member.roles or admins in member.roles or decent in member.roles):
        if(ident==591065765185191983):
            await  member.add_roles(role)
            await ctx.send("You have been assigned the Student role")
        else:           
            if(role in user.roles):
                await  user.remove_roles(role)
                await ctx.send("<@{}> has been unassigned the Student role".format(ident))
            else:
                await  user.add_roles(role)
                await ctx.send("<@{}> has been assigned the Student role".format(ident))
    else:
        await ctx.send("Request to Change Role Denied: Invalid Permissions")

@bot.command(pass_context=True)
async def downbad(ctx, user: discord.Member):
    member = ctx.message.author
    ident = user.id

    role = discord.utils.find(lambda r: r.name == 'Downbad', user.guild.roles)#ctx.message.author.guild.roles)
    
    DNC = discord.utils.find(lambda r: r.name == 'Does Not Cap', ctx.message.author.guild.roles)
    admins = discord.utils.find(lambda r: r.name == 'Admins', ctx.message.author.guild.roles)
    decent = discord.utils.find(lambda r: r.name == 'Decent', ctx.message.author.guild.roles)
    
    if(DNC in member.roles or admins in member.roles or decent in member.roles):
        if(ident==591065765185191983):
            await  member.add_roles(role)
            await ctx.send("<@{}> is downbad".format(member.id))
        else:         
            if(role in user.roles):
                await  user.remove_roles(role)
                await ctx.send("<@{}> has come to their senses".format(ident))
            else:
                await  user.add_roles(role)
                await ctx.send("<@{}> is down horrendously".format(ident))
    else:
        await ctx.send("Request to Change Role Denied: Invalid Permissions")


@bot.command()
async def angry(ctx):
    await ctx.message.delete()
    await ctx.send("<:angry:835398771491733515>")
    

@bot.command()
async def pfp(ctx, user: discord.Member):
    ident = user.id
    pfp = user.avatar_url
    await ctx.send("Here is <@{}>'s pfp {}".format(ident,pfp))
    
@bot.command()
async def announce(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
async def associates(ctx):
    guild = bot.get_guild(809500009124855878)
    for member in guild.Members:
        if(member!=591065765185191983):
            await member.edit(nick='TEST')
    
    
@bot.command(pass_context = True)
async def purge(ctx, number):
    member = ctx.message.author
    DNC = discord.utils.find(lambda r: r.name == 'Does Not Cap', ctx.message.author.guild.roles)
    admins = discord.utils.find(lambda r: r.name == 'Admins', ctx.message.author.guild.roles)
    
    if(DNC in member.roles or admins in member.roles):
        await ctx.channel.purge(limit=int(number))
        await ctx.send("{} messages were purged.".format(number))
    else:
        await ctx.send("Cannot Purge: Invalid Permissions")

@bot.command()
async def commands(ctx):
    embed=discord.Embed(title="Here are my commands", description="""
**$callOut @user**: Makes me callout a user'
**$downbad @user**: Assigns the tagged user the Downbad role
**$timeout @user**: Assigns the tagged user the Retard Alert role
**$pfp @user**: Makes me show the tagged user's pfp
**$purge amount**: I will purge the last given amount of messages in the current channel""", color=0xb406cb)
    #embed.add_field(name="Gentle Reminder", value="""Most of my commands require special permissions. If a command doesn't work for you it means you're a peasant""", inline=False)
    embed.set_footer(text="Cap_Bot", icon_url="https://cdn.discordapp.com/emojis/835398771491733515.png?v=1")
    await ctx.send(embed=embed)


bot.run(TOKEN)
        
