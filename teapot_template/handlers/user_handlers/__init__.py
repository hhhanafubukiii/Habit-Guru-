from aiogram import Router
from teapot_template.handlers.user_handlers.user_handlers import router

user_router = Router()
user_router.include_router(router)