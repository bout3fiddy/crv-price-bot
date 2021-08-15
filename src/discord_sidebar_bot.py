import asyncio
from pycoingecko import CoinGeckoAPI

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=".")
token = ""
guild_id = 850700789831958559

COINGECKO = CoinGeckoAPI()


async def send_update():

    crv_price = COINGECKO.get_price(
        ids="curve-dao-token", vs_currencies="usd"
    )["curve-dao-token"]["usd"]
    nickname = (
        f"CRV ${crv_price}"
    )
    activity_status = "CRV Price"
    await bot.get_guild(guild_id).me.edit(nick=nickname)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=activity_status
        )
    )
    await asyncio.sleep(60)  # in seconds


@bot.event
async def on_ready():
    """
    When discord client is ready
    """
    while True:
        await send_update()


bot.run(token)
