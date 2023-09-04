#  █▀ ▀ █▀▀▄ █▀▀ █░░░█     █▄░▄█ ▄▀▄ █▀▄ ▄▀▀ 
#  █▀ █ █▐█▀ █▀▀ █░█░█     █░█░█ █░█ █░█ ░▀▄ 
#  ▀░ ▀ ▀░▀▀ ▀▀▀ ░▀░▀░     ▀░░░▀ ░▀░ ▀▀░ ▀▀░ 
#             © F1reW 2023
#        https://t.me/firewmods

import os
import qrcode
from .. import loader

@loader.module("QRcode", "@firewmods")
class QRcodeMod(loader.Module):
    """Делает QRcode"""

    async def qrcode_cmd(self, app, message):
        """Создание qrcode"""
        await message.edit("<b><emoji id=5325731315004218660>🔄</emoji> Создание QRcode...</b>")
        app.me = await app.get_me()
        try:
            txt = message.text.split(" ")[1]
        except:
            prefix = self.db.get("shika.loader", "prefixes", ["."])[0]
            return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}qrcode [text]</code></b>")

        img = qrcode.make(txt)
        img.save('assets/code.png')

        with open('assets/code.png', 'rb') as photo:
           await app.send_photo(message.chat.id, photo, caption=f"<b>Ваш QRcode с текстом <code>{txt}</code> создан</b>")
           return await message.delete()