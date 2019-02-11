from aiohttp.web import Application
from aiohttp_cors import ResourceOptions, setup as cors_setup
from router import router


async def init_app() -> Application:
    app = Application()
    app.add_routes(router)
    cors = cors_setup(app, defaults={
        '*': ResourceOptions(
            allow_credentials=True,
            expose_headers=('Content-Type', 'Access-Control-Allow-Origin'),
            allow_headers=('Content-Type', 'Access-Control-Allow-Origin', 'Authorization'),
            allow_methods="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    return app
