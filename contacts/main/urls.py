from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('new',views.new,name='new'),
    path('<int:id>',views.show,name='show'),
path('<int:id> <str:name> <str:seccond_name>',views.update,name='update'),
    path('<int:id> <str:name>',views.remove,name='remove'),
    path('search',views.search,name='search')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)