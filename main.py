from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
MONGO_URL = os.environ.get("MONGO_URL", None)

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
