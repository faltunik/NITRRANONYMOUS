from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  blank=True, null=True, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts',)
    image = models.FileField(upload_to= 'photos/%Y/%m/%d', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class meta:
        ordering = ['-id']


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # taking some property from save method of this class and calling it
        if self.image:  # checking whther it has image or not
            img = Image.open(self.image)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    # def rename_image(self):
    #     return self.image.name.split('/')[-1]


    def number_of_likes(self):
        return self.like.count()

    def __str__(self):
        return self.content[:15]

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parentchild')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='commentslike', blank=True)


    @property
    def is_parent(self):
        return True if self.parent is None else False

    @property
    def children(self):
        return Comment.objects.filter(parent=self)

    def __str__(self):
        return self.body[:15]


class Subly(models.Model):
    body = models.TextField()
    comment = models.ForeignKey(Comment, on_delete= models.CASCADE, related_name= 'subly')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  blank=True, null=True, on_delete=models.CASCADE, related_name='subly')

    def __str__(self):
        return self.body[:15]
