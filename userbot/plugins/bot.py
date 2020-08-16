import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot.utils import register
from telethon.tl import functions
from userbot import CMD_HELP




@borg.on(admin_cmd(pattern=f"names(?: |$)(.*)", allow_sudo=True))
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:
    name = username = [] ; reply_message = await event.get_reply_message() 
    if not event.reply_to_msg_id or reply_message.media:
       return await rkp.edit("`reply to a user text message`")
    chat = "@SangMataInfo_bot"   
    async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @sangmatainfo_bot and try again`")
              return
          if response.text.startswith("Forward"):
             return await rkp.edit("`Privacy error!`")              
          if response.text.startswith("🔗"):
          	return await rkp.edit("`No name/username history for this user`")   
          if response.text.startswith("Name"):
              name = response.text
              await rkp.edit(f"` Got name history Trying to get username history....` ")
          test = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))         
          response = await test
          if response.text.startswith("Username"):
               username = response.text
               await rkp.edit("` Got username history Trying to give full results....` ")
          return await rkp.edit(f"**User History**\n\n{name}\n\n{username}")
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
        
        

@borg.on(admin_cmd("getid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to text message```")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```nikal gendu```")
              return
          if response.text.startswith("Hello,"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.edit(f"{response.message.message}")

                
                
@borg.on(admin_cmd("mean ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to text message```")
       return
    chat = "@UrbanDictionaryBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=185693644))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```nikal gendu```")
              return
          if response.text.startswith("Hello,"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.edit(f"{response.message.message}")
             
             
             
             
             
             
CMD_HELP.update({
    "bot":
    "`.names <reply to a message>`\
\n**Usage:** Give you uername and name hitory using sangmata bot\
\n\n`.getid <reply to a message>`\
\n**Usage:** Give you uername and name hitory using getidsbot\
\n`.mean <word>`\
\n**Usage:** Show the meaning of word using UrbanDictionaryBot\
"
})

