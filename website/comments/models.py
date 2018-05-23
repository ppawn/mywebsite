from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=300)
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20] + '...'

class Visit_Comment(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:20] + '...'
