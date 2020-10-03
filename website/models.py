from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    def full_desc(self):
        return self.title + self.sub_title

    full_desc.admin_order_field = 'title'