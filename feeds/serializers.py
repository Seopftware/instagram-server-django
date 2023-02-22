from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import UserSerializer

class FeedSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Feed
        fields = "__all__"
