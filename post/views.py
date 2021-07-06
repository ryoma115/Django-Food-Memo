from django.db.models import Q
from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Post
 

def home(request):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.all()
        posts = posts.filter(
            Q(store_name__icontains=query)|
            Q(where__icontains=query)|
            Q(food_category__icontains=query)|
            Q(description__icontains=query)|
            Q(posted_at__icontains=query)
            ).distinct()
    else:
        posts = Post.objects.all()  
    return render(request, 'post/list.html', {'posts': posts, 'query': query})
            

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
        obj = Post.objects.all()
    return render(request, 'post/upload.html', {
        'form': form,
        'obj': obj
    })
