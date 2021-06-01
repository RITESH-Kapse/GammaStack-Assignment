from django.shortcuts import render , HttpResponse, redirect
from sampletask import models
from sampletask.models import Data
import time
from django.contrib import messages

# Create your views here.
 
def hello(request):
    if request.method == "POST":
        data = request.POST['textfield']
        print(data)
        ins = Data(data = data)

        messages.info(request,'Data is successfully saved !')
        
        time.sleep(10)

        if ins.save():
            messages.info(request,'Data is successfully saved AFTER DELAY!')
				return redirect('/')


    return render(request,'sampletask/main.html')

    
