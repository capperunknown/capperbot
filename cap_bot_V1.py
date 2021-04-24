import discord
from discord.ext.commands import Bot
from discord.utils import get

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

email = "javamailtest093@gmail.com" # the email where you sent the email
password = "javamail"

TOKEN = 'ODE0MjU3NjQxOTQ5ODg4NTkz.YDbOhg.DtiGZZdqbwSOmdP38gpANj3nLrs'
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
    if message.content.startswith('<:angry_penis:813683190664790048>'):
        await message.channel.send('<:angry_penis:813683190664790048>')
        
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
    perms = discord.utils.find(lambda r: r.name == 'mod', ctx.message.author.guild.roles)
    middi = discord.utils.find(lambda r: r.name == 'Server Therapist', ctx.message.author.guild.roles)
    admin = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.author.guild.roles)
    if(perms in member.roles or middi in member.roles or admin in member.roles):
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
    role = discord.utils.find(lambda r: r.name == 'Horny Jail', user.guild.roles)#ctx.message.author.guild.roles)
    perms = discord.utils.find(lambda r: r.name == 'mod', ctx.message.author.guild.roles)
    middi = discord.utils.find(lambda r: r.name == 'Server Therapist', ctx.message.author.guild.roles)
    admin = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.author.guild.roles)
    if(perms in member.roles or middi in member.roles or admin in member.roles):
        if(ident==591065765185191983):
            await  member.add_roles(role)
            await ctx.send("You have been put in Horny Jail")
        else:         
            if(role in user.roles):
                await  user.remove_roles(role)
                await ctx.send("<@{}> has been released from Horny Jail".format(ident))
            else:
                await  user.add_roles(role)
                await ctx.send("<@{}> has been put in Horny Jail".format(ident))
    else:
        await ctx.send("Request to Change Role Denied: Invalid Permissions")


@bot.command()
async def penis(ctx):#for AS101 Server
    await ctx.send("<:angry_penis:813683190664790048>")
    await ctx.message.delete()

@bot.command()
async def shid(ctx):#for AS101 Server
    await ctx.send("""
░░░░░░░░░░░█▀▀░░█░░░░░░
░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
░░░░░░█░█░░░░░░░░░░▐░░░
░░░░░░▐▐░░░░░░░░░▄░▐░░░
░░░░░░█░░░░░░░░▄▀▀░▐░░░
░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
░░█░░░▐░░░░░░░░▄░█░░░░░
░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░
░░░▀▀░▄TSM▄░░░▐▄▄▄▀░░░░""")
    await ctx.message.delete()

@bot.command()
async def DB(ctx):#for AS101 Server
    await ctx.send("""
░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▄▀▀▀▀▄░░░
░░░░░░░░░░▄▀░░▄░▄░█░░
░▄▄░░░░░▄▀░░░░▄▄▄▄█░░
█░░▀▄░▄▀░░░░░░░░░░█░░
░▀▄░░▀▄░░░░█░░░░░░█░░
░░░▀▄░░▀░░░█░░░░░░█░░
░░░▄▀░░░░░░█░░░░▄▀░░░
░░░▀▄▀▄▄▀░░█▀░▄▀░░░░░
░░░░░░░░█▀▀█▀▀░░░░░░░
░░░░░░░░▀▀░▀▀░░░░░░░░""")
    await ctx.message.delete()

@bot.command()
async def COCK(ctx):#for Wonderland_Tingz_Server
    channel = bot.get_channel(798339279466135582)
    await ctx.send("<:angry_penis:814680187614527508>")

@bot.command()
async def pfp(ctx, user: discord.Member):
    ident = user.id
    pfp = user.avatar_url
    await ctx.send("Here is <@{}>'s pfp {}".format(ident,pfp))
        
@bot.command()
async def fermentedwhalecum(ctx):
    await ctx.send("<@485215049133064204> The council would like to speak to you about your username")
    await ctx.message.delete()
        
