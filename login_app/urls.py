from django.urls import path
from login_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name='login_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('user_login/',views.user_login,name='user_login')
]
