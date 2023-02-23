from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):
    user = UserSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Feed
        fields = "__all__"
