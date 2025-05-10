from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_slug', 'user', 'content', 'created')
    list_filter = ('post_slug', 'user', 'created')
    search_fields = ('content', 'post_slug', 'user__email')
    readonly_fields = ('created',)
    ordering = ('-created',)