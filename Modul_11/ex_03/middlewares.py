import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class AddProcessTimeHeader(BaseHTTPMiddleware):
    def __init__(self, app):
        super(AddProcessTimeHeader, self).__init__(app)

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time2"] = str(process_time)
        return response
