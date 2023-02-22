from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, NotFound
from .serializers import UserSerializer
from .models import User


class MyInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
class SignUpUsers(APIView):
    def post(self, request): # 회원가입
        # is_valid()에서 password 이외 다른 것들은 모두 validation 해주는 중
        password = request.data.get("password")

        if not password:
            raise ParseError

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password) # password hash화
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PublicUser(APIView):
    def get(self, request, username): # 로그인
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Django Auth Login
from django.contrib.auth import authenticate, login
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


import jwt
from django.conf import settings
class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError
        
        # authenticate가 맞다면, user객체 반환
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            # token안에 담을 정보
            # 토큰이 암호화된 것은 아니기 때문에 민감한 정보를 넣으면 안됨.
            # 지금은 유저 아이디만 넣자.
            token = jwt.encode(
                {"id":user.id},
                settings.SECRET_KEY, #서명
                algorithm="HS256"
            )
            return Response({"token":token})
        else:
            return Response({"error":"wrong password"})

from django.contrib.auth import logout
class Logout(APIView):
    # 인증된 요청에 한해서 뷰 호출 허용 (로그인이 되어있어야만 접근 허용)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"msg":"logout success"})