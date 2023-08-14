from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import Movieform
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# def home(request):
#     p=Movie.objects.all()
#     return render(request,'home.html',{'movie':p})
class Movielistview(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie_list"


# def viewmovie(request,p):
#     b=Movie.objects.get(id=p)
#     return render(request,'moviedetails.html',{'b':b})

class Detailview(DetailView):
    model=Movie
    template_name="moviedetails.html"
    context_object_name="movie"

# def addmovie(request):
#     if (request.method == "POST"):
#         n = request.POST['n']
#         d = request.POST['d']
#         y = request.POST['y']
#         i = request.FILES['i']
#         b = Movie.objects.create(name=n,desc=d,year=y,img=i)
#         b.save()
#         return home(request)
#     return render(request,'addmovie.html')

class Createview(CreateView):
    model=Movie
    template_name="add1.html"
    fields=['name','desc','year','img']
    success_url=reverse_lazy('movieapp:home')

class Updateview(UpdateView):
    model=Movie
    template_name="add1.html"
    fields=['name','desc','year','img']
    success_url=reverse_lazy('movieapp:home')


class Deleteview(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url=reverse_lazy('movieapp:home')

# def deletemovie(request,p):
#     b=Movie.objects.get(id=p)
#     b.delete()
#     return home(request)

# def editmovie(request,p):
#     b=Movie.objects.get(id=p)
#     form=Movieform(instance=b)
#     if (request.method == "POST"):
#         form = Movieform(request.POST,request.FILES,instance=b)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request, 'add1.html', {'form': form})