from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import person

# Create your views here.
def index(request):
    # return HttpResponse("<h1>KS Pias</h1>")
    # return render(request,"index.html")
    # name = "Pias"
    # age = 32
    # if age >= 30:
    #     message = "คุณไม่เด็กแล้วนะ"
    # else:
    #     message = "คุณยังเป็นเด็กอยู่"
    
    # return render(request,"index.html",{"name":name,"age":age,"message":message})
    all_person = person.objects.all()
    # all_person = person.objects.filter(age=31)
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    # return HttpResponse("<h1>เกี่ยวกับเรา</h1>")
    return render(request,"about.html")

def form(request):
    # return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1>")
    return render(request,"form.html")