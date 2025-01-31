from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcademicRecordViewSet, ResearchPaperViewSet, upload_file
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'academic-records', AcademicRecordViewSet)
router.register(r'research-papers', ResearchPaperViewSet)

urlpatterns = [
    path('api/upload/', upload_file, name='upload_file'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 