@bot.command(pass_context=True)
async def nicks(ctx, user: discord.Member, nick):
    member = ctx.message.author
    ident = user.id
    
    perms = discord.utils.find(lambda r: r.name == 'mod', ctx.message.author.guild.roles)
    middi = discord.utils.find(lambda r: r.name == 'Server Therapist', ctx.message.author.guild.roles)
    admin = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.author.guild.roles)
    
    if(perms in member.roles or middi in member.roles or admin in member.roles):
        if(ident==591065765185191983):
            await ctx.send('Request to Change Nickname Denied')
        else:
            await user.edit(nick=nick)
            await ctx.send('Nickname was changed for <@{}>'.format(user.id))
    else:
        await ctx.send('Request to Change Nickname Denied')

@bot.command()
async def reset(ctx, user: discord.Member):
    ident = user.id
    if(ident!=591065765185191983):
        await user.edit(nick=user.name)
        await ctx.send('Username was reset successfully')
    else:
        await ctx.send('Request to Reset Nickname Denied')
@bot.command()
async def ninja(ctx):
    await ctx.send("***The fuck did you say to me, you little shit? How are you not in fucking school? You kiss your mother with that mouth? It's called you kiss your mother with that fucking mouth? Huh? Huh? Because the fucking youth of. You shut up when I'm talking to you, you shut your mouth!***")
@bot.command()
async def announce(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
async def spam(ctx, amount):
    for i in range(int(amount)):
        await ctx.send('kys bitch')

@bot.command()
async def commands(ctx):
    embed=discord.Embed(title="Here are my commands", description="""
**$emailer address text:** Makes me send an email to a given email address with the provided text
**$penis**: Makes me respond with the <:angry_penis:813683190664790048> emoji
**$simp @user**: Makes me respond with the tagged user followed by 'is a ***SIMP*** '
**$ninja**: Makes me respond with a script of Ninja raging
**$downbad @user**: Assigns the tagged user the Horny Jail role
**$timeout @user**: Assigns the tagged user that Retard Alert role
**$shid**: Makes me send a giant ASCII image of a man shitting
**$DB**: Makes me send a giant ASCII dick butt
**$pfp @user**: Makes me show the tagged user's pfp
**$nicks @user nick**: Makes me change the tagged user's nickname with the text in 'nick'
**$reset @user**: Makes me reset the tagged user's nickname
Because I'm an asshole, I also call out users who mention 'Fortnite'""", color=0xb406cb)
    #embed.set_author(name="cxpper")
    embed.add_field(name="Gentle Reminder", value="""Most of my commands require special permissions. If a command doesn't work for you it means you're a peasant""", inline=False)
    embed.set_footer(text="Cap_Bot", icon_url="https://cdn.discordapp.com/emojis/813683190664790048.png?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def emailer(ctx, to_mail,*, texts):
    await ctx.send('Processing Email Request')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        msg = MIMEMultipart()
        msg["From"] = str(email)
        msg["To"] = str(to_mail)
        #msg["Subject"] = str(subj)
        msg.attach(MIMEText(texts, 'plain'))
        text = msg.as_string()

        embed = discord.Embed(color=0xb406cb, timestamp=datetime.datetime.utcfromtimestamp(1617082729))

        embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/281/281769.png")
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Presented by Cap_Bot", icon_url="https://cdn.discordapp.com/emojis/813683190664790048.png?v=1")

        embed.add_field(name="From:", value=email, inline=False)
        embed.add_field(name="To:", value=to_mail, inline=False)
        #embed.add_field(name="Subject:", value=subj, inline=False)
        embed.add_field(name="Body:", value=texts, inline=False)

        await ctx.send(embed=embed)
        server.sendmail(email, to_mail, text)
        server.quit()

    except:
        await ctx.send('Request to send email failed. Possible invalid receiving address')
    else:
        await ctx.send('Request to send email successful <:angry_penis:814680187614527508>')

bot.run(TOKEN)
        
