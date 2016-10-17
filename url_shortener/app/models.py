from django.db import models


class Bookmark(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created",)


class Click(models.Model):
    bookmark = models.ForeignKey('app.Bookmark')
    time_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bookmark

    class Meta:
        ordering = ("-time_accessed",)
