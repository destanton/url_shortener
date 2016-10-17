from django.contrib import admin
from app.models import Bookmark, Click


admin.site.register([Bookmark, Click])
