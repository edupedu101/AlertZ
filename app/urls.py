from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('cpanel', views.panelControl, name="cpanel"),
    path('cpanel/registros/<int:id_sensor>', views.showRegistros, name="registros"),
    path('cpanel/galeria', views.galeria, name="galeria")
] 


from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomLoginForm
#Login
urlpatterns += [
    path('login/', LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)