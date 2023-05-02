import asyncio
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class Words:
    async def hello(self):
        await asyncio.sleep(10)
        return "Hello"

    async def world(self):
        await asyncio.sleep(5)
        return "World"

    async def thenia(self):
        await asyncio.sleep(4)
        return "Thenia"

    async def krut(self):
        await asyncio.sleep(7)
        return "Krut"
    

class WordAPIView(APIView):
    def get(self, request: Request) -> Response:
        words = Words()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(asyncio.gather(words.hello(), words.world(), words.thenia(), words.krut()))
        response_data = {
            "results": results
        }
        return Response(response_data)