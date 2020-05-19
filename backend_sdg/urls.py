
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api/', include('user_api.urls')),
]
