from aiogram import Router
from teapot_template.handlers.other_handlers.other_handlers import router

other_router = Router()
other_router.include_router(router)
