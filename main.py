from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re

API_ID = os.environ.get("18654447", None)
API_HASH = os.environ.get("60ac6f65c766e73dfcc1debef93d06bc", None)
BOT_TOKEN = os.environ.get("5058249365:AAEDyTkMrE9xWifvAgxjdHJ6c4qaGycfl3M", None)
MONGO_URL = os.environ.get("mongodb+srv://abc:abcd@cluster0.r9241sb.mongodb.net/?retryWrites=true&w=majority", None)

bot = Client(
    "VickBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(chat_id, filter="administrators")
    ]

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hi! My name is Ishi. I'm an Artificial Intelligence\n /chatbot - [on|off]")

# Add other command handlers here

@bot.on_message(
    filters.text
    & ~filters.private
    & ~filters.bot
)
async def vickai(client: Client, message: Message):
    # Add your code logic here

@bot.on_message(
    filters.sticker
    & ~filters.private
    & ~filters.bot
)
   async def vickstickerai(client: Client, message: Message):
    # Add your code logic here

@bot.on_message(
    filters.text
    & filters.private
    & ~filters.bot
)
async def vickprivate(client: Client, message: Message):
    # Add your code logic here

@bot.on_message(
    filters.sticker
    & filters.private
    & ~filters.bot
)
async def vickprivatesticker(client: Client, message: Message):
    # Add your code logic here

bot.run()
