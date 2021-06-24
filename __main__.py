#!/usr/bin/env python
# encoding=utf-8
import asyncio
import sys
from os import getenv

from telethon import TelegramClient

try:
    # Standalone script WTAntispam.py with folder extensions/
    import extensions
except ImportError:
    try:
        # Running as a module with `python -m WTAntispam` and structure:
        #
        #     WTAntispam/
        #         __main__.py (this file)
        #         extensions/    (cloned)
        from . import extensions
    except ImportError:
        print('could not load the extensions module, does the directory exist '
              'in the correct location?', file=sys.stderr)
        exit(1)


async def main():
    client = TelegramClient('current', int(getenv('API_ID')), getenv('API_HASH'))

    try:
        await extensions.init(client)
        async with client:
            await client.run_until_disconnected()
    finally:
        await client.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
