from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def homepage(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['images']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, "dr_ui/navbaritems.html", context)

