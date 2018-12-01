
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse,Http404
from django.views.generic.edit import CreateView,DeleteView,UpdateView  # form to create new object
import django.views.generic as gen
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

from .models import Album,Song
from .users import UserForm,MyUser
# # Create your views here.


class IndexView(gen.ListView):
    template_name='music/index.html'
    context_object_name='all_albums'
    def get_queryset(self):
        return Album.objects.all()
# def index(request):
#     all_albums=Album.objects.all()
#     template=loader.get_template('music/index.html')
#     context= {
#         'all_albums':all_albums
#     }


#     return HttpResponse(template.render(context,request))

#----------------------html and python jumbled------------------
# def index(request):
#     all_albums=Album.objects.all()
#     html=''
#     for album in all_albums:
#         url= '/music/'+str(album.id)+'/'
#         html+='<a href="'+url+'">'+album.album_title+'</a><br>'
#     return HttpResponse(html)

class DetailsView(gen.detail.DetailView):
    model=Album
    template_name='music/detail1.html'
    context_object_name='alb'
    
# def detail(request,album_id):
#    album=get_object_or_404(Album,pk=album_id)
#    return render(request,'music/detail1.html',{'alb':album,'no_song_err':'Oops! why there\'s no song in here?'})

# def detail(request,album_id):
#     try:
#         al=Album.objects.get(pk=album_id)
#     except: #Album.DoesNotExist:
#         raise Http404('Sorry! Album doesn\'t exist' )
#     return render(request,'music/detail.html',{'alb':al})

# def detail(request,album_id):
#     return HttpResponse('<h1>Details for album:'+str(album_id)+' </h2>')

# def favourite(request, album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song=album.song_set.get(pk=request.POST['song'])
#     except (KeyError,Song.DoesNotExist):
#         return render(request, 'music/detail.html',{'alb':album, 'error_mes':'you did not select a valid song'})
#     else:
#         selected_song.is_favourite=True
#         selected_song.save()
#         return render(request,'music/detail.html',{'alb':album}) #here, 'music/detail.html is basically the folder directory, not the url pattern'

class AlbumCreate(CreateView):    #to create a new album
    model=Album
    fields=['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):    #to update/edit an album
    model=Album
    fields=['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):    #to delete an album
    model=Album
    success_url=reverse_lazy('music_index')

class UserFormView(gen.View):
    form_class=UserForm
    template_name='music/registration.html'


    def get(self,request):
        form= self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music_index')        
        return render(request,self.template_name,{'form':form})


class UserLoginView(gen.View):
    form_class=MyUser
    template_name='music/homepage1.html'

    def get(self,request):
        form= self.form_class(None)
        return render(request,self.template_name,{'login':form})
        
    def post(self,request):
        form=self.form_class(request.POST)

        username=form.cleaned_data['username']
        password=form.cleaned_data['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('music_index')