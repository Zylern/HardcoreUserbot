import os
import asyncio
from getpass import getuser
from os import remove
from subprocess import PIPE
from subprocess import run as runapp
import pybase64
from telethon import events
from sys import executable
from userbot.utils import register
from userbot.utils import admin_cmd
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID
from userbot.events import  bot
from userbot import CMD_HELP, ALIVE_NAME

FULL_SUDO = os.environ.get("FULL_SUDO", None)
import inspect
running_processes: dict = {}


@register(outgoing=True, pattern="^\.term(?: |$|\n)([\s\S]*)")
async def evaluate(event):  
    await event.edit(f"`Running Terminal.....`")
    message = (str(event.chat_id) + ':' + str(event.message.id))
    if running_processes.get(message, False):
        await event.edit("A process for this event is already running.")
        return
    cmd = event.pattern_match.group(1).strip()    
    if not cmd:
        await event.edit("``` Give a command or use .help script.```")
        return
    if cmd in ("userbot.session", "env", "printenv"):
        return await event.edit(f"**Privacy Error, This command not permitted**")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    running_processes.update({message: process})
    stdout, stderr = await process.communicate()
    not_killed = running_processes.get(message, False)
    if not_killed:
        del running_processes[message]    
    text = f"**Terminal Command**: `{cmd}`\n**Return code**: `{process.returncode}`\n\n"
    if stdout:    	
        text += "\n**[stdout]**\n`" + stdout.decode("UTF-8").strip() + "\n`"
    if stderr:
        text += "\n**[stderr]**\n`" + stderr.decode('UTF-8').strip() + "\n`"   
    if stdout or stderr:
    	if not len(text) > 4096:    
            return await event.edit(text)  
    output = open("term.txt", "w+")
    output.write(text)
    output.close()
    await event.client.send_file(event.chat_id, "term.txt", reply_to=event.id, caption=f"`{JAVES_NNAME}:` **Output too large, sending as file**")
    os.remove("term.txt")           
    return
        
              
        
@borg.on(admin_cmd(pattern=f"term(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def evaluate(event):  
  if not FULL_SUDO:
      await query.reply(f"**Sorry , Normal Sudo cant acess this comand,  active advance sudo by set  FULL_SUDO as true in heroku var**") 
  else:
    rkp = await event.reply(f"`Running Terminal.....`")
    message = (str(event.chat_id) + ':' + str(event.message.id))
    if running_processes.get(message, False):
        await rkp.edit("A process for this event is already running.")
        return
    cmd = event.pattern_match.group(1).strip()
    if not cmd:
        await rkp.edit("``` Give a command or use .help script.```")
        return
    if cmd in ("userbot.session", "env", "printenv"):
        return await rkp.edit(f"**Privacy Error, This command not permitted**")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    running_processes.update({message: process})
    stdout, stderr = await process.communicate()
    not_killed = running_processes.get(message, False)
    if not_killed:
        del running_processes[message]    
    text = f"**Terminal Command**: `{cmd}`\n**Return code**: `{process.returncode}`\n\n"
    if stdout:    	
        text += "\n**[stdout]**\n`" + stdout.decode("UTF-8").strip() + "\n`"
    if stderr:
        text += "\n**[stderr]**\n`" + stderr.decode('UTF-8').strip() + "\n`"   
    if stdout or stderr:
    	if not len(text) > 4096:    
            return await rkp.edit(text)  
    output = open("term.txt", "w+")
    output.write(text)
    output.close()
    await event.client.send_file(event.chat_id, "term.txt", reply_to=event.id, caption=f"`{JAVES_NNAME}:` **Output too large, sending as file**")
    os.remove("term.txt")           
    return
        
              
        



@register(outgoing=True, pattern="^\.hash (.*)")
async def gethash(hash_q):
    hashtxt_ = hash_q.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = ("Text: `" + hashtxt_ + "`\nMD5: `" + md5 + "`SHA1: `" + sha1 +
           "`SHA256: `" + sha256 + "`SHA512: `" + sha512[:-1] + "`")
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `")
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)



@borg.on(admin_cmd(pattern=f"base64 (en|de) (.*)", allow_sudo=True))
async def endecrypt(query):
    if query.pattern_match.group(1) == "en":
        lething = str(
            pybase64.b64encode(bytes(query.pattern_match.group(2),
                                     "utf-8")))[2:]
        await query.reply("Encoded: `" + lething[:-1] + "`")
    else:
        lething = str(
            pybase64.b64decode(bytes(query.pattern_match.group(2), "utf-8"),
                               validate=True))[2:]
        await query.reply("Decoded: `" + lething[:-1] + "`")



CMD_HELP.update({
    "script":
    ".term\
\nUsage: run  shell command in javes, Javes's os is alpine so use apline commands like .term apk add < packges>\
\n\n.hash\
\nUsage: find the md5, sha1, sha256, sha512 of the string.\
\n\n.base64 en/de\
\nUsage: find the base64 encode/decode  the given string.  like .base64 en hello\
"
})






    