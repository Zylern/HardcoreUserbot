"""Command .currency <amount> <from> <to>
"""

from telethon import events
import asyncio
from datetime import datetime
import requests
from userbot.utils import register, admin_cmd
from requests import get

@register(outgoing=True, pattern="^\.currency (.*)")
async def moni(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(
                currency_from)
            current_response = get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await rkp.edit("{} {} = {} {}".format(
                    number, currency_from, rebmun, currency_to))
            else:
                await rkp.edit(
                    "`unknown currency, which I can't convert right now.`"
                )
        except Exception as e:
            await rkp.edit(str(e))
    else:
        await rkp.edit("`Use currency <amount> <from> <to>`")
        return
