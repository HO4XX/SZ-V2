# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
from datetime import datetime

from userge import Message, userge


@userge.on_cmd(
    "ping",
    about={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
    },
    group=-1,
)
async def pingme(message: Message):
    start = datetime.now()
    if "-a" in message.flags:
        await message.edit("`!....`")
        await asyncio.sleep(0.3)
        await message.edit("`..!..`")
        await asyncio.sleep(0.3)
        await message.edit("`....!`")
        end = datetime.now()
        t_m_s = (end - start).microseconds / 1000
        m_s = round((t_m_s - 0.6) / 3, 3)
        await message.edit(f"**SCUMZ♦️[𝙊𝙉𝙇𝙄𝙉𝙀]♦️SCUMZ**\n\n**LAST UPDATED: 9:33 AM (GMT)**\n\n_________\nSay **!commands**\n\n\n\n****MAIN GROUP/CHANNEL:\nhttps://t.me/NiceneCreed \n\nhttps://t.me/seven6four****")
    else:
        await message.edit("`STATUS:`")
        end = datetime.now()
        m_s = (end - start).microseconds / 1000
        await message.edit(f"**SCUMZ♦️[𝙊𝙉𝙇𝙄𝙉𝙀]♦️SCUMZ**\n\n**LAST UPDATED: 9:33 AM (GMT)**\n\n_________\nSay **!commands**\n\n\n\n****MAIN GROUP/CHANNEL:\nhttps://t.me/NiceneCreed \n\nhttps://t.me/seven6four****")
