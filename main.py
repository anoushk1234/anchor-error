# This example requires the 'message_content' privileged intents

import os
import disnake
from disnake.ext import commands
import json


intent = disnake.Intents(message_content=True, messages=True, guilds=True)
bot = commands.Bot(command_prefix="!", sync_commands=True, intents=intent)


@bot.slash_command(description="Responds with 'World'")
async def hello(inter):
    await inter.response.send_message("World")


@bot.slash_command(name="hex", description="Gives anchor error for certain hex code")
async def multiply(inter, hexcode: str):
    print(hexcode, "hex")
    f = open("codes.json")
    data = json.loads(f.read())
    # print(data)
    error_obj = data[hexcode]
    msg = error_obj["message"]
    print(error_obj, msg)
    await inter.response.send_message(msg)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(os.environ["DISCORD_TOKEN"])
