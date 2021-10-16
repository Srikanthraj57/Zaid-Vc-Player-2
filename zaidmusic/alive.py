#zaid Project 
#Ur Motherfucker If U Kang And Don't Give Creadits 🥴

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cbd81c831318fb65603b8.jpg",
        caption=f"""**➮𝐳 ʜɪɪ ɪ ᴍ [Sriki Music bot}](https://t.me/Sriki_Vcmusic_bot)**

➮ Sriki Sყʂƚҽɱ Wσɾƙιɳɠ Fιɳҽ

➮ Sriki ᴠᴇʀꜱɪᴏɴ : 5.0 Lҽƚҽʂƚ

➮ ᴍʏ ᴏᴡɴᴇʀ : [Srikanth](https://t.me/Srikanth_36)

➮ **ꜱᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ : {uptime}**

𝚃𝚑𝚊𝚗𝚔𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝚣𝚊𝚒𝚍 𝙱𝚘𝚝𝚜 ♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫🆂🆄🅿🅿🅾🆁🆃 ", url=f"https://t.me/we_all_are_best_friends"
                    ),
                    InlineKeyboardButton(
                        "🅲🅷🅰🅽🅽🅴🅻 ☑️", url=f"https://t.me/legend_friends_Updates"
                    )
                ]
            ]
        )
    )
