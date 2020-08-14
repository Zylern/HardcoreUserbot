"""COMMAND : .cool"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 40
    

    animation_ttl = range(0, 41)

    input_str = event.pattern_match.group(1)

    if input_str == "cool":

        await event.edit(input_str)

        animation_chars = [
            
            "😳",    
            "I am Putting my glasses.",
            "😳                           🕶🤏",
            "😳                          🕶🤏",
            "😳                         🕶🤏",
            "😳                        🕶🤏",
            "😳                       🕶🤏",
            "😳                      🕶🤏",
            "😳                     🕶🤏",
            "😳                    🕶🤏",
            "😳                   🕶🤏",
            "😳                  🕶🤏",
            "😳                 🕶🤏",
            "😳                🕶🤏",
            "😳               🕶🤏",
            "😳              🕶🤏",
            "😳             🕶🤏",
            "😳            🕶🤏",
            "😳           🕶🤏",
            "😳          🕶🤏",
            "😳         🕶🤏",
            "😳        🕶🤏",
            "😳       🕶🤏",
            "😳      🕶🤏",
            "😳     🕶🤏",
            "😳    🕶🤏",
            "😳   🕶🤏",
            "😳  🕶🤏",
            "😳 🕶🤏",
            "😎",
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 41])
