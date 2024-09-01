from aiogram import Router
from .user_handlers import user_router
from .other_handlers import other_router
from .admin_handlers import admin_router

main_router = Router()
main_router.include_router(user_router)
main_router.include_router(other_router)
main_router.include_router(admin_router)