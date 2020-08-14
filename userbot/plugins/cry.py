"""Emoji

Available Commands:

.cry


"""

from telethon import events

import asyncio



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 33)

    input_str = event.pattern_match.group(1)

    if input_str == "cry":

        await event.edit(input_str)

        animation_chars = [

            "`😞`",
            "`😔`",    
            "`☹️`",
            "`😖`",
            "`😩`",
            "`🥺`",
            "`😢`",
            "`😭`",
            "`😞`",
            "`😔`",    
            "`☹️`",
            "`😖`",
            "`😩`",
            "`🥺`",
            "`😢`",
            "`😭`",
            "`😞`",
            "`😔`",    
            "`☹️`",
            "`😖`",
            "`😩`",
            "`🥺`",
            "`😢`",
            "`😭`",
            "`😞`",
            "`😔`",    
            "`☹️`",
            "`😖`",
            "`😩`",
            "`🥺`",
            "`😢`",
            "😭",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 33])
