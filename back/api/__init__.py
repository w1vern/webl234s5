from fastapi import APIRouter
from back.api.auth import AuthController
from back.api.catalog import CatalogController


router = APIRouter(prefix='/api')
router.include_router(AuthController.create_router())
router.include_router(CatalogController.create_router())
