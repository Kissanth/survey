from django.shortcuts import render,redirect

# Create your views here.
from .models import survey
#from .forms import surveyform
def home(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        feed = request.POST.get('feedback')
        chaneel= request.POST.get('ch')
        chaneel1= request.POST.get('ch1')
        if survey:
            the=survey(Name=name,Age=age,Email=email,Feedback=feed,)   
            the.save() 
            return redirect('/')   
    return render(request,'index.html')


