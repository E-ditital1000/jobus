from django.contrib import admin
from django.urls import path, include
from jobus.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('jobus/', include('jobus.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('resume_cv/', include("resume_cv.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
