from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
def index(request): return render(request,"index.html",{"contacts":Contact.objects.all()})
def add_contact(request):
 if request.method=="POST":
  name=request.POST.get("name","").strip(); phone=request.POST.get("phone","").strip(); email=request.POST.get("email","").strip()
  if name and phone: Contact.objects.create(name=name,phone=phone,email=email)
 return redirect("index")
def delete_contact(request,pk): get_object_or_404(Contact,pk=pk).delete(); return redirect("index")
