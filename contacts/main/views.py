from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
from django.db.models import Q


def search(request):
    if request.method == "POST":
        value = request.POST['value']
        list = Contact.objects.filter(
            Q(name = value) | Q(seccond_name=value) | Q(third_name=value)
        )
    return render(request, 'main/index.html', {'list': list})
# Create your views here.
def index(request):
    list = Contact.objects.all()
    return render(request,'main/index.html',{'list':list})

def new(request):
    error =''
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = 'Невірні значення'
    form = ContactForm()
    return render(request,'main/new.html',{'form':form,'error':error})

def show(request, id):
    record = Contact.objects.get(id=id)
    return render(request,'main/show.html',{'record':record})
def update(request,id,name,seccond_name):
    error =''
    if request.method == 'POST':
        searchingform = ContactForm(request.POST, request.FILES)
        form = Contact.objects.get(id=id)
        if searchingform.is_valid():
            searchingform1 = searchingform.save(commit=False)
            if not searchingform1.photo:
                searchingform1.photo = form.photo
            form.delete()
            searchingform1.save()
            return redirect(index)
        else:
            error = 'Невірні значення'
    contact = Contact.objects.get(id=id)
    form = ContactForm(initial={'name':contact.name,
                                'seccond_name':contact.seccond_name,
                                'third_name':contact.third_name,
                                'number':contact.number,
                                'photo':contact.photo})

    return render(request,'main/update.html',{'form':form,'error':error,'contact':contact})
def remove(request,id,name):
    record = Contact.objects.get(id=id)
    record.delete()
    return redirect(index)

