from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registros', views.todosRegistros, name="registros"),
    path('cpanel', views.panelControl, name="cpanel"),
    path('cpanel/registros', views.showRegistros, name="registros")
]


from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomLoginForm
#Login
urlpatterns += [
    path('login/', LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]