from django.conf import settings
from django.db import models
from django.conf import settings

<<<<<<< HEAD

=======
>>>>>>> e950869 (admin, models)
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

<<<<<<< HEAD

def __str__(self):
    return self.user.get_username()


=======
    def __str__(self):
        return self.user.get_username()
    
>>>>>>> e950869 (admin, models)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
<<<<<<< HEAD


=======
    
>>>>>>> e950869 (admin, models)
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
<<<<<<< HEAD
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-publish_date']
=======

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_date"]
        
>>>>>>> e950869 (admin, models)
