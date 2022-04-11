from django.shortcuts import render, redirect
from  .forms import *

# Create your views here.




def checkout(request):
    if request.method == 'POST':
        form = Managmentforms(request.POST)
        if form.is_valid():
            form.save()
         
    else:
        form = Managmentforms()

    context = {
        'form': form
    }
    return render(request, 'page/index.html', context)



def Home(request,):
    som = Managment.objects.all()[::-1]
    context = {'som':som,}
    return render(request,'page/line.html', context)
    
  