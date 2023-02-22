from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Feed
from users.models import User
from .serializers import FeedSerializer

class Feeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(
            all_feeds,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            feed = serializer.save()
            return Response(
                FeedSerializer(feed).data,
            )
        else:
            return Response(serializer.errors)

class UserFeeds(APIView):
    def get(self, request, username):
        owner_id = User.objects.get(username=username)
        all_feeds = Feed.objects.filter(owner_id=owner_id)
        serializer = FeedSerializer(
            all_feeds,
            many=True,
        )
        return Response(serializer.data)