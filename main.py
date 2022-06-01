# This example requires the 'message_content' privileged intents

import os
import disnake
from disnake.ext import commands


bot = commands.InteractionBot()


@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(os.environ["DISCORD_TOKEN"])
