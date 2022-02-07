from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚂", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝚂𝚃𝙰𝚃𝚂", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚂", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝙼𝚘𝚗𝚐𝚘𝙳𝙱 𝚂𝚃𝙰𝚃𝚂", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙰𝚂𝙸𝚂𝚃𝙴𝙽 𝚂𝚃𝙰𝚃𝚂", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝙶𝚎𝚗𝚎𝚛𝚊𝚕 𝚂𝚝𝚊𝚝𝚜", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝚂𝚃𝙰𝚃𝚂", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚂", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝙼𝚘𝚗𝚐𝚘𝙳𝙱 𝚂𝚃𝙰𝚃𝚂", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙰𝚂𝙸𝚂𝚃𝙴𝙽 𝚂𝚃𝙰𝚃𝚂", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚂", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝙶𝚎𝚗𝚎𝚛𝚊𝚕 𝚂𝚝𝚊𝚝𝚜", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚂", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝙼𝚘𝚗𝚐𝚘𝙳𝙱 𝚂𝚃𝙰𝚃𝚂", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙰𝚂𝙸𝚂𝚃𝙴𝙽 𝚂𝚃𝙰𝚃𝚂", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="General Stats", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="MongoDB Stats", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot Stats", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="General Stats", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚝𝚊𝚝𝚜", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝚂𝚃𝙰𝚃𝚂", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚂", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝙼𝚘𝚗𝚐𝚘𝙳𝙱 𝚂𝚃𝙰𝚃𝚂", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙶𝚎𝚗𝚎𝚛𝚊𝚕 𝚂𝚝𝚊𝚝𝚜", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="⛔ Loading....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
