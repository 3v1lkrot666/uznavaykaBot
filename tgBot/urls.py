from tgBots import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('delete/<int:user_id>/<int:work_id>', views.deleteInt, name = 'delete'),
    
]
