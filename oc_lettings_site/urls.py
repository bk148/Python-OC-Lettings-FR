from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


app_name = 'c_lettings_site'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),

]
