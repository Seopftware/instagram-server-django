from rest_framework.serializers import ModelSerializer
from .models import User

# ModelSerializer: 
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"

        fields = (
            "id",
            "email",
            "username",
            "profileImg",
            "profileIntroduce"
        )