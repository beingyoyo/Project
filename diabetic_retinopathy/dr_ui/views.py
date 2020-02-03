from django.shortcuts import render
from .forms import PhotoUploadModelForm
from django.views.generic import ListView, FormView
from .models import ImageUpload
# Create your views here.
class Homepage(FormView):
    form_class = PhotoUploadModelForm
    template_name = 'dr_ui/home.html'
    success_url = '/'
    context_object_name = 'img'

class Uploaded_images(ListView):
    model = ImageUpload
    images = ImageUpload.objects.all
    context_object_name = 'images'
    template_name = 'dr_ui/images_uploaded.html'