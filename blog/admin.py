from django.contrib import admin
<<<<<<< HEAD
=======
from unfold.admin import ModelAdmin
>>>>>>> e950869 (admin, models)
from blog.models import Post, Profile, Tag


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

<<<<<<< HEAD

=======
>>>>>>> e950869 (admin, models)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

<<<<<<< HEAD

=======
>>>>>>> e950869 (admin, models)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
<<<<<<< HEAD
        'id',
        'title',
        'subtitle',
        'slug',
        'publish_date',
        'published',
    )
    list_filter = (
        'published',
        'publish_date',
    )
    list_editable = (
        'title',
        'subtitle',
        'slug',
        'publish_date',
        'published',
    )
    search_fields = (
        'title',
        'subtitle',
        'slug',
        'body',
    )
    prepopulated_fields = {
        'slug': (
            'title',
            'subtitle',
        )
    }
    date_hierarchy = 'publish_date'
    save_on_top = True
=======
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True
>>>>>>> e950869 (admin, models)
