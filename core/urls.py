from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from main_app.views import  home , blog  , label , posts ,author
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name='home'),
    path('blog/' , blog , name='blog'),
    path('label/<str:label_text>/', label , name='label'),
    path('blog/<int:posts_pk>/', posts , name='post'),
    path('author/<str:name>/' , author,name='author')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
