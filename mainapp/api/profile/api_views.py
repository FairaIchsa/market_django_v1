from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class UserDataAPIView(APIView):
    # authentication_classes = [SessionAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
            serializer = UserDataSerializer(user)
            return Response(serializer.data)
        return Response('User is not authenticated')

