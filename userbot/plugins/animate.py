"""COMMAND : .aag, .cool .cry .tcloud .sneeze"""

from telethon import events
from collections import deque
from userbot.utils import admin_cmd
import asyncio



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 40
    

    animation_ttl = range(0, 41)

    input_str = event.pattern_match.group(1)

    if input_str == "aag":

        await event.edit(input_str)

        animation_chars = [
            
            "`🔥`",    
            "🌬💨                                   🔥",
            "🌬 💨                                  🔥",
            "🌬  💨                                 🔥",
            "🌬   💨                                🔥",
            "🌬    💨                               🔥",
            "🌬     💨                              🔥",
            "🌬      💨                             🔥",    
            "🌬       💨                            🔥",
            "🌬        💨                           🔥",
            "🌬         💨                          🔥",
            "🌬          💨                         🔥",
            "🌬           💨                        🔥",
            "🌬            💨                       🔥",
            "🌬             💨                      🔥",
            "🌬              💨                     🔥",
            "🌬               💨                    🔥",
            "🌬                💨                   🔥",
            "🌬                 💨                  🔥",
            "🌬                  💨                 🔥",
            "🌬                   💨                🔥",
            "🌬                    💨               🔥",
            "🌬                     💨              🔥",
            "🌬                      💨             🔥",
            "🌬                       💨            🔥",
            "🌬                        💨           🔥",
            "🌬                         💨          🔥",
            "🌬                          💨         🔥",
            "🌬                           💨        🔥",
            "🌬                            💨       🔥",
            "🌬                             💨      🔥",
            "🌬                              💨     🔥",
            "🌬                               💨    🔥",
            "🌬                                💨   🔥",
            "🌬                                 💨  🔥",
            "🌬                                  💨 🔥",
            "🌬                                   💨🔥",
            "🌬                                       ",
            "😁",
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 41])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 50
    

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "cool":

        await event.edit(input_str)

        animation_chars = [
            
            "I am Putting my glasses.",
            "😳⁡ ⁠⁠",    
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


            await event.edit(animation_chars[i % 30])
            
           
            
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.50

    animation_ttl = range(0, 32)

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

            await event.edit(animation_chars[i % 32])
            
            
                       
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.40

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "tcloud":

        await event.edit(input_str)

        animation_chars = [

            "☁️️",
            "🌩",    
            "⛈",
            "🌧",
            "🌨",
            "🌦",
            "🌥",
            "⛅",
            "🌤",
            "☀",    
            "☁️️",
            "🌩",    
            "⛈",
            "🌧",
            "🌨",
            "🌦",
            "🌥",
            "⛅",
            "🌤",
            "☀",    
            "☁️️",
            "🌩",    
            "⛈",
            "🌧",
            "🌨",
            "🌦",
            "🌥",
            "⛅",
            "🌤",
            "☀",    
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.50

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "sneeze":

        await event.edit(input_str)

        animation_chars = [

            "`😦`",  
            "`😮`",
            "`😲`",
            "`😵`",
            "`🤧`",
            "`😖`",
            "`😦`",  
            "`😮`",
            "`😲`",
            "`😵`",
            "`🤧`",
            "`😖`",
            "`😦`", 
            "`😮`",
            "`😲`",
            "`😵`",
            "`🤧`",
            "`😖`",
            "`😦`",
            "`😮`",
            "`😲`",
            "`😵`",
            "`🤧`",
            "`😖`",
            "`😦`", 
            "`😮`",
            "`😲`",
            "`😵`",
            "`🤧`",
            "`😖`",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
