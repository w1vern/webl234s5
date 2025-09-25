from fastapi import APIRouter

from back.api.auth import AuthController
from back.api.catalog import CatalogController
from back.api.chat import router as chat_router
from back.api.feedback import FeedbackController

router = APIRouter(prefix='/api')
router.include_router(AuthController.create_router())
router.include_router(CatalogController.create_router())
router.include_router(FeedbackController.create_router())
router.include_router(chat_router)
