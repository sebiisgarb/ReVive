from django.urls import include, path
from . import views

urlpatterns = [
    path('colorizer/flow/', views.colorize_flow_view, name='colorizer_flow'),

    #supervised options
    path('colorized/supervised/scribble/', views.supervised_scribble_view, name='supervised_scribble'),
    path('colorized/supervised/color_palette/', views.supervised_color_palette_view, name='supervised_color_palette'),
    path('colorized/supervised/prompt/', views.supervised_prompt_view, name='supervised_prompt'),

    #unsupervised options
    path('colorized/unsupervised/image/', views.unsupervised_image_view, name='unsupervised_image'),
    path('colorized/unsupervised/video/', views.unsupervised_video_view, name='unsupervised_video'),

    path('accounts/', include('allauth.urls')),
]
