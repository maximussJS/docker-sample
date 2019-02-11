from aiohttp.web import RouteTableDef, Request, Response


router = RouteTableDef()


@router.get('/')
async def f(request: Request) -> Response:
    print(request.remote)
    return Response(status=200, text='hi maximuss')
