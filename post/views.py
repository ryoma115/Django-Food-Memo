from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Post
 

def home(request):
    obj = Post.objects.all()
    return render(request, 'post/list.html', {'obj': obj})

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     if 'query' in self.request.GET:
    #         qs = self.requset.GET['query']
    #         queryset = QuerySet.filter(name__contains=qs)
    #         return queryset

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post/home.html')
    else:
        form = DocumentForm()
        obj = Post.objects.all()
    return render(request, 'post/upload.html', {
        'form': form,
        'obj': obj
    })
