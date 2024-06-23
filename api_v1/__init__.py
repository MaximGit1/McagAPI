from fastapi import APIRouter
from .products.views import router as product_router
from .teachers.views import router as teacher_router
from .lessons.views import router as lessons_router
from .periods.views import router as period_router
from .groups.views import router as group_router
from .groupDays.views import router as groupDay_router




router = APIRouter()
router.include_router(router=product_router, prefix='/products')
router.include_router(router=teacher_router, prefix='/teachers')
router.include_router(router=lessons_router, prefix='/lessons')
router.include_router(router=period_router, prefix='/period')
router.include_router(router=group_router, prefix='/groups')
router.include_router(router=groupDay_router, prefix='/groups-day')

