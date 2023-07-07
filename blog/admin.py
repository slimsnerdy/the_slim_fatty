from django.contrib import admin
from .models import Post, PostImage
from django.utils.html import format_html


# Register your models here.

class PostImageInline(admin.StackedInline):
    model = PostImage
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        return format_html('<img src="{0}" style="width: 64px; height: 64px; object-fit: cover;" />'.format(obj.image.url))
    image_preview.short_description = 'Image Preview'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'image_preview')    #tuple (immuatable; read-only)
    # list_display = ('title', 'slug', 'status','created_on')   #no image_preview mode..
    list_filter = ('status',)                                                    #tuple w one value, needs comma
    search_fields = ['title']                                        #list (mutable)
    prepopulated_fields = {'slug': ('title',)}                                  #dictionary
    inlines = [PostImageInline]
    readonly_fields = ('image_preview',)
    
    class Meta:
        model = Post

    def image_preview(self, obj):
        return format_html('<img src="{0}" style="width: 64px; height: 64px; object-fit: cover;" />'.format(obj.image.url))
    image_preview.short_description = 'Image Preview'


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'image_preview', )
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{0}" style="width: 64px; height: 64px; object-fit: cover;" />'.format(obj.image.url))
    image_preview.short_description = 'Image Preview' 

    @admin.display(description='Title', ordering='post__title')
    # @admin.display(ordering='book__author', description='Author')
    def get_title(self, obj):
        return obj.post.title
# https://stackoverflow.com/a/164631/1064843