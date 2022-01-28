import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/9e95d6f3e8eeaa4ae4ea8.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  Hori san = "**Holla I'm hori san!** \n\n"
  Hori san += "×**I'm Working Properly** \n\n"
  Hori san += "×**My Owner : [VOID](https://t.me/voidxtoxic)** \n\n"
  Hori san += f"×**Telethon Version : {tlhver}** \n\n"
  Hori san += f"×**Pyrogram Version : {pyrover}** \n\n"
  Hori san += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/horisan_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Hori san,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  Hori San = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Hori san,  buttons=BUTTON)
