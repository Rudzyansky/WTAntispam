from telethon import TelegramClient
from telethon.tl.types import User, Chat, Channel

client: TelegramClient


async def init(c: TelegramClient):
    global client
    client = c


async def print_dialogs():
    print_header()
    [print_dialog(i.id, i.entity) async for i in client.iter_dialogs()]


async def print_dialogs_ids(ids):
    print_header()
    [print_dialog(i, await client.get_entity(i)) for i in ids]


def print_header():
    print(f'[Type] [         ID] [Username                        ] Title')
    print(f'-------------------------------------------------------------')


def print_dialog(i, e):
    p = "U" if type(e) is User else "C" if type(e) is Channel and not e.megagroup else \
        "S" if type(e) is Channel and e.megagroup else "G" if type(e) is Chat else " "
    un = "" + e.username if hasattr(e, "username") and e.username is not None else ""
    t = ("" if e.first_name is None else e.first_name) + ("" if e.last_name is None else " " + e.last_name) \
        if type(e) is User else e.title
    print(f'[{p}] [{i:14}] [{un:32}] {t}')
