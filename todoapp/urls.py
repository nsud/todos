from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from tasks.views import cache


urlpatterns = [
    path('', include('tasks.urls', namespace="tasks")),
    path('admin/', admin.site.urls),
    path('date_cache/', cache, name="cache")

]

if not settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns
