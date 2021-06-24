from os import getenv

from telethon import TelegramClient

from . import filter
from . import printer
from . import reader


# modules = []
# for name, path in {basename(f)[:-3]: f for f in glob.glob(join(dirname(__file__), "*.py")) if
#                    isfile(f) and not f.endswith('__init__.py')}.items():
#     spec = importlib.util.spec_from_file_location(name, path)
#     module = importlib.util.module_from_spec(spec)
#     sys.modules[name] = module
#     spec.loader.exec_module(module)
#     modules.append(module)


async def init(client: TelegramClient):
    await printer.init(client)
    await reader.init(client)
    await filter.init(client)

    if getenv('SHOW_DIALOGS'):
        async with client:
            await printer.print_dialogs()
            await client.disconnect()
        exit()

    if getenv('CURRENT_DIALOGS'):
        async with client:
            await printer.print_dialogs_ids({await client.get_peer_id(i) for i in reader.load_ids()})
            await client.disconnect()
        exit()

    async with client:
        await reader.start()
