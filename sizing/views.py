from django.shortcuts import render, redirect
from django.http import HttpResponse
# import cv2
from .models import Body
from .forms import BodyForm
# import cv2
# from .backend import facialDetection
# from django.http import JsonResponse
# from .TensorFlowModel import bodyDetect
# Create your views here.
def Home(request):
    return render(request, "index.html", context={})

def Calculate(request):
    if request.method == 'POST':
        form = BodyForm(request.POST, request.FILES)
        print("posted")
        if form.is_valid():
            print("dk")
            form.save()
            return redirect('success')
    else:
        form = BodyForm()
    return render(request, "calculate.html", context={'form':form})

# def success(request):
#     filePath = [*Body.objects.all()][-1].bodyImage.url
#     print(filePath)
#     newPath, faceCount = bodyDetect(filePath)
    
#     return JsonResponse({'count': bool(faceCount), 'imgPath':newPath}, safe=False)
#     # return render(request, "results.html", context={'count': bool(faceCount), 'imgPath':newPath})

# def Register(request):
#     return render(request, "register.html")