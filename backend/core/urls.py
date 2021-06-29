from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .views import root

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # api docs
    path('api/docs/', include_docs_urls(title='MyTodo API')),
    path('api/schema/', get_schema_view(
        title="MyTodo API",
        description="API for the MyTodo",
        version="1.0.0"
    ), name='openapi-schema'),

    # api
    path('api/user/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),

    # test route
    path('', view=root.as_view(), name='root-path')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
