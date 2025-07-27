from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
# Create your views here.

def home(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid(): form.save()
        return redirect('/') 
    form=ImageForm()
    img=Image.objects.all()
    return render(request,'myapp/home.html',{'img':img,'form':form})

def delete_img(request,pk):
    image=get_object_or_404(Image,pk=pk)
    if request.method=='POST':
        image.delete()
        return redirect('/')
    