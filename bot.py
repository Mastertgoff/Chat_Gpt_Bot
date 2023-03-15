from os import environ
from pyrogram import idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from urllib import response
import openai

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
OPEN_AI_KEY = environ.get("OPEN_AI_KEY")
START_MSG = "Hi {} Iam Artificially Intelligente Bot Maded By @MLZ_BOTZ Ask Me Anything I will Give Answers Properly"

Client = Client(name="chat-gpt",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url="https://t.me/MLZ_BOTZ"),
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/MLZ_BOTZ_SUPPORT")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        text=START_MSG.format(message.from_user.mention),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
    )
    
        
def ai_responses(input_text):
    user_message = str(input_text).lower()
    prompt_addition = "ENTER YOUR PROMPT HERE" + user_message
    openai.api_key = OPEN_AI_KEY
    bot_output = openai.Completion.create(engine="text-davinci-002",prompt=prompt_addition,temperature=0.7,max_tokens=200,top_p=1,frequency_penalty=0,presence_penalty=0)
    response = bot_output['choices'][0]['text']
    return response
  
@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    query = message.text
    response = ai_responses(query)
    await message.reply_text(response)

Client.start()
print("Bot Started!")

idle()

Client.stop()
print("Bot Stopped!")


    
  
