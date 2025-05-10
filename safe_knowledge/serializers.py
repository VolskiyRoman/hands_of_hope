from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post_slug', 'user', 'user_email', 'content', 'created']
        read_only_fields = ['id', 'user', 'user_email', 'created']
