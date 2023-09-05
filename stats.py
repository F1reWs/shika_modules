#  █▀ ▀ █▀▀▄ █▀▀ █░░░█     █▄░▄█ ▄▀▄ █▀▄ ▄▀▀ 
#  █▀ █ █▐█▀ █▀▀ █░█░█     █░█░█ █░█ █░█ ░▀▄ 
#  ▀░ ▀ ▀░▀▀ ▀▀▀ ░▀░▀░     ▀░░░▀ ░▀░ ▀▀░ ▀▀░ 
#             © F1reW 2023
#        https://t.me/firewmods

from pyrogram import enums
from datetime import datetime
from .. import loader, utils

@loader.module("Stats", "@firewmods")
class StatsMod(loader.Module):
    """Статистика аккаунта"""

    async def stats_cmd(self, app, message):
        """Статистика чатов аккаунта"""
        await utils.answer(message, "<b><emoji id=5326015457155620929>🔄</emoji> Загрузка статистики...</b>")
        start = datetime.now()
        u = 0
        g = 0
        sg = 0
        c = 0
        b = 0
        a_chat = 0
        async for dialog in app.get_dialogs():
          if dialog.chat.type == enums.ChatType.PRIVATE:
              u += 1
          elif dialog.chat.type == enums.ChatType.BOT:
              b += 1
          elif dialog.chat.type == enums.ChatType.GROUP:
              g += 1
          elif dialog.chat.type == enums.ChatType.SUPERGROUP:
              sg += 1
              user_s = await dialog.chat.get_member(int(self.db.get("shika.me", "id")))
              if user_s.status in (
                  enums.ChatMemberStatus.OWNER,
                  enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                 a_chat += 1
          elif dialog.chat.type == enums.ChatType.CHANNEL:
             c += 1

        end = datetime.now()
        ms = (end - start).seconds
        await message.edit(
        """<b><emoji id=5422360266618707867>📊</emoji> Твоя статистика собрана за <code>{}</code> секунд</b>

<b>У тебя <code>{}</code> личных чатов.</b>
<b>У тебя <code>{}</code> приватных чатов.</b>
<b>У тебя <code>{}</code> публичных чатов.</b>
<b>У тебя <code>{}</code> каналов.</b>
<b>У тебя <code>{}</code> чатах.</b>
<b>Чатов с ботами: </b> <code>{}</code>""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )