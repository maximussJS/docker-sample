import asyncio
from aiohttp import web
from app import init_app


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        app = loop.run_until_complete(init_app())
        print('Server started')
        web.run_app(app)
        print('Server was stopped')
    except Exception as e:
        print(e)
