from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from .serializers import FeedSerializer

class AllFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(
            all_feeds,
            many=True
        )

        return Response(serializer.data)