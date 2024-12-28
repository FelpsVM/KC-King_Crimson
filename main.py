import discord 
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

#Mega-Variables
load_dotenv()
guild_id = os.getenv('guild_id')
bot_token = os.getenv('token')
default_prefix = "!"

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix = "!", intents = intents)

    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id = guild_id))
        print(f"Synced slash commands for {self.user}.")
    
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

bot = Bot()

@bot.event
async def on_ready():
    guild = bot.get_guild(guild_id)
    if guild:
        print(f"Launched as ({bot.user.id}){bot.user.name} - Default server set to ({guild_id}){guild.name}")
    else:
        print(f"Launched as ({bot.user.id}){bot.user.name} - Default server set to {guild_id}")

@bot.hybrid_command(name = "prefix", with_app_command = True, description = "Show my default prefix")
@app_commands.guilds(discord.Object(id = guild_id))
async def prefix(ctx):
    await ctx.send(f"My atual prefix in this server is: {default_prefix}")
    
bot.run(bot_token)