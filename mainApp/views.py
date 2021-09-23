from django.conf.urls import handler403
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import GroceryAddItemForm
from .models import GroceryItems
from django.contrib import messages

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        dateclicked = request.POST.get('dateClicked')
        filtereditems = GroceryItems.objects.filter(owner=request.user,dateAdded=dateclicked)
        if len(filtereditems) == 0:
            messages.warning(request,f'No items in the Grocery list on Date : {dateclicked}.Please Click on Grocery Bag logo')
        context = {'items':filtereditems}
        return render(request,'mainApp/index.html',context)
    items = GroceryItems.objects.filter(owner=request.user)
    context = {'items':items}
    return render(request,'mainApp/index.html',context)

@login_required(login_url='login')
def add_view(request):
    form = GroceryAddItemForm()
    if request.method == 'POST':
        form = GroceryAddItemForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
            messages.success(request,'New Item Added')
            return redirect('index')
    context = {'addform':form}
    return render(request,'mainApp/add.html',context)

@login_required(login_url='login')
def update_view(request,id_num):
    item = GroceryItems.objects.get(id=id_num)
    updateform = GroceryAddItemForm(instance=item)
    context = {'item':updateform}
    if request.method == 'POST':
        form = GroceryAddItemForm(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'mainApp/update.html',context)

@login_required(login_url='login')
def delete_view(request,id_num):
    obj = GroceryItems.objects.get(id=id_num)
    if obj.owner == request.user:
        obj.delete()
    return redirect('index')