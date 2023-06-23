from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'address', 'review_text', 
                  'date_of_vist', 'main_photo', 'photo_1', 'photo_2', 'photo_3',)