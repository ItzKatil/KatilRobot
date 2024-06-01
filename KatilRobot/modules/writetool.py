import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from KatilRobot import BOT_NAME, BOT_USERNAME
from KatilRobot import pbot as Katil


@Katil.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
    else:
        text = message.reply_to_message.text

    m = await Katil.send_message(
        message.chat.id, "`Please wait...,\n\nWriting your text...`"
    )

    try:
        api_url = f"https://api.safone.me/write?text={text}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = response.content

        caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
        await m.delete()
        await Katil.send_photo(
            message.chat.id,
            photo=image_data,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=api_url)]]
            ),
        )

    except requests.exceptions.HTTPError as http_err:
        await Katil.send_message(message.chat.id, f"HTTP error occurred: {http_err}")
    except Exception as e:
        await Katil.send_message(message.chat.id, f"An error occurred: {e}")


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__help__ = """
 ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.

☆............𝙱𝚈 » [Katil](https://t.me/Itz_Kaatil)............☆
"""
