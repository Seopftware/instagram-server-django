from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from multiprocessing import AuthenticationError
from django.conf import settings
from users.models import User

import jwt

# BaseAuthentication을 상속받아서 나만의 인증 모델 구조를 만들 수 있음.
class JWTAuthentication(BaseAuthentication):
    # BaseAuthentication를 상속받은 함수에서 authenticate를 사용하면,
    # API request가 있을때마다 자동으로 호출된다.
    def authenticate(self, request): # request: 헤더, URL, 쿠키, IP주소등이 담겨 있음.
        token = request.headers.get("jwt")

        # (1) 토큰 값이 없거나
        if not token:
            return None

        # 복호화 (<=> 암호화 encode)
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        id = decoded.get("id")

        # (2) id값이 없을 때 반환
        if not id:
            raise AuthenticationFailed("Invalid Token")
        
        try:
            user = User.objects.get(id=id)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed("User Not Found")