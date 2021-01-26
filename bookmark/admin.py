from django.contrib import admin

# Register your models here.
from .models import Bookmark, Tag, Tag2Bookmark


class Tag2BookmarkInline(admin.TabularInline):
    model = Tag2Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    inlines = (Tag2BookmarkInline,)


class TagAdmin(admin.ModelAdmin):
    inlines = (Tag2BookmarkInline,)


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tag2Bookmark)
