from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Post

from .forms import ContactForm

def Index(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'Index.html', {'posts': posts})
    

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def contact_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Use the form, not the model
        if form.is_valid():  # Validate the form
            form.save()  # Save the form data into the Contact model
            
            return redirect('index')  # Redirect to the contact page after successful submission
        else:
            print("Form is invalid", form.errors)  # Debugging line to see form validation errors
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




