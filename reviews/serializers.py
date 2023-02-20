from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
# from feeds.serializers import FeedSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    user = UserSerializer(read_only=True) # res에서는 보이고, req에서는 param에 포함 X

    class Meta:
        model = Review
        fields = "__all__"