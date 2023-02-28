from django.shortcuts import render
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MyInfo(APIView):
    # 로그인한 유저만 허용하겠다. MyInfo 호출을.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        # Serialize화 해줘야 -> 유저한테 보낼 수 있다.
        serializer = UserSerializer(user)

        return Response(serializer.data)

# django의 session을 활용한 로그인
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate, login
from rest_framework import status
class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError()
        
        user = authenticate(
            request,
            username = username,
            password = password
        )
        print(user)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

# django의 session을 활용한 로그아웃
from django.contrib.auth import logout
class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

import jwt
from django.conf import settings
class JWTLogin(APIView):
    def post(self, request):
        username = request.data.gate("username")
        password = request.data.gate("password")

        if not username or not password:
            raise ParseError
        
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            token = jwt.encode(
                {"id":user.id, "username":user.username},
                settings.SECRET_KEY,
                algorithm="HS256"
            )
            print(token)
            return Response({"token":token})