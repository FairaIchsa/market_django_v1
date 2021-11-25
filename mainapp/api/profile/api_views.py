from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class UserDataAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserDataSerializer(user)
        return Response(serializer.data)


class UpdateUserDataAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = self.request.data
        user = self.request.user

        user.first_name = data['firstname'] if data['firstname'] is not None else user.first_name
        user.last_name = data['secondname']
        user.father_name = data['fathername']
        user.phone = data['phone']
        user.ship_address = data['ship_adress']
        user.birthday = data['birthday']

        user.save()
        return Response({'status': 'success'})


class UpdateUserPasswordAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = self.request.user
        data = self.request.data

        new_password = data['new_password']
        user.set_password(new_password)
        return Response({'status': 'success'})
