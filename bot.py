from os import environ
from pyrogram import idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")

START_MSG = "Hi Iam Artificially Intelligente Bot Maded By @MLZ_BOTZ Ask Me Anything I will Give Answers Properly"

Client = Client(name="chat-gpt",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton('Oᴡɴᴇʀ', user_id='1957296068'),
        InlineKeyboardButton('Gʀᴏᴜᴘ', url='https://t.me/MaSTeR_filims')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        text=START_MSG.format(message.from_user.mention),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
    )
    
        
