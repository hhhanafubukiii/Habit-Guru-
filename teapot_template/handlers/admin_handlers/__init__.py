from aiogram import Router
from teapot_template.handlers.admin_handlers.admin_handlers import router

admin_router = Router()
admin_router.include_router(router)