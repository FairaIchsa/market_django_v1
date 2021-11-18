from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.authentication import authenticate

from .serializers import *
from ...models import User


# @method_decorator(csrf_protect, name='dispatch')
class SignUpAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = self.request.data

        email = data['email']
        username = data['username']
        password = data['password']
        first_name = data['firstname']
        last_name = data['secondname']
        father_name = data['fathername']
        phone = data['phone']
        ship_address = data['ship_adress']
        birthday = data['birthday']

        if User.objects.filter(username=username).exists():
            return Response({'error': 'username already exists.'})

        try:
            user = User.objects.create_user(
                email=email, username=username, password=password, first_name=first_name, last_name=last_name,
                father_name=father_name, phone=phone, ship_address=ship_address, birthday=birthday
            )
            return Response(SignUpOutputSerializer(user).data)
        except:
            return Response({'status': 'something went wrong('})


# @method_decorator(csrf_protect, name='dispatch')
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = self.request.data

        username = data['username']
        password = data['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return Response({'status': 'authenticated'})
        return Response({'status': 'something went wrong again('})


class LogoutAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        try:
            auth.logout(request)
            return Response({'status': 'logged out'})
        except:
            return Response({'status': 'something went wrong('})


# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFTokenAPIView(APIView):
#     permission_classes = (AllowAny, )
#
#     def get(self, request):
#         return Response({'success':  'CSRF cookie set'})
