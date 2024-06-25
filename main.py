from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api_v1 import router as router_v1
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(app, 'has been started')
    yield


app = FastAPI(title='@MaximGit1', lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get('/', response_class=RedirectResponse, status_code=302)
async def home():
    return '/docs'

if __name__ == '__main__':
    import uvicorn

    _host, _port = '127.0.0.1', 4000
    uvicorn.run(
        "main:app",
        host=_host,
        port=_port,
        reload=True,
    )
