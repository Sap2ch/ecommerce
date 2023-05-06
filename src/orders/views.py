from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, FormView
from .forms import MyOrders
from .models import Photo


# class Home(FormView):
#     form_class = MyOrders
#     template_name = 'index.html'
#     success_url = 'add'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

        
#         return context

class Home(FormView):
    model = Photo
    form_class = MyOrders
    template_name = 'index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'

        return context
    
    def post(self, request, *args, **kwargs):
        # images = request.FILES.getlist('photo')
        # image_part_id = Photo.objects.last()
        form = MyOrders(request.POST, request.FILES)

        if form.is_valid():
            form.save(True, request=request)

        return super().post(request, *args, **kwargs)

    

# def home(request):
#     if request.method == 'POST':
#         form = MyOrders(request.POST, request.FILES)
#         photos = request.FILES.getlist('photo')
#         sender = Profile.objects.get(profile__username=request.user.username)
    
#         if form.is_valid():
#             if Photo.objects.last() is None:
#                     for photo in photos:
#                         Photo.objects.create(
#                             photo=photo,
#                             sender=sender,
#                             custom=1
#                         )
#             else:
#                 number = Photo.objects.last().custom + 1
#                 for photo in photos:
#                     Photo.objects.create(
#                         photo=photo,
#                         sender=sender,
#                         custom=number
#                     )

            # user = .objects.get(profile__pk=1)
            # form.save()
            # Photo.objects.create(sender='qwe')

    #     return redirect('home')
    
    # return render(request, 'index.html', {'title': 'Головна сторінка', 'form': MyOrders})

