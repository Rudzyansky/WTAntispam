from telethon import TelegramClient, events

client: TelegramClient
ids: set


async def init(c: TelegramClient):
    global client, ids
    client = c
    ids = {await client.get_peer_id(i) for i in load_ids()}

    @client.on(events.NewMessage(chats=ids, incoming=True))
    async def handler(event):
        await event.message.mark_read()


async def start():
    [await client.send_read_acknowledge(i) for i in ids]


def load_ids():
    result = []
    try:
        with open(f"reader.txt", encoding="utf-8") as f:
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
