from django.shortcuts import render
from .forms import ContactFormModel
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page (or the same page)
    else:
        form = ContactFormModel()
        return render(request, 'index.html', {'form': form})

def submit_form(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect back to the main page after submission
    else:
        form = ContactFormModel()

    return render(request, 'your_template.html', {'form': form})