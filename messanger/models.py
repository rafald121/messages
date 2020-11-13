from django.db import models

# Create your models here.


class Message(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=160, blank=False, null=False)
    views_count = models.PositiveIntegerField(default=0)

    def reset_views_count(self):
        self.views_count = 0
        self.save()

    def increment_views_count(self):
        self.views_count += 1
        self.save()
