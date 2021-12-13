from django.urls import include, path
from .import views

app_name= 'login_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('createuser/', views.reg_user, name='reg_user')
]
