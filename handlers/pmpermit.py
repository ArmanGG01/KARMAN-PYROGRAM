from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto, User
from pyrogram import filters, Client
from pyrogram.types import Message
import re
from helpers.SQL.pmstuff import givepermit, checkpermit, blockuser, getwarns, allallowed, allblocked, inwarns, addwarns
from main import SUDO_USERS as Adminsettings, LOG_GROUP
from handlers.help import *
from main import ALIVE_PIC

Alive_msg = f"👑 𝙺𝙰𝚁𝙼𝙰𝙽-𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 👑 \n\n"
Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
Alive_msg += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
Alive_msg += f"► Rᴇᴘᴏ : [Gɪᴛʜᴜʙ](https://GitHub.com/ArmanGG01/KARMAN-PYROGRAM) \n"
Alive_msg += f"► 𝙶𝚁𝙾𝚄𝙿 : [Jᴏɪɴ.](https://t.me/obrolansuar) \n"
Alive_msg += f"► 𝙲ʜᴀɴɴᴇʟ : [Jᴏɪɴ.](https://t.me/StoryArman) \n"
Alive_msg += f"► **Nᴏᴛᴇ** : 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙻𝙰𝙷 𝙺𝙾𝙽𝚃𝙾𝙻 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙴𝙺 𝙰𝙽𝙰𝙺 𝙷𝙰𝚁𝙰𝙼 𝙸𝙽𝙸 𝙱𝙰𝙻𝙰𝚂 𝙿𝙴𝚂𝙰𝙽 𝙺𝙰𝚄 𝚈𝙰 𝙰𝙽𝙹𝙸𝙽𝙷 \n"
Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"

@Client.on_message(~filters.me & filters.private & ~filters.bot & filters.incoming , group = 69)
async def alive(client: Client, e: Message):
  message = e
  if checkpermit(message.chat.id):
        print("sql is cringe here")
        return
  else:
    print("gotit")
    addwarns(message.chat.id)
    gw= getwarns(message.chat.id)
    teriu= message.from_user
    teriun= teriu.id
    teriuni= str(teriun)
    teriunia="aprv_"+teriuni
    teriunid="decine_"+teriuni
    ids = 0
  if isinstance(gw , str):
      sb= await client.get_me()
      un= LOG_GROUP
  else:
      keyboard= InlineKeyboardMarkup([  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Approve",
                        callback_data=teriunia
                    ),
                    InlineKeyboardButton(
                        "Decline",
                        callback_data=teriunid
                    ),
                ])
      await message.reply_photo(photo=ALIVE_PIC, caption=Alive_msg)
      if gw==3:
        await message.reply_text("You have crossed your warns so die")
        await client.block_user(message.from_user.id)
        blockuser(message.from_user.id)
        return


@Client.on_message(filters.command(["app", "ap", "approve"], ["."]) & filters.me & filters.private)
async def refet(client: Client, message: Message):
    givepermit(message.chat.id)
    await message.edit_text("the user has been approved!!")
    
     
@Client.on_message(filters.command(["dapp", "dap", "dapprove", "disapprove", "dp"], ["."]) & filters.me & filters.private)
async def refes(client: Client, message: Message):
    await message.edit_text("the user has been blocked!!")
    blockuser(message.chat.id)
    await client.block_user(message.chat.id)
    
@Client.on_message(filters.command(["allpermitted", "approvedlist"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allallowed()
  strr ="Following are the users allowed"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["allblocked"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allblocked()
  strr ="Following are the users blocked"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["nonpermitted"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = inwarns()
  strr ="Following are the users not allowed"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)


add_command_help(
    "private",
    [
        [
            ".ap",
            "To Approve A User in Your Pm",
        ],
        [
            ".dap",
            "To Disapprove/Block A User in Your Pm",
        ],
        [
            ".approvedlist",
            "Get approved Users list",
        ],
        [
            ".allblocked",
            "Get blocked list",
        ],
        [
            ".nonpermitted",
            "non permitted list",
        ],
    ],
)
