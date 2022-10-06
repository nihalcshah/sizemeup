from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
from forms import BodyForm
# Create your views here.
def Home(request):
    return render(request, "index.html", context={})

def Camera(request):
    img = request.P
    print(request.FILES)
    return render(request, "camera.html", context={})