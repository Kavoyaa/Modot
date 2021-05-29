'''
Prerequisite:
Make a file called '.env'
In that file, type 'token = <your bot token>'
'''

import discord
from discord.ext import commands
import os
import dotenv

# Set this to the prefix you want for your bot.
prefix = ">"
client = commands.Bot(command_prefix=prefix)

# Removing the defualt help command so we can use our custom help command
client.remove_command("help")


@client.event
async def on_ready():
    print("Bot online!")


# Kick command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    # Embed which will be sent when a person is banned
    embed = discord.Embed(color=discord.Color.red)
    
    embed.set_author(name=f'User Kicked | {member}',icon_url=member.avatar_url)
    
    embed.add_field(name='User', value=f'{member.mention}', inline=True)
    
    embed.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=True)

'''
You can do the following if you're using replit.com and this
method dosen't work:
client.run(os.getenv('token'))

You can also use the following if no one can see your code:
client.run(<your bot token here>)
This way you don't need a '.env' file and no need to import os and dotenv
Keep in mind that if someone can see your code, they will we able to see your bot token and get access to your bot.
'''
dotenv.load_dotenv()
client.run(os.environ.get("token"))
