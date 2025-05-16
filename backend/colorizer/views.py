from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import os
import uuid


@login_required
def colorize_flow_view(request):
   return render(request, 'colorizer/colorize_flow.html')


@login_required
def unsupervised_image_view(request):
   return redirect('colorizer_flow')


@login_required
def unsupervised_video_view(request):
   return redirect('colorizer_flow')


@login_required
def supervised_scribble_view(request):
   return redirect('colorizer_flow')


@login_required
def supervised_color_palette_view(request):
   return redirect('colorizer_flow')


@login_required
def supervised_prompt_view(request):
   return redirect('colorizer_flow')