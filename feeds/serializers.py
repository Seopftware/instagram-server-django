from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer
from .models import Feed

class FeedSerializer(ModelSerializer):

    owner = UserSerializer()
    reviews = ReviewSerializer(many=True, read_only=True) # feed.review_set.all()

    class Meta:
        model = Feed
        fields = "__all__"
