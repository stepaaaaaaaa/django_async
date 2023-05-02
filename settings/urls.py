from django.contrib import admin
from django.urls import path, include
from main.views import WordAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/main/', WordAPIView.as_view())
]
