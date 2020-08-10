from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),

    path('customer/', views.customer, name='customer'),

    path('customer/<int:customer_id>/', views.detail, name='detail'),

    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logoutuser'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
