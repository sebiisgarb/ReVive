from django.urls import include, path
from . import views

urlpatterns = [
    path('colorizer/', views.colorize_view, name='colorize'),
    path('accounts/', include('allauth.urls')),
]
