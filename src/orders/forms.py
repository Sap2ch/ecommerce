from typing import Any
from django import forms
from .models import Photo, Orders, Category
from users.models import Profile

from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from string import ascii_lowercase, ascii_uppercase, digits
import random


# class MyOrders(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ['photo']
#         widgets = {
#             'photo': forms.FileInput(attrs={'multiple': 'multiple'})
#         }



class MyOrders(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Не вибрано'


    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=5000, label='Про товар', widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    cat = forms.ModelChoiceField(queryset=Category.objects.all())


    class Meta:
        model = Photo
        fields = ['title', 'price', 'description', 'photo', 'cat']
        widgets = {
            'photo': forms.FileInput(attrs={'multiple': 'multiple'})
        }


    def save(self, commit, *args, **kwargs):
        request = kwargs['request']
        photos = request.FILES.getlist('photo')
        image_part_id = 1 if Photo.objects.last() is None else Photo.objects.last().custom + 1

        URL = list(ascii_lowercase + digits)
        random.shuffle(URL) 
        
        Orders.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            slug="".join(URL),
            price=request.POST.get('price'),
            photo_id=image_part_id,
            cat=Category.objects.get(pk=request.POST.get('cat'))
        )
    
        for photo in photos:
            Photo.objects.create(
                photo=photo,
                sender=Profile.objects.get(profile__username=request.user.username),
                # sender=request.user.username,
                custom=image_part_id
            )

        return super().save(commit=False)