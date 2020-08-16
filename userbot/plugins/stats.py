import asyncio, time, io, math, os, logging, asyncio, shutil, re, subprocess, json
from userbot.utils import admin_cmd
from userbot.utils import register
from telethon.tl import functions
from datetime import datetime
from userbot import client, BOTLOG_CHATID, CMD_HELP, BOTLOG, BOTLOG_CHATID, bot
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.errors import FloodWaitError
from bs4 import BeautifulSoup
from time import sleep





@register(outgoing=True, pattern=r"^.stats(?: |$)(.*)") 
async def stats(event: NewMessage.Event) -> None:  
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    if not sender.id == me.id and not SUDO_USERS:
       return await rkp.edit("`Sorry normal sudo users cant access this command..`")
    try:
       await e.delete()
    except:
    	pass    
    waiting_message = await rkp.edit('`Collecting.........`')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):           
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif entity.megagroup:
                groups += 1
                if entity.creator or entity.admin_rights:                    
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f' **Stats for {full_name}** \n\n'
    response += f'**Private Chats:** {private_chats} \n'
    response += f'   • `Users: {private_chats - bots}` \n'
    response += f'   • `Bots: {bots}` \n'
    response += f'**Groups:** {groups} \n'
    response += f'**Channels:** {broadcast_channels} \n'
    response += f'**Admin in Groups:** {admin_in_groups} \n'
    response += f'   • `Creator: {creator_in_groups}` \n'
    response += f'   • `Admin Rights: {admin_in_groups - creator_in_groups}` \n'
    response += f'**Admin in Channels:** {admin_in_broadcast_channels} \n'
    response += f'   • `Creator: {creator_in_channels}` \n'
    response += f'   • `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'**Unread:** {unread} \n'
    response += f'**Unread Mentions:** {unread_mentions} \n\n'
    response += f'__It Took:__ {stop_time:.02f}s \n'
    await waiting_message.edit(response)



CMD_HELP.update({
    "stats":
    "`.stats `\
\n**Usage:** Command to get stats about your account\
"
})