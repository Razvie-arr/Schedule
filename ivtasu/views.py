from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import string
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
def zan_list(request, id=None):
    if request.method == "POST":
        f = ZanyatiaForm(request.POST)
        if f.is_valid():
            ed = f.save(commit=False)
            ed.id = id if id else None
            ed.save()
            return redirect('zan_list')
    if id:
        form = ZanyatiaForm(instance=Zanyatia.objects.get(pk=id))
    else:
        form = ZanyatiaForm()
    perem = Zanyatia.objects.all()

    return render(request, 'ivtasu/base.html', locals())


# def zan_edit(request, id=None):
#     if request.method == "POST":
#         form = ZanyatiaForm(request.POST)
#         if form.is_valid():
#             ed = form.save(commit=False)
#             ed.id = id if id else None
#             ed.save()
#             return redirect('zan_list')
#     else:
#         form = ZanyatiaForm(instance=Zanyatia.objects.get(pk=id))
#     return render(request, 'ivtasu/zan_edit.html', {'form': form})
def raspis(request, id=None):
    if request.method == "POST":
        form = DaysForm(request.POST)
        perem = Days.objects.all().order_by('day')
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('raspis')
        else:
            return render(request, 'ivtasu/raspis.html', locals())
    form = DaysForm()
    perem = Days.objects.all().order_by('day')
    dni = Days.MndSun
    dnidict = dict(dni)

    mon = Days.objects.filter(day=0)

    tue = Days.objects.filter(day=1)
    
    wed = Days.objects.filter(day=2)

    thu = Days.objects.filter(day=3)
    
    fri = Days.objects.filter(day=4)

    sat = Days.objects.filter(day=5)

    sun = Days.objects.filter(day=6)
    return render(request, 'ivtasu/raspis.html', locals())



def raspis_edit(request, id):
    #res = get_object_or_404(Days, id)
    if request.method == "POST":
        form = DaysForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.id = id if id else None
            res.save()
            return redirect('raspis')
    else:
        form = DaysForm(instance=Days.objects.get(pk=id))
        perem = Days.objects.all().order_by('day')
        return render(request, 'ivtasu/raspis.html', locals())
def raspis_delete(requesit,id):
    Days.objects.filter(pk=id).delete()
    return redirect('raspis')