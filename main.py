from contextlib import asynccontextmanager

from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings



@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title='@MaximGit1', lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

if __name__ == '__main__':
    import uvicorn

    _host, _port = '127.0.0.1', 4000
    uvicorn.run(
        "main:app",
        host=_host,
        port=_port,
        reload=True,
    )