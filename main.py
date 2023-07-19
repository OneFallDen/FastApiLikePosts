from fastapi import FastAPI

from routers import post_router, reg_router

app = FastAPI()


app.include_router(post_router.router)
app.include_router(reg_router.router)
