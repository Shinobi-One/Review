from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



# Create your views here.





def thanks(request):
    return render(request,"thank_you.html")

def critic(request):
    if request.method == 'GET':
        return render(request, "critic.html",{'form':UserCreationForm})
    else:
        pass

