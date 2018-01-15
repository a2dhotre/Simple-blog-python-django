from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.
#Model for Post
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #after creating post the page will go back to this view
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

# Model for a Comment
class Comments(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    #after creating comment the page will go back to this view
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
