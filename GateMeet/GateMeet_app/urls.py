from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .views import dashboard
from django.contrib.auth.views import LoginView
from .views import logout_view

urlpatterns = [
    path('register/', views.register, name='register'),
     path('login/', LoginView.as_view(template_name='login.html'), name='login'),  
    path('credit/', views.credit_view, name='credit'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('meeting/', views.GateMeet, name='meeting'),
    path('join/', views.join_room, name='join'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)