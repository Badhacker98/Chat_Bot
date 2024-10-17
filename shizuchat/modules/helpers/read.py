from config import OWNER_USERNAME, SUPPORT_GRP
from shizuchat import shizuchat
from pyrogram import Client, filters



START = """**
{} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 💞

 ➪ ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ:
┏━━━━━━━━━━━━━━━┓
┃ ➤ ꜱᴜᴘᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
┃ ➤ ᴍᴜʟᴛɪ-ʟᴀɴɢ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
┃ ➤ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot
┗━━━━━━━━━━━━━━━┛

┏━━━━━•❃°•°❀•━━━━━┓
┣⪼ ๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {}
┣⪼ ๏ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {}
┗━━━━━•❃°•°❀•━━━━━┛

╔═══════════════╗
 ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/Badhacker98/Chat_Bot/fork)
 ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll)
╚═══════════════╝
**"""

ADMIN = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {shizuchat.mention}:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏns ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
📡 ᴍᴀᴅᴇ ʙʏ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll) 💞**
"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/THE_VIP_BOY).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

TOOLS_DATA_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {shizuchat.mention}:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\nᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ ᴜsᴇ /repo ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ ᴜsᴇ /emoji /love ᴛᴇxᴛ ᴛᴏ ᴇᴍᴏᴊɪ.
──────────────
➻ ᴜsᴇ /afk <text> ɢɪᴠᴇꜱ ᴀᴜᴛᴏ ʀᴇᴘʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʀᴇ ᴏꜰꜰʟɪɴᴇ
──────────────
➻ ᴜsᴇ /brb <text> ɢɪᴠᴇꜱ ᴀᴜᴛᴏ ʀᴇᴘʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʀᴇ ᴏꜰꜰʟɪɴᴇ
──────────────
๏ ᴍᴀᴅᴇ ʙʏ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll) 💞**
"""

AIBOT_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {shizuchat.mention}:

➻ ᴜsᴇ /ai - ɪ ᴀsᴋ ᴀɴʏ ǫᴜᴇᴅᴛɪᴏɴ .
──────────────
➻ ᴜsᴇ /gemini - ɪ ᴀsᴋ ᴀɴʏ ǫᴜᴇᴅᴛɪᴏɴ .
──────────────
➻ ᴜsᴇ /bard ᴡʀɪᴛᴇ ꜱʜᴏʀᴛꜱ ɴᴏᴛᴇꜱ ᴏɴ ʜᴜᴍᴀɴ ᴇʏᴇꜱ
──────────────
➻ ᴜsᴇ /blackbox ᴡʀɪᴛᴇ ꜱɪᴍᴘʟᴇ ꜰʟᴀꜱᴋ ᴀᴘᴘ ᴄᴏᴅᴇ
──────────────
📡 ᴍᴀᴅᴇ ʙʏ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll) 💞**
"""

CHATBOT_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {shizuchat.mention}:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏns ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
📡 ᴍᴀᴅᴇ ʙʏ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll) 💞**
"""

SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{shizuchat.name}](https://t.me/{shizuchat.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n**──────────────────**\n**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/Badhacker98/Chat_Bot/frok)**\n**──────────────────**\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP}).\n<b>||©️ @{OWNER_USERNAME}||</b>"

ADMIN_READ2 = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {shizuchat.mention}:

➻ ᴜsᴇ /purge [n] - ᴘᴜʀɢᴇ "ɴ" ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰʀᴏᴍ ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ .
──────────────
➻ ᴜsᴇ /del - ᴅᴇʟᴇᴛᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ .
──────────────
➻ ᴜsᴇ /promote - ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ .
──────────────
➻ ᴜsᴇ /fullpromote - ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ᴡɪᴛʜ ᴀʟʟ ʀɪɢʜᴛꜱ .
──────────────
➻ ᴜsᴇ /demote - ᴅᴇᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ .
──────────────
➻ ᴜsᴇ /pin - ᴘɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ .
──────────────
➻ ᴜsᴇ /unpin - ᴜɴᴘɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ .
──────────────
➻ ᴜsᴇ /unpinall - ᴜɴᴘɪɴᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ .
──────────────
➻ ᴜsᴇ /mute - ᴍᴜᴛᴇ ᴀ ᴜꜱᴇʀ .
──────────────
➻ ᴜsᴇ /tmute - ᴍᴜᴛᴇ ᴀ ᴜꜱᴇʀ ꜰᴏʀ ꜱᴘᴇᴄɪꜰɪᴄ ᴛɪᴍᴇ.
──────────────
➻ ᴜsᴇ /unmute - ᴜɴᴍᴜᴛᴇ ᴀ ᴜꜱᴇʀ .
──────────────
๏ ᴍᴀᴅᴇ ʙʏ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll) 💞**
"""

ADMIN_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {shizuchat.mention}:

➻ ᴜsᴇ /ban - Ban A User
──────────────
➻ ᴜsᴇ /sban - Delete all messages of user that sended in group and ban the user
──────────────
➻ ᴜsᴇ /tban - Ban A User For Specific Time
──────────────
➻ ᴜsᴇ /unban - Unban A User
──────────────
➻ ᴜsᴇ /warn - Warn A User
──────────────
➻ ᴜsᴇ /swarn - Delete all the message sended in group and warn the user
──────────────
➻ ᴜsᴇ /rmwarns - Remove All Warning of A User
──────────────
➻ ᴜsᴇ /warns - Show Warning Of A User
──────────────
๏ ᴍᴀᴅᴇ ʙʏ ➪ [ʙᴀᴅ ✯ ᴍᴜɴᴅᴀ](https://t.me/ll_BAD_MUNDA_ll) 💞**
"""

ABOUT_READ = f"""
**➻ [{shizuchat.name}](https://t.me/{shizuchat.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{shizuchat.name}](https://t.me/{shizuchat.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{shizuchat.name}](https://t.me/{shizuchat.username})**
"""
