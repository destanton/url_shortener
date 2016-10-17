from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from app.models import Bookmark, Click
from random import choice
from string import ascii_letters, digits


class CreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ('title', 'description', 'url')

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["bookmark_list"] = Bookmark.objects.all()
            return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.new_url = ""
        for i in range(8):
            instance.new_url += choice(ascii_letters + digits)
        return super().form_valid(form)


class ShortView(View):
    model = Bookmark
    # success_url =
    pass
