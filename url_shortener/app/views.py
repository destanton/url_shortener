from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from app.models import Bookmark, Click


class CreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ('title', 'description', 'url')
