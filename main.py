# This example requires the 'message_content' privileged intents

import os
import disnake
from disnake.ext import commands
import json


intent = disnake.Intents(message_content=True, messages=True, guilds=True)
bot = commands.Bot(command_prefix="!", sync_commands=True, intents=intent)


@bot.slash_command(name="health", description="health check")
async def health(inter):
    await inter.response.send_message("200 OK")


@bot.slash_command(name="hex", description="Gives anchor error for certain hex code")
async def multiply(inter, hexcode: str):
    print(hexcode, "hex")
    f = open("codes.json")
    data = json.loads(f.read())
    # print(data)
    try:
        error_obj = data[hexcode]
        msg = error_obj["message"]
        print(error_obj, msg)
        await inter.response.send_message(msg)
    except KeyError:
        await inter.response.send_message(
            "Invalid hex code or code doesnt exist in db, considering contributing at <https://github.com/anoushk1234/anchor-error>"
        )
    except:
        await inter.response.send_message("an unknown error has occured")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(os.environ["DISCORD_TOKEN"])
