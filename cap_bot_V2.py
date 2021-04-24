import discord
from discord.ext.commands import Bot
from discord.utils import get

TOKEN = 'ODE0MjU3NjQxOTQ5ODg4NTkz.YDbOhg.MafbU8qZJImtm30ETatqvqGFlTw'
bot = Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # Setting `Playing ` status
    #await bot.change_presence(activity=discord.Game(name="a game"))

    # Setting `Streaming ` status
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

    # Setting `Listening ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your bullshit"))

    # Setting `Watching ` status
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('<:angry_penis:835415989642199070>'):
        await message.channel.send('<:angry_penis:835415989642199070>')
        
    author=message.author
    if('fortnite' in message.content or 'Fortnite' in message.content):
        await message.channel.send("<@{}> imagine playing fortnite :clown:".format(author.id))
    await bot.process_commands(message)

@bot.command()
async def simp(ctx, user: discord.Member):
    ident = user.id
    if(ident==591065765185191983):     
        await ctx.send("<@{}> is a ***SIMP***".format(ctx.message.author.id))
    else:
        await ctx.send("<@{}> is a ***SIMP***".format(ident))


@bot.command(pass_context=True)
async def timeout(ctx, user: discord.Member):
    member = ctx.message.author
    ident = user.id

    role = discord.utils.find(lambda r: r.name == 'Retard Alert', user.guild.roles)#ctx.message.author.guild.roles)
    
    DNC = discord.utils.find(lambda r: r.name == 'Does Not Cap', ctx.message.author.guild.roles)
    admins = discord.utils.find(lambda r: r.name == 'Admins', ctx.message.author.guild.roles)
    decent = discord.utils.find(lambda r: r.name == 'Decent', ctx.message.author.guild.roles)

    if(DNC in member.roles or admins in member.roles or decent in member.roles):
        if(ident==591065765185191983):
            await  member.add_roles(role)
            await ctx.send("You have been assigned the Retard Alert role")
        else:           
            if(role in user.roles):
                await  user.remove_roles(role)
                await ctx.send("<@{}> has been unassigned the Retard Alert role".format(ident))
            else:
                await  user.add_roles(role)
                await ctx.send("<@{}> has been assigned the Retard Alert role".format(ident))
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
async def penis(ctx):
    await ctx.message.delete()
    await ctx.send("<:angry_penis:835415989642199070>")
    

@bot.command()
async def pfp(ctx, user: discord.Member):
    ident = user.id
    pfp = user.avatar_url
    await ctx.send("Here is <@{}>'s pfp {}".format(ident,pfp))

async def announce(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
async def commands(ctx):
    embed=discord.Embed(title="Here are my commands", description="""
**$penis**: Makes me respond with the <:angry_penis:835415989642199070> emoji
**$simp @user**: Makes me respond with the tagged user followed by 'is a ***SIMP*** '
**$downbad @user**: Assigns the tagged user the Downbad role
**$timeout @user**: Assigns the tagged user the Retard Alert role
**$pfp @user**: Makes me show the tagged user's pfp
Because I'm an asshole, I also call out users who mention 'Fortnite'""", color=0xb406cb)
    #embed.add_field(name="Gentle Reminder", value="""Most of my commands require special permissions. If a command doesn't work for you it means you're a peasant""", inline=False)
    embed.set_footer(text="Cap_Bot", icon_url="https://cdn.discordapp.com/emojis/813683190664790048.png?v=1")
    await ctx.send(embed=embed)


bot.run(TOKEN)
        
