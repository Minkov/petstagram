from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from petstagram.common.forms import CommentForm
from .forms import PhotoAddForm, PhotoEditForm
from django.views import generic as views
from .models import Photo


class PhotoAddView(views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoAddForm

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


# @login_required
# def photo_add(request):
#     form = PhotoAddForm()
#
#     if request.method == "POST":
#         form = PhotoAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'photos/photo-add-page.html', context=context)


@login_required
def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "likes": photo.like_set.count(),
        "comments": photo.comment_set.all(),
        "comment_form": comment_form,
    }

    return render(
        request,
        'photos/photo-details-page.html',
        context=context
    )


@login_required
def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(instance=photo)

    if request.method == "POST":
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=pk)

    context = {
        "photo": photo,
        "form": form,
    }

    return render(request, 'photos/photo-edit-page.html', context)


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
