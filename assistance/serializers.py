from rest_framework import serializers
from .models import HelpRequest, HelpReply
from .enums import HelpTypeEnum, HelpStatusEnum


class HelpReplySerializer(serializers.ModelSerializer):
    responder_email = serializers.EmailField(source='responder.email', read_only=True)

    class Meta:
        model = HelpReply
        fields = ['id', 'request', 'responder', 'responder_email', 'message', 'created']
        read_only_fields = ['id', 'responder', 'responder_email', 'created']


class HelpRequestSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    replies = HelpReplySerializer(many=True, read_only=True)

    type = serializers.ChoiceField(
        choices=[(tag.value, tag.name.replace('_', ' ').title()) for tag in HelpTypeEnum]
    )
    status = serializers.ChoiceField(
        choices=[(tag.value, tag.name.replace('_', ' ').title()) for tag in HelpStatusEnum],
        read_only=True
    )

    class Meta:
        model = HelpRequest
        fields = [
            'id', 'user', 'user_email', 'type', 'description', 'location', 'contact_phone',
            'status', 'created', 'updated', 'replies'
        ]
        read_only_fields = ['id', 'user', 'user_email', 'status', 'created', 'updated', 'replies']
