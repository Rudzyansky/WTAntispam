import json
import re

from telethon import TelegramClient, events

client: TelegramClient
assoc = {}
cache = {}


async def init(c: TelegramClient):
    global client, assoc, cache
    client = c

    # Load Assoc
    try:
        with open("filters.json", encoding="utf-8") as f:
            assoc = {int(k): frozenset(set(v)) for k, v in json.load(f).items()}
    except FileNotFoundError:
        return

    # Load Filters
    filters = {}
    for key in {item for sublist in assoc.values() for item in sublist}:
        try:
            with open(f"filters/{key}.txt", encoding="utf-8") as f:
                filters[key] = {line.rstrip() for line in f}
        except FileNotFoundError:
            filters[key] = set()

    # Cache
    cache = {uniq: "(" + "|".join({w for u in uniq for w in filters[u]}) + ")" for uniq in assoc.values()}

    # Handler
    @client.on(events.NewMessage(chats=list(assoc.keys()), incoming=True))
    async def handler(event):
        if re.search(cache[assoc[event.message.chat_id]], event.message.text, re.IGNORECASE) is not None:
            await client.delete_messages(event.message.chat_id, event.message.id)
