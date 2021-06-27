import importlib.util
from glob import glob
from os.path import basename, join, dirname, isfile

from telethon import TelegramClient

modules = {}
for name, path in {basename(f)[:-3]: f for f in glob(join(dirname(__file__), '*.py')) if
                   isfile(f) and not f.endswith('__init__.py')}.items():
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    modules[name] = module
    # noinspection PyUnresolvedReferences
    spec.loader.exec_module(module)


# noinspection PyUnresolvedReferences
async def init(client: TelegramClient):
    for m in modules.values():
        await m.init(client)

    for m in modules.values():
        await m.post_init(modules)

    async with client:
        for m in modules.values():
            await m.start()
