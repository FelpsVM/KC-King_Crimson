import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import json

# Mega-Variables
load_dotenv()
guild_id = int(os.getenv('guild_id'))  # Certifique-se de converter para int
bot_token = os.getenv('token')
minimum_role_id = os.getenv('minimum_role_id')
default_prefix = "!"

# Função para carregar prefixos salvos
def load_prefixes():
    try:
        with open("prefixes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar prefixos
def save_prefixes(prefixes):
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

# Carregar prefixos
prefixes = load_prefixes()

# Função para obter prefixo de um servidor
def get_prefix(bot, message):
    return prefixes.get(str(message.guild.id), default_prefix)

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix=get_prefix, intents=intents)

    async def setup_hook(self):
        await self.tree.sync(guild=discord.Object(id=guild_id))
        print(f"Synced slash commands for {self.user}.")

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral=True)

bot = Bot()

@bot.event
async def on_ready():
    guild = bot.get_guild(guild_id)
    if guild:
        print(f"Launched as ({bot.user.id}){bot.user.name} - Default server set to ({guild_id}){guild.name}")
    else:
        print(f"Launched as ({bot.user.id}){bot.user.name} - Default server set to {guild_id}")

@bot.hybrid_command(name="prefix", with_app_command=True, description="Show my  prefix")
@app_commands.guilds(discord.Object(id=guild_id))
async def prefix(ctx):
    current_prefix = prefixes.get(str(ctx.guild.id), default_prefix)
    await ctx.send(f"My current prefix in this server is: {current_prefix}")

@bot.hybrid_command(name="setprefix", with_app_command=True, description="Set a new prefix for this server")
@app_commands.guilds(discord.Object(id=guild_id))
async def setprefix(ctx, new_prefix: str):
    if discord.utils.get(ctx.author.roles, id=minimum_role_id):
        if len(new_prefix) > 5:
            await ctx.send("Prefix too long! Please use a prefix with up to 5 characters.")
            return

        prefixes[str(ctx.guild.id)] = new_prefix
        save_prefixes(prefixes)
        await ctx.send(f"Prefix updated to: {new_prefix}")
    else:
        await ctx.send("Você não tem o cargo mínimo")

@bot.hybrid_command(name="kick", with_app_command=True, description="Remove someone from the server")
@app_commands.guilds(discord.Object(id=guild_id))
async def kick(ctx, user: discord.Member, reason: str = "No reason provided"):
    if discord.utils.get(ctx.author.roles, id=int(minimum_role_id)):
        await user.kick(reason=reason)
        await ctx.send(f"The user ({user.id}) {user.name} was kicked for: {reason}")
    else:
        await ctx.send("Você não tem o cargo mínimo para usar este comando.")
        
bot.run(bot_token)