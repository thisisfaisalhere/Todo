from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # api docs
    path('api/docs/', include_docs_urls(title='Todo API')),
    path('api/schema/', get_schema_view(
        title="Todo API",
        description="API for the Todo",
        version="1.0.0"
    ), name='openapi-schema'),

    path('api/users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
