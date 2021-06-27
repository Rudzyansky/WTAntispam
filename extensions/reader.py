from os import getenv

from telethon import TelegramClient, events

client: TelegramClient
ids: set


async def init(c: TelegramClient):
    global client, ids
    client = c
    ids = {await client.get_peer_id(i) for i in load_ids()}


async def post_init(modules):
    if getenv('CURRENT_DIALOGS'):
        async with client:
            # noinspection PyUnresolvedReferences
            await modules['printer'].print_dialogs_ids(ids)
            await client.disconnect()
        exit()


async def start():
    @client.on(events.NewMessage(chats=ids, incoming=True))
    async def handler(event):
        await event.message.mark_read()

    [await client.send_read_acknowledge(i) for i in ids]


def load_ids():
    result = []
    try:
        with open(f'reader.txt', encoding='utf-8') as f:
            for line in f:
                i = line.rstrip()
                try:
                    result.append(int(i))
                except ValueError:
                    if len(i) > 0:
                        result.append(i)
    except FileNotFoundError:
        pass
    return result
