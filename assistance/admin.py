from django.contrib import admin
from .models import HelpRequest, HelpReply


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_email',
        'type',
        'status',
        'location',
        'contact_phone',
        'created',
    )
    list_filter = ('status', 'type', 'created')
    search_fields = ('description', 'location', 'user__email')
    readonly_fields = ('created', 'updated')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "User Email"


@admin.register(HelpReply)
class HelpReplyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'request_id',
        'responder_email',
        'short_message',
        'created',
    )
    list_filter = ('created',)
    search_fields = ('message', 'responder__email')
    readonly_fields = ('created',)

    def responder_email(self, obj):
        return obj.responder.email
    responder_email.short_description = "Responder Email"

    def request_id(self, obj):
        return obj.request.id
    request_id.short_description = "Request ID"

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = "Message"
