from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = AddForm()
    
    return render(request, 'mycontacts/add.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        form = AddForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = AddForm(instance=contact)
    
    return render(request, 'mycontacts/edit.html', {'form': form, 'contact': contact})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('show')

