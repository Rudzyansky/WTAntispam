import importlib.util
from glob import glob
from inspect import signature
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


async def exec_func(mod, f_name, *args, **kwargs):
    if hasattr(mod, f_name):
        func = getattr(mod, f_name)
        if len(signature(func).parameters):
            await func(*args, **kwargs)
        else:
            await func()


async def init(client: TelegramClient):
    for m in modules.values():
        await exec_func(m, 'init', client)

    for m in modules.values():
        await exec_func(m, 'post_init', modules)

    async with client:
        for m in modules.values():
            await exec_func(m, 'start')